from fastapi import APIRouter

router = APIRouter()


## 연결이 되나 테스트해보기 위한 코드
@router.get("/ping")
async def ping():
    return {"message":"pong"}