
# PyKartRider
- A Python Library for Kartrider official API. For official documentation, please check [Here](https://developers.nexon.com/kart/apiList).
- 카트라이더 공식 API를 파이썬에서 활용할 수 있게 해주는 간단한 파이썬 라이브러리입니다.

## Installation (설치)
1. Clone this repository by `git clone https://github.com/gooday2die/PyKartRider.git`
2. Change directory inside the repository by `cd ./PyKartRider`
3. Install this package by `pip install .`
---
4. 이 프로젝트를 Clone 합니다. `git clone https://github.com/gooday2die/PyKartRider.git`
5. cd 로 디렉토리 안으로 이동합니다 `cd ./PyKartRider`
6. 패키지를 `pip install .` 으로 설치합니다. 

## Dependency & Environment (의존성과 환경)
- [requests](https://github.com/psf/requests)
- Confirmed this script working in `Python 3.8.10`
- 이 스크립트는 `Python 3.8.10` 에서 동작을 확인했습니다.

## Functions (함수)
### User Information (유저정보)
**1.  **Retrieving User ID by Name (라이더명으로 유저 정보 조회)****
- This function retrieves User ID and the user's Level  by Name. This function returns `tuple` object as its return value.
- 이 함수는 유저의 닉네임을 가지고 유저 ID 와 유저의 레벨을 조회합니다. 이 함수는 `tuple` 타입으로 결과를 반환합니다.
   `>>> from PyKartRider import userInfo`
    `>>> PyKartRider.userInfo.get_user_id('o양파극혐o')`
    `('1728506595', 78)`

**2.  **Retrieving Name by User ID (유저 고유 식별자로 라이더명 조회)****
- This function retrieves User Name and user's Level by User ID. This function returns `tuple` object as its return value.
- 이 함수는 유저 ID를 가지고 유저의 닉네임과 유저의 레벨을 조회합니다. 이 함수는 `tuple` 타입으로 결과를 반환합니다.
`>>> from PyKartRider import userInfo`
`>>> PyKartRider.userInfo.get_user_name('1728506595')`
`('o양파극혐o', 78)`

### Match Information (매치정보)
**1. Getting All Match Information (유저 고유 식별자로 매치 리스트 조회)**
- This function retrieves match information by user's ID. This function returns `json` type of results.
- 이 함수는 유저 ID를 가지고 유저의 매치 전적을 조회합니다. 이 함수는 `json` 타입으로 결과를 반환합니다.

   `>>> from PyKartRider import matchInfo`
   `>>> PyKartRider.matchInfo.get_all_matches('1728506595')`
   `..., 'matchWin': '0', 'matchTime': ''}}], 'matchType': 'effd66758144a29868663aa50e8                                                                                                                                                             5d3d95c5bc0147d7fdb9802691c2087f3416e'}], 'nickName': 'o양파극혐o'} ...`

**2. Class for a single match (한 경기를 표현하는 Class)**
- `class Match` is a class that represents a single match. For constructing a new class, you have to provide a single ` json ` format of a match.
- `class Match` 는 한개의 경기를 표현하는 class입니다. 이 class를 활용하기 위해서, Parameter 로 `json`  형태의 한개의 경기를 넣어야 합니다.
`>>> from PyKartRider import matchInfo`
`>>> matchInfo.Match(matchInfo.get_all_matches('1728506595')['matches'][0]['matches'][0])`
`===== Match ID 024400118fc05561 =====\n
Track Name : 올림포스 제우스 시티\n
Start Time : 2022-01-27T11:44:53\n
End Time : 2022-01-27T11:46:58\n
Match Rank : 99\n
Match Win : 0\n
Player Count : 8\n
Player Kart : 파이어 마라톤 V1\n
Player Flying Pet : None\n
Player Pet : None\n
Match Type : 스피드 팀전`


### Json Information (MetaData 정보)
**1. Getting 'Character' name (캐릭터 이름 조회)**
- This function retrieves 'character' name from id that is listed in `/metadata/character.json`. The metadata seems a bit outdated since it does not have some updated characters. 
- 이 함수는 `/metadata/chracter.json` 에 정의된 JSON ID에 의해서 캐릭터 이름을 조회합니다. 넥슨에서 제공한 metdata에 일부 최신 캐릭터가 포함되어있지 않습니다. 
`>>> from PyKartRider import jsonInfo`
`>>> PyKartRider.jsonInfo.get_character_info("95de437771bb1e094b4f3ef1c1a81574093a01e8d3be037c5a9fe0834dfbffa0")`
`'베이비 배찌'`

**2. Getting 'Flying Pet' name (플라잉 펫이름 조회)**
- This function retrieves 'Flying Pet' name from id that is listed in `/metadata/flyingPet.json`
- 이 함수는 `/metadata/flyingPet.json` 에 정의된 JSON ID에 의해서 플라잉펫 이름을 조회합니다.
`>>> from PyKartRider import jsonInfo`
`>>> jsonInfo.get_flying_pet_info("a87cb96d91a4e0c357c4eaeb7dbc05ef515d183e79a8aa0e674c36f917400a4b")`
`'플라잉 라이트론'`

**3. Getting 'Kart' name (카트 이름 조회)**
- This function retrieves 'Kart' name from id that is listed in `/metadata/kart.json`
- 이 함수는 `/metadata/kart.json` 에 정의된 JSON ID에 의해서 카트바디 이름을 조회합니다.
`>>> from PyKartRider import jsonInfo`
`>>> jsonInfo.get_kart_info("30711352d5c6279e96a5f449e613c5f9f04889f1c3ca6049e600d2b867821af7")`
`'그믐 산군 V1'`

**4. Getting 'Track' name (트랙 이름 조회)**
- This function retrieves 'Track' name from id that is listed in `/metadata/track.json`
- 이 함수는 `/metadata/track.json` 에 정의된 JSON ID에 의해서 트랙이름을 조회합니다.
`>>> from PyKartRider import jsonInfo`
`>>> jsonInfo.get_track_info("5873d5fe128549b597e984c87881e7d0ab632e381073164fe513e902f48a3ccd")`
`'쥐라기 공룡 결투장'`

**5. Getting 'Game Type' name (트랙 이름 조회)**
- This function retrieves 'Game Type' name from id that is listed in `/metadata/gameType.json`
- 이 함수는 `/metadata/gameType.json` 에 정의된 JSON ID에 의해서 게임 종류를 조회합니다.
`>>> from PyKartRider import jsonInfo`
`>>> jsonInfo.get_game_type_info("effd66758144a29868663aa50e85d3d95c5bc0147d7fdb9802691c2087f3416e")`
`'스피드 팀전'`

## Contacts (연락)
- The POC for this project is edina00@naver.com. Any issues regarding this project will be fixed or modified by myself. PR is welcomed as well as forks. The project is intended to be not feature rich. Thus, there might be some features that are available by official API might be missing. If you have any ideas about this project, please let me know. 

- 이 프로젝트의 POC는 edina00@naver.com 입니다. 프로젝트를 사용하면서 또는 프로젝트에 관해서 생기는 모든 문제들은 고쳐질 것입니다. PR 과 fork 또한 환영합니다. 이 프로젝트는 아직 많은 기능을 넣을 의도로 만들지 않았습니다. 공식 API 에서 제공하는 일부 기능들이 구현되지 않았을 수 있습니다. 만약 이 프로젝트에 대해서 도움이 필요하시거나 의견을 제안해주신다면, 연락 부탁드립니다. 

