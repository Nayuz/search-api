import os
import json
from typing import List
from datetime import datetime
from app.schema.search import Trademark, SearchQuery

# 단일 파일일 경우, path의 파일을 불러와 로드하는 코드
# def load_data(path:str) -> List[Trademark]:
#     with open(path, encoding='utf-8') as file:
#         raw = json.load(file)
#         return [Trademark(**item) for item in raw]

_cached_data : List[Trademark] = []

def preload_data(dir : str = "data"):
    global _cached_data
    if _cached_data: #이미 로드된 경우 생략
        return
    _cached_data = load_data(dir)

def get_trademarks() -> List[Trademark]:
    return _cached_data

def load_data(dir :str = "data") -> List[Trademark]:
    result = []
    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            filepath = os.path.join(dir, filename)
            with open(filepath, encoding='utf-8') as file:
                raw = json.load(file)
                for item in raw:
                    # 모든 필드에 None이 있을 수 있다고 생각하고 체크
                    for key, value in item.items():
                        if isinstance(value, list):
                            item[key] = [x for x in value if x is not None]
                            if not item[key]:
                                item[key] = None
                        elif value is None:
                            item[key] = None
                    result.append(Trademark(**item))
    return result
    
def filter_trademark(data: List[Trademark], query: SearchQuery) -> List[Trademark]:
    result = []
    for item in data:
        match = False
        for field, value in query.model_dump(exclude_none=True).items():
            item_value = getattr(item, field, None)
            if isinstance(value, list):
                #None이 아니고, 값이 일치하는 경우 True로
                if item_value is not None and any(v in item_value for v in value):
                    match = True
                    break
        if match:
            result.append(item)
    return result

# field : applicationDate, publicationDate, registrationDate, internationalRegDate
def filter_trademark_by_date(data:List[Trademark],
                             field:str,
                             start_date:str,
                             end_date:str) -> List[Trademark]:
    result = []

    start = datetime.strptime(start_date, "%Y%m%d")
    end = datetime.strptime(end_date, "%Y%m%d")

    for item in data:
        item_value = getattr(item, field, None)

        if item_value:
            item_date = datetime.strptime(item_value, "%Y%m%d")
            if start <= item_date <= end:
                result.append(item)
    return result