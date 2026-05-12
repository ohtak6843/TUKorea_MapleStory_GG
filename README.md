# TUKorea Maplestory GG

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Nexon API](https://img.shields.io/badge/API-Nexon%20Open%20API-red)
![Status](https://img.shields.io/badge/Status-Completed-success)


## 📖 프로젝트 소개

**TUKorea Maplestory GG** 는 넥슨 메이플스토리 Open API 와 다양한 외부 공공 API 를 활용하여 메이플스토리 캐릭터의 정보를 손쉽게 검색하고 시각화해 주는 데스크톱 애플리케이션입니다.

게임 클라이언트에 접속하지 않고도 캐릭터의 **기본 정보, 능력치(스탯), 하이퍼 스탯, 어빌리티, 유니온, 무릉도장 기록, 인기도, 경험치 성장 그래프** 등을 한눈에 확인할 수 있으며, 이메일 전송 및 PC방 위치 안내(공공데이터 API + Google Maps)와 같은 부가 기능까지 통합 제공합니다.

> 한국공학대학교(TUKorea) 캡스톤/팀 프로젝트로 진행되었으며, 여러 외부 API 를 하나의 GUI 안에서 활용하는 통합 사례를 목표로 합니다.


## 👨‍💻 개발자

| 이름 | GitHub |
| --- | --- |
| 오현택 | [@ohtak6843](https://github.com/ohtak6843) |
| 박우진 | [@Lucianne0424](https://github.com/Lucianne0424) |


## 📅 개발 기간

- **개발 기간:** 2024년 5월 ~ 2024년 6월
- **상태:** 완료(Completed)

### 주요 마일스톤

1. 넥슨 메이플스토리 Open API 연동 및 `MapleInfo` 데이터 모델 설계
2. Tkinter 기반 메인 검색 GUI(`SearchGUI`) 구현
3. 하이퍼 스탯 / 어빌리티 / 성장치 보조 화면 추가
4. SMTP(Gmail) 기반 이메일 전송 기능 통합
5. Google Maps + 공공데이터 API 를 활용한 시흥시 PC방 지도 뷰(`MapGUI`) 추가
6. C 확장 모듈(`spammodule.c` → `spam2.pyd`) 빌드로 날짜 계산 가속


## 💻 개발 환경

| 항목 | 내용 |
| --- | --- |
| OS | Windows 10/11 |
| IDE | JetBrains PyCharm (`.idea` 디렉터리 포함) |
| 언어 | Python 3.x, C (Python 확장 모듈) |
| 빌드 도구 | `distutils` / `setuptools` (C 확장 빌드용) |
| 패키지 매니저 | pip |
| 버전 관리 | Git / GitHub |


## 🛠️ 기술 스택

### Language
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?logo=c&logoColor=white)

### GUI / Frontend
| 라이브러리 | 용도 |
| --- | --- |
| `tkinter`, `tkinter.ttk` | 메인 GUI 윈도우, 위젯, 다이얼로그 |
| `Pillow (PIL)` | 캐릭터/배경 이미지 로드 및 리사이즈 |

### 외부 API 연동
| 라이브러리 / 서비스 | 용도 |
| --- | --- |
| Nexon Open API (MapleStory) | 캐릭터 OCID, 기본 정보, 스탯, 하이퍼 스탯, 어빌리티, 유니온, 무릉도장, 인기도 조회 |
| Google Maps Static API | 지도 이미지 렌더링 및 마커 표시 |
| `googlemaps` (Python Client) | 지오코딩(주소 → 좌표) |
| `geopy` (Nominatim) | OpenStreetMap 기반 보조 지오코딩 |
| 공공데이터포털 API (odcloud) | 시흥시 PC방(인터넷컴퓨터게임시설제공업) 현황 |
| `requests` | HTTP 통신 |

### 부가 기능
| 라이브러리 | 용도 |
| --- | --- |
| `smtplib`, `email.mime` | Gmail SMTP 를 통한 캐릭터 정보 이메일 전송 |
| `telepot` | Telegram 봇을 통한 PC방 정보 알림 (`teller.py`, `noti.py`) |
| 자체 C 확장 모듈 `spam2.pyd` | 날짜 계산 등 성능 보조 |

### Build / DevOps
![PyCharm](https://img.shields.io/badge/PyCharm-000000?logo=pycharm&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)


## ✨ 주요 기능

- **🔍 캐릭터 검색**
  캐릭터 명을 입력하면 Nexon Open API 를 호출하여 OCID 를 조회하고, 해당 캐릭터의 기본 정보(레벨, 직업, 길드, 캐릭터 이미지)와 능력치를 화면에 표시합니다.

- **📊 능력치(Stat) 상세 보기**
  전투력, HP, STR/DEX/INT/LUK, 최종 데미지, 보스/일반 몬스터 데미지, 크리티컬 확률·데미지, 메소 획득량, 아이템 드롭률, 스타포스/아케인포스/어센틱포스 등 30여 종의 스탯을 카테고리별로 정렬해 한 화면에 출력합니다.

- **⚡ 하이퍼 스탯 / 어빌리티 패널 토글**
  버튼 클릭으로 하이퍼 스탯 표(17종 능력치 레벨)와 어빌리티 등급(레전드리/유니크/에픽/레어 색상 구분) 정보를 메인 창 오른쪽에 펼쳐서 보여 줍니다.

- **📈 경험치 성장치 그래프**
  최근 7일간의 일자별 경험치 비율을 Canvas 막대 그래프로 시각화하여 캐릭터의 성장 추이를 한눈에 파악할 수 있게 합니다. 날짜 계산은 자체 C 확장 모듈(`spam2.pyd`)을 통해 처리합니다.

- **🏰 유니온 · 무릉도장 · 인기도 표시**
  단순 스탯 외에도 유니온 레벨, 무릉도장 최고 층수, 인기도 점수를 캐릭터 정보 패널에 함께 노출하여 종합적인 캐릭터 가치를 확인할 수 있습니다.

- **📧 이메일 전송 기능**
  검색한 캐릭터의 능력치를 사용자가 입력한 이메일 주소로 Gmail SMTP 를 통해 자동 발송합니다. 결과를 외부에 공유하거나 백업하는 용도로 활용할 수 있습니다.

- **🗺️ PC방 지도 뷰 (보너스 기능)**
  공공데이터포털의 시흥시 인터넷컴퓨터게임시설제공업 데이터를 받아 PC방 목록을 표시하고, 선택 시 Google Maps Static API 로 해당 위치를 지도 위에 마커로 표시합니다. 줌인/줌아웃 버튼도 제공합니다.

- **🤖 텔레그램 봇 알림 (보너스 기능)**
  Telegram 봇 명령(`상호 [상호명]`, `주소 [주소]`)을 받아 PC방 정보를 조회·응답하는 메시지 봇 인터페이스를 함께 제공합니다.


## 📁 폴더 구조

```
TUKorea_MapleStory_GG/
├── .idea/                  # PyCharm 프로젝트 설정
├── image/                  # GUI 배경 이미지 (캐릭터창, 하이퍼/어빌리티/스탯 UI 등)
├── MapleInfo.py            # Nexon Open API 래퍼 클래스
├── SearchGUI.py            # 메인 캐릭터 검색 GUI
├── TitleGUI.py             # 타이틀(인트로) 화면
├── MapGUI.py               # PC방 지도 뷰 GUI (Google Maps + 공공데이터)
├── teller.py               # Telegram 봇 메시지 핸들러
├── noti.py                 # Telegram 토큰 / 알림 유틸
├── spammodule.c            # C 확장 모듈 소스(날짜 계산)
├── spam2.pyd               # 빌드된 C 확장(Windows)
├── test.py                 # 테스트 스크립트
├── .gitattributes
└── .gitignore
```


## 🖼️ 스크린샷

### 타이틀 화면
메인 진입 화면에서 **캐릭터 검색** 또는 **PC방 찾기** 기능을 선택할 수 있습니다.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f1db268-f289-46b9-a8fa-d28dd48e1ac7" alt="타이틀 화면" width="600"/>
</p>

### 캐릭터 검색 화면
캐릭터 명을 입력하여 검색하면 캐릭터 정보, 능력치, 하이퍼 스탯, 어빌리티를 한눈에 확인할 수 있습니다.

<p align="center">
  <img src="https://github.com/user-attachments/assets/39291d03-0072-416e-9095-b867380b0c5c" alt="캐릭터 검색 화면" width="700"/>
</p>

### PC방 지도 뷰
공공데이터 API 와 Google Maps 를 활용하여 시흥시 PC방 목록 및 위치를 지도 위에 표시합니다.

<p align="center">
  <img src="https://github.com/user-attachments/assets/defb9090-d1ed-495b-8940-b1a931db457b" alt="PC방 지도 뷰" width="700"/>
</p>


## ⚠️ 주의 사항

- **C 확장 모듈(`spam2.pyd`)** 은 Windows 64-bit Python 용으로 빌드되어 있습니다. 다른 환경에서는 `spammodule.c` 를 다시 컴파일해야 합니다.
  ```bash
  python setup.py build_ext --inplace
  ```
- Nexon Open API 는 **하루 단위 데이터 갱신** 정책이 있으므로, 당일 캐릭터 정보가 즉시 반영되지 않을 수 있습니다.
- Gmail SMTP 전송 기능을 사용하려면 발신 계정에서 **앱 비밀번호**를 발급받아야 합니다.
- 저장소에 포함된 API 키들은 테스트용이며, 실제 사용 시 본인 키로 교체하고 환경 변수 또는 `.env` 파일로 분리하는 것을 권장합니다.
