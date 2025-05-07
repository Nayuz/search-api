from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import endpoint
from app.service.search import preload_data

# 실행 시 데이터 로드를 위한 함수
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("데이터 로드 시작...")
    preload_data()
    print("데이터 로드 완료")
    yield
    print("종료됨")



app = FastAPI(lifespan=lifespan)



# 라우터 등록
app.include_router(endpoint.router)



# 실행코드
# uvicorn app.main:app --reload