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

