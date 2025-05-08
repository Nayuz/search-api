# search-api

데이터셋 컬럼 정의
- productName: 상표명(한글)
- productNameEng: 상표명(영문)
- applicationNumber: 출원 번호
- applicationDate: 출원일 (YYYYMMDD 형식)
- registerStatus: 상표 등록 상태 (등록, 실효, 거절, 출원 등)
- publicationNumber: 공고 번호
- publicationDate: 공고일 (YYYYMMDD 형식)
- registrationNumber: 등록 번호
- registrationDate: 등록일 (YYYYMMDD 형식)
- internationalRegNumbers: 국제 출원 번호
- internationalRegDate: 국제출원일 (YYYYMMDD 형식)
- priorityClaimNumList: 우선권 번호
- priorityClaimDateList: 우선권 일자 (YYYYMMDD 형식)
- asignProductMainCodeList: 상품 주 분류 코드 리스트
- asignProductSubCodeList: 상품 유사군 코드 리스트
- viennaCodeList: 비엔나 코드 리스트



### 과제
**데이터 내 다양한 결측치(null 값), 리스트 형태의 필드가 존재합니다. 이를 적절히 처리해주세요.**

> **상표 데이터를 검색할 수 있는 API를 1개 이상 구현하세요.**

> **Python 기반의 FastAPI 프레임워크를 사용해 개발해 주세요.**

> **최소한 하나 이상의 필터링 기능을 포함하세요. (예: 등록 상태, 상품 코드, 날짜 등)**

> 키워드가 정확하게 일치하지 않더라도 사용자가 원하는 결과를 찾을 수 있는 방법을 고민해보세요.
> 
> 사용자 편의를 위해 검색 품질을 높일 수 있는 방안을 생각해보세요.
> 
> 데이터가 대량(예: 10만 건 이상)으로 늘어났을 경우의 확장성을 고려하면 좋습니다
>
> 코드의 효율성과 가독성을 높이기 위해 노력해주세요.




---

python 3.12에서 작성해보려 함. -> 가장 안정화되어있는 최신버전으로 알고 있음

python 3.12 기준, deprecated 된 코드는 가능한 피해서 작성하는것이 목표.



data가 단일 파일인 경우를 고려하여 작성했지만,

이후에 데이터가 늘어날 것을 고려해서 해당 경로 안의 '.json' 확장자 파일 전부를 로드하는것으로 작성.

---

항목과 항목의 내용을 JSON방식으로 채워서 POST /search 에 요청하면 답을 받을 수 있음.


---

POST /search 의 경우, JSON으로 모든 항목을 동시에 검색할 수 있지만 검색하는데에 조금 번거로움이 있음.

그러므로 GET /search/productname, GET /search/applicationnumber 등으로 나누어 결과물을 받는 API를 조금 더 편리하게 호출해보고자 함.

결과

GET /search/productname, GET /search/applicationnumber, GET /search/resisterstatus, GET /search/internationnumber

요청하면 해당 항목을 포함한 결과를 검색해 보여줌.

---

