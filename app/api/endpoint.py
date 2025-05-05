from fastapi import APIRouter
from app.schema.search import SearchQuery, Trademark
from app.service.search import get_trademarks, filter_trademark
router = APIRouter()


## 연결이 되나 테스트해보기 위한 코드
@router.get("/ping")
async def ping():
    return {"message":"pong"}


@router.post("/search", response_model=list[Trademark])
def search_trademark(query: SearchQuery):
    data = get_trademarks()
    result = filter_trademark(data, query)
    return result