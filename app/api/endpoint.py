from fastapi import APIRouter, Query
from app.schema.search import SearchQuery, Trademark
from app.service.search import get_trademarks, filter_trademark, filter_trademark_by_date


router = APIRouter()


## 연결이 되나 테스트해보기 위한 코드
@router.get("/ping")
async def ping():
    return {"message":"pong"}


# 프로토타입, 뭐든지 입력받아서 검색 가능한 상태
@router.post("/search", response_model=list[Trademark])
def search_trademark(query: SearchQuery):
    print(f"[DEBUG] 받은 요청 데이터: {query}")
    print(f"[DEBUG] 모델 덤프: {query.model_dump()}")
    data = get_trademarks()
    result = filter_trademark(data, query)
    return result
    
######
##  각 항목마다 입력받아서 검색하기
######


@router.get("/search/productname", response_model = list[Trademark])
def search_by_product_name(search : str = Query(...)):
    data = get_trademarks()
    query = SearchQuery(productName=[search], productNameEng=[search])
    result = filter_trademark(data, query)
    return result

@router.get("/search/applicationnumber", response_model= list[Trademark])
def search_by_application_number(search : str = Query(...)):
    data = get_trademarks()
    query = SearchQuery(applicationNumber=[search])
    result = filter_trademark(data, query)
    return result

@router.get("/search/registerstatus", response_model=list[Trademark])
def search_by_register_status(search : str = Query(...)):
    data = get_trademarks()
    query = SearchQuery(registerStatus=[search])
    result = filter_trademark(data, query)
    return result

@router.get("/search/internationnumber", response_model=list[Trademark])
def search_by_internation_number(search : str = Query(...)):
    data = get_trademarks()
    query = SearchQuery(internationalRegNumbers=[search])
    result = filter_trademark(data, query)
    return result

# 출원일
@router.get("/search/applicationdate", response_model=list[Trademark])
def search_by_application_date(start_date: str = Query(...), end_date: str = Query(...)):
    data = get_trademarks()
    result = filter_trademark_by_date(data, "applicationDate", start_date, end_date)
    return result

# 공고일
@router.get("/search/publicationdate", response_model=list[Trademark])
def search_by_publication_date(start_date: str = Query(...), end_date: str = Query(...)):
    data = get_trademarks()
    result = filter_trademark_by_date(data, "publicationDate", start_date, end_date)
    return result

# 등록일
@router.get("/search/registrationdate", response_model=list[Trademark])
def search_by_registration_date(start_date: str = Query(...), end_date: str = Query(...)):
    data = get_trademarks()
    result = filter_trademark_by_date(data, "registrationDate", start_date, end_date)
    return result

# 국제출원일
@router.get("/search/internationalregdate", response_model=list[Trademark])
def search_by_international_date(start_date:str = Query(...), end_date : str = Query(...)):
    data = get_trademarks()
    result = filter_trademark_by_date(data, "internationalRegDate", start_date, end_date)
    return result
