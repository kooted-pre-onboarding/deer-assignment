

![디어코퍼레이션](https://user-images.githubusercontent.com/89339349/142787849-0aeba5e4-99c6-4bc3-ae66-f03ca9bc8a3d.png)
<br/>
<br/>

# 원티드x위코드 백엔드 프리온보딩 과제 6.

> ## [Assignment] 과제 제출 기업정보



- 기업명 : 디어코퍼레이션
- [디어코퍼레이션 웹사이트 링크](https://web.deering.co/)
- [디어코퍼레이션 채용공고 링크](https://www.wanted.co.kr/wd/59051)

<br/>



> ## Members



| 이름       | Github                                          | 담당 기능                                                    |
| ---------- | ----------------------------------------------- | ------------------------------------------------------------ |
| 👨🏻‍🎤 김주현 | [kjhabc2002](https://github.com/kjhabc2002)     | DB data control,  AWS (EC2/RDS) 배포                         |
| 👨🏻‍🦳 양가현 | [chrisyang256](https://github.com/chrisyang256) | 조건에 따른 벌금 API view, unit test, postman api            |
| 👶🏻 구본욱  | [qhsdnr0](https://github.com/qhsdnr0)           | 주차 및 금지구역 API view, unit test, postman api, README 작성 |
| 👰🏻‍♂️ 이다빈 | [thisisempty](https://github.com/thisisempty)   | 새로운 할인/벌금 조건 확장성 설계,  postman api, AWS (EC2/RDS) 배포 |
| 🦹🏻‍♂️ 문승준 | [palza4dev](https://github.com/palza4dev)       | Member API 및 확장성 설계 , unit test,  postman api, README 작성 |
| 🥷 김지훈   | [kimfa123](https://github.com/kimfa123)         | 조건에 따른 벌금 API view, unit test,  postman api, README 작성 |

ㅤ👪 공동작업: DB Modeling

<br/><br/>



> ## 사용 기술
>
> <br/>

[![Python](https://camo.githubusercontent.com/a1b2dac5667822ee0d98ae6d799da61987fd1658dfeb4d2ca6e3c99b1535ebd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)](https://camo.githubusercontent.com/a1b2dac5667822ee0d98ae6d799da61987fd1658dfeb4d2ca6e3c99b1535ebd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)ㅤ[![Django](https://camo.githubusercontent.com/5473e0d3006bb7e662bdf754d830a026ce050be61f1cbbd4689783ae49950b93/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/5473e0d3006bb7e662bdf754d830a026ce050be61f1cbbd4689783ae49950b93/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465)ㅤ[![SQLite](https://camo.githubusercontent.com/b310667470594171440f9b80f624787ea58555296d88af177788509b0d73a40b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/b310667470594171440f9b80f624787ea58555296d88af177788509b0d73a40b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465)ㅤ[![AWS](https://camo.githubusercontent.com/9281daa5684971fd3325661e3dd5fea86b21a902e3741a556fb636fbf0e2f3d4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d2532334646393930302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d617773266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9281daa5684971fd3325661e3dd5fea86b21a902e3741a556fb636fbf0e2f3d4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d2532334646393930302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d617773266c6f676f436f6c6f723d7768697465)ㅤㅤ[![Postman](https://camo.githubusercontent.com/3f0e26b0951bab845a1bb9a7198ecca0da272e462921b6edd85879f3673b6927/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d706f73746d616e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/3f0e26b0951bab845a1bb9a7198ecca0da272e462921b6edd85879f3673b6927/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d706f73746d616e266c6f676f436f6c6f723d7768697465)ㅤ[![GitHub](https://camo.githubusercontent.com/f6d50128cb007f85916b7a899da5d94f654dce35a37331c8d28573aef46f4274/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333132313031312e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/f6d50128cb007f85916b7a899da5d94f654dce35a37331c8d28573aef46f4274/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333132313031312e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)



<br/>

> <aside> 📝 아래의 상황을 읽고 요구사항을 구현해주세요!
>
>
> </aside>
>
> ### **[필수 포함 사항]**
>
> - READ.ME
>
>   작성
>
>   - 프로젝트 빌드, 자세한 실행 방법 명시
>   - 구현 방법과 이유에 대한 간략한 설명
>   - 완료된 시스템이 배포된 서버의 주소
>   - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
>
> - Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
>
> ### 주요 평가 사항
>
> - 주어진 정보를 기술적으로 설계하고 구현할 수 있는 역량
> - 확장성을 고려한 시스템 설계 및 구현
>
> ### 과제 안내
>
> 디어는 사용자의 요금을 계산하기 위해 다양한 상황을 고려합니다.
>
> - 우선 지역별로 다양한 요금제를 적용하고 있습니다. 예를 들어 건대에서 이용하는 유저는 기본요금 790원에 분당요금 150원, 여수에서 이용하는 유저는 기본요금 300원에 분당요금 70원으로 적용됩니다.
> - 할인 조건도 있습니다. 사용자가 파킹존에서 반납하는 경우 요금의 30%를 할인해주며, 사용자가 마지막 이용으로부터 30분 이내에 다시 이용하면 기본요금을 면제해줍니다.
> - 벌금 조건도 있습니다. 사용자가 지역 바깥에 반납한 경우 얼마나 멀리 떨어져있는지 거리에 비례하는 벌금을 부과하며, 반납 금지로 지정된 구역에 반납하면 6,000원의 벌금을 요금에 추과로 부과합니다.
> - 예외도 있는데, 킥보드가 고장나서 정상적인 이용을 못하는 경우의 유저들을 배려하여 1분 이내의 이용에는 요금을 청구하지 않고 있습니다.
>
> 최근에 다양한 할인과 벌금을 사용하여 지자체와 협력하는 경우가 점점 많아지고 있어 요금제에 새로운 할인/벌금 조건을 추가하는 일을 쉽게 만드려고 합니다. 어떻게 하면 앞으로 발생할 수 있는 다양한 할인과 벌금 조건을 기존의 요금제에 쉽게 추가할 수 있는 소프트웨어를 만들 수 있을까요?
>
> 우선은 사용자의 이용에 관한 정보를 알려주면 현재의 요금 정책에 따라 요금을 계산해주는 API를 만들어주세요. 그 다음은, 기능을 유지한 채로 새로운 할인이나 벌금 조건이 쉽게 추가될 수 있게 코드를 개선하여 최종 코드를 만들어주세요.
>
> **다음과 같은 정보들이 도움이 될 것 같아요.**
>
> ------
>
> - 요금제가 사용자 입장에서 합리적이고 이해가 쉬운 요금제라면 좋을 것 같아요.
> - 앞으로도 할인과 벌금 조건은 새로운 조건이 굉장히 많이 추가되거나 변경될 것 같아요.
> - 가장 최근의 할인/벌금 조건의 변경은 '특정 킥보드는 파킹존에 반납하면 무조건 무료' 였습니다.
>
> **이용에는 다음과 같은 정보들이 있습니다.**
>
> ------
>
> ```
> use_deer_name (사용자가 이용한 킥보드의 이름)
> use_end_lat, use_end_lng (사용자가 이용을 종료할 때 위도 경도)
> use_start_at, use_end_at (사용자가 이용을 시작하고 종료한 시간)
> ```
>
> **데이터베이스에는 킥보드에 대해 다음과 같은 정보들이 있습니다.**
>
> ------
>
> ```
> deer_name (킥보드의 이름으로 고유한 값)
> deer_area_id (킥보드가 현재 위치한 지역의 아이디)
> ```
>
> **데이터베이스에는 지역에 대해 다음과 같은 정보들이 있습니다.**
>
> ------
>
> ```
> area_id (지역 아이디로 고유한 값)
> area_bounday (지역을 표시하는 MySQL spatial data로 POLYGON)
> area_center (지역의 중심점)
> area_coords (지역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
> ```
>
> **데이터베이스에는 파킹존에 대해 다음과 같은 정보들이 있습니다.**
>
> ------
>
> ```
> parkingzone_id (파킹존 아이디로 고유한 값)
> parkingzone_center_lat, parkingzone_center_lng (파킹존 중심 위도, 경도)
> parkingzone_radius (파킹존의 반지름)
> ```
>
> **데이터베이스에는 반납금지구역에 대해 다음과 같은 정보들이 있습니다.**
>
> ------
>
> ```
> forbidden_area_id (반납금지구역 아이디로 고유한 값)
> forbidden_area_boundary (반납금지구역을 표시하는 MySQL spatial data로 POLYGON)
> forbidden_area_coords (반납금지구역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
> ```
>
> <br/>
> <br/>

> ## 모델링

<br/>

![스크린샷 2021-11-22 오후 2 39 47](https://user-images.githubusercontent.com/72376931/142807745-06969b55-19e5-4660-8654-a3b628572056.png)

<br/>

> ## 구현 기능 

<br/>

### ▶︎ Member 생성 및 정보  조회

- 유저 회원가입을 위한 SignUpView class 작성 (bcrypt로 비밀번호 암호화)
- 유저 로그인을 위한 SignInView class 작성 (JWT 토큰 생성)
- 유저 인가를 위한 login_decorator를 utils.py 작성

<br/>

### ▶︎ Parking zone 및 forbidden zone 설정

- Parking_zone은 중심점과 반지름 속성을 가지며 이 속성들로 만든 원형 범위를 가지고 있습니다.
- Forbidden_zone은 여러 점을 잇는 다각형형태로 지정되어 있습니다.
  ![image](https://user-images.githubusercontent.com/89339349/142794449-f6aa4a6d-37d6-4f66-b359-5ac7d70e1c46.png)

<br/>

### ▶︎ 요금 할인 조건 및 벌금 조건 설정

- 할인 : Parking_zone에 주차 시 요금의 30% 할인, 마지막 이용시간으로부터 30분 이내에 재사용 시 기본요금 면제 조건이 적용되어 있습니다.
- 벌금 : Forbidden_zone에 주차 시 6000원의 추가요금, 운행 시작지역을 벗어난 경우 도착지점과 해당 지역과의 거리에따른 추가요금이 부과됩니다.

```python
if use_time <= datetime.timedelta(seconds=60):
    return JsonResponse({'message' : 'CREATED', 'cost' : 0}, status = 201)
            
total_fee = rate_plan.basic + (use_time.seconds // 60) * rate_plan.per_minute
use_list = Use.objects.filter(member=member, end_at__gte=convert_time(use.start_at) -			datetime.timedelta(seconds=1800))
            
if use_list.exclude(id=use.id).exists():
    total_fee = (use_time.seconds // 60) * rate_plan.per_minute
            
adjusted_fee = add_fee(deer, member, discount_fee(deer, member, total_fee))
```

<br/>

### ▶︎ 다양한 할인과 벌금 조건을 추가 할수 있는 확장성

- 할인과 벌금요건들을 utils에 각각 함수형태로 저장하여 할인, 벌금이 추가될 때마다 각 함수 내부에 조건들을 추가할 수 있도록 설계했습니다.
- 할인, 벌금에 필요한 대부분의 요소들은 deer, member를 통해서 가져올 수 있는 값들로 판단하여 추가적인 parameter를 넣지 않았고 할인, 벌금 조건이 추가될 때마다 조건문을 통해 지정된 요금에 할인, 벌금이 추가된 최종 요금을 확인할 수 있도록 구성했습니다.

```python
if parking_circle.contains(arrive_point):
	return total_fee * 0.7
       
if forbidden_area.boundary.contains(arrive_point):
    surcharge += 6000
```

<br/>

### ▶︎ 설치 및 설정 방법 

1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동한다.

```
https://github.com/kooted-pre-onboarding/deer-assignment.git
cd deer-assignment
```

2. 가상 환경을 생성하고 프로젝트에 사용한 python package를 설치한다

```
conda create -n "deer" python=3.8
conda activate deer
```

3. gdal을 설치 한다. 

   3-1 Mac 일 경우

```
brew install gdal
```

​	3-2 ubutu 일경우

```
$ sudo apt-get install binutils libproj-dev gdal-bin
```

4. 환경변수 설정

```
DEER_SECRET_KEY=‘해당 키’
DEER_DB_NAME=‘해당 네임’
DEER_DB_USER=‘해당 유저’
DEER_DB_PASSWORD=‘해당 비밀번호’
DEER_DB_HOST=‘해당 주소’
DEER_DB_PORT=3306
DEER_DB_GDAL='해당모듈'
```

<br/>
<br/>

> ## API Document & Test 


1. [Postman API 문서 링크](https://documenter.getpostman.com/view/18218753/UVJWr1CU#c54fbfa6-dffc-472b-9787-7639cf00a881)로 접속해 우측 상단의 `Run in Postman` 버튼을 클릭합니다.
2. 개인 Workspace로 Import 합니다.
3. hostname 환경변수를 deploy로 선택합니다.
4. 배포 주소 `13.125.45.93:8000` 를 확인합니다. 
5. API 문서 예시를 참고해 Request를 보냅니다.


<br/>
<br/>


> ## 폴더 구조 



```
.
├── Dockerfile
├── areas
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── deer
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── manage.py
├── members
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── pull_request_template.md
├── requirements.txt
├── use
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── utils.py
```


<br/>


# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 디어코퍼레이션에서 출제한 과제를 기반으로 만들었습니다.
