import os
import json
from typing import List
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
                    result.append(Trademark(**item))
    return result
    
def filter_trademark(data: List[Trademark], query: SearchQuery) -> List[Trademark]:
    result = []
    for item in data:
        match = True
        for field, value in query.model_dump(exclude_none=True).items():
            item_value = getattr(item, field)
            if isinstance(value, list):
                if not item_value or not any(single_value in item_value for single_value in value):
                    match = False
                    break
                else:
                    if item_value != value:
                        match = False
                        break
            if match:
                result.append(item)
    return result