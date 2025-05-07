from typing import List, Optional
from pydantic import BaseModel


class Trademark(BaseModel):
    productName: Optional[str]                #상표명(한글)
    productNameEng: Optional[str]   #상표명(영문)
    applicationNumber: Optional[str]              #출원 번호
    applicationDate: Optional[str]      #출원일 (YYYYMMDD 형식)
    registerStatus: Optional[str]       #상표 등록 상태 (등록, 실효, 거절, 출원 등)
    publicationNumber: Optional[str]    #공고 번호
    publicationDate: Optional[str]      #공고일 (YYYYMMDD 형식)
    registrationNumber: Optional[List[str]]   #등록 번호
    registrationDate: Optional[List[str]]     #등록일 (YYYYMMDD 형식)
    internationalRegNumbers: Optional[str]  #국제 출원 번호
    internationalRegDate: Optional[str]     #국제출원일 (YYYYMMDD 형식)
    priorityClaimNumList: Optional[List[str]]   #우선권 번호
    priorityClaimDateList: Optional[List[str]]  #우선권 일자 (YYYYMMDD 형식)
    asignProductMainCodeList: Optional[List[str]]   #상품 주 분류 코드 리스트
    asignProductSubCodeList: Optional[List[str]]    #상품 유사군 코드 리스트
    viennaCodeList: Optional[List[str]]     #비엔나 코드 리스트

class SearchQuery(BaseModel):
    productName: Optional[List[str]] = None
    productNameEng: Optional[List[str]] = None
    applicationNumber: Optional[List[str]] = None
    applicationDate: Optional[List[str]] = None
    registerStatus: Optional[List[str]] = None
    publicationNumber: Optional[List[str]] = None
    publicationDate: Optional[List[str]] = None
    registrationNumber: Optional[List[str]] = None
    registrationDate: Optional[List[str]] = None
    internationalRegNumbers: Optional[List[str]] = None
    internationalRegDate: Optional[List[str]] = None
    priorityClaimNumList: Optional[List[str]] = None
    priorityClaimDateList: Optional[List[str]] = None
    asignProductMainCodeList: Optional[List[str]] = None
    asignProductSubCodeList: Optional[List[str]] = None
    viennaCodeList: Optional[List[str]] = None