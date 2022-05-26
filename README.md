# MOVIE JOY

![img](README.assets/logo.png)



## THEME

> TMBD API를 사용한 영화 정보 실시간 업데이트
>
> 유저 선호 장르와 유저 리뷰 기반의 영화 추천 사이트



## Members

![img](README.assets/role.png)



##	Plan of Features

* 3가지 영화 추천 카테고리
  * TMDB 인기 영화
  * 유저 선호 장르
  * 유저 리뷰 기반 높은 평점의 장르
* 소셜 로그인 
* 영화 관심 표시
* 유저의 관심 표시에 따라 추천받고 싶지 않은 영화 설정
* 리뷰, 평점 작성
* 현재 상영중인 영화, 개봉 예정 영화 데이터
* 음성인식
* 전화번호 인증에 따른 비밀번호 변경
* 프로필 사진 
* 나만의 포토카드 꾸미기
* black & light 모드

=> 나만의 포토카드 꾸미기, black & light 모드 외 구현 완료



## ERD

![image-20220527062759985](README.assets/image-20220527062759985.png)

> * TMDB API로 데이터를 불러온 후 
>
>   유저가 영화 카드를 클릭하면 Detail 페이지를 생성하며 
>
>   DB에 영화 정보를 저장
>
> * 별다른 update를 거치지 않아도 영화 데이터가 갱신 될 수 있음



## Features

### Login and Signup

1. Login 

![img](README.assets/login.png)

> * 카카오톡 로그인 서비스 구현

2. Signup

![img](README.assets/signup.png)

> * 유저 선호 장르 입력을 받은 후 DB에 데이터 저장



### Movie Recommend

![img](README.assets/main_recommend.png)

> * TMDB popular 추천 영화
> * 유저 선호 장르 기반 추천 영화
> * 유저 리뷰 평점 기반 추천 영화
> * 3가지 추천 알고리즘의 영화들을 각 12개씩 페이지에 출력



## Genre Category

![img](README.assets/genre_1.png)

![img](README.assets/genre_2.png)

![img](README.assets/genre_3.png)

> * 선택한 장르에 따른 12개의 영화를 랜덤으로 추천



## Release Movie

![img](README.assets/release.png)

> * 현재 상영 영화, 개봉 예정 영화들의 목록을 추천



## Search

![img](README.assets/search_1.png)

![img](README.assets/search_2.png)

> * 음성인식을 통한 검색어 입력 가능
> * 영화 title을 입력시 TMDB API를 통해 검색 결과들을 출력



## Movie Detail

1. Detail 페이지 전체 화면

![img](README.assets/detail_1.png)

![img](README.assets/detail_2.png)

> * 영화 트레일러 영상 
>
>   * TMDB API에 트레일러 정보가 없을 땐 
>
>     유튜브에서 해당 영화 제목을 검색하여 첫번째 영상을 출력
>
> * 영화 관심 정보 표시
>
>   * 아무런 관심 정보도 표시되지 않은 상태
>
>     ![img](README.assets/like_1.png)
>
>   * 관심 영화 등록
>
>     ![img](README.assets/like_2.png)
>
>   * 추천 제외 영화 등록
>
>     ![img](README.assets/like_3.png)
>
> * Review 작성
>
>   ![img](README.assets/review_1.png)
>
>   * 음성인식을 통한 리뷰 작성 가능
>   * 별점 부여 및 리뷰 수정, 삭제
>
> * 다른 사람의 Review 열람



## Under navbar

![img](README.assets/under_nav.png)

> * 페이지 스크롤을 top으로 올려주는 버튼
> * mypage 이동 router rink
> * 로그아웃 버튼
> * 유저 프로필 이미지 사진 
>   * 평소엔 이미지 사진만 뜨지만 클릭시 다른 3개의 버튼 활성화



## My Page

1. 기본 유저 프로필

![img](README.assets/profile_1.png)

![img](README.assets/profile_2.png)

> * 현재 유저 정보 표시
>   * 닉네임
>   * 선호 장르
>   * 리뷰 작성 목록, 별점 정보 => 클릭시 detail page modal 호출
> * 프로필 사진 변경



2. Like Movies

![img](README.assets/like_movie_1.png)

![img](README.assets/like_movie_2.png)

> * 지금까지 입력해둔 관심 영화 정보, 추천 제외 영화 목록을 출력
> * title 클릭시 detail page modal 호출



3. Auth

![img](README.assets/auth_1.png)

![img](README.assets/auth_2.jpeg)

> * 처음 인증하는 유저
>   1. 전화번호를 입력 후, 인증 번호를 받는다. 다른 유저로 인증된 전화번호로는 인증 번호를 받을 수 없다.
>   2. 올바른 인증 번호를 5분 이내에 제출하면 해당 유저는 인증된다.
> * 이미 인증된 유저
>   1. 전화번호 입력하지 않고 `Send`버튼을 눌러 인증 번호를 받을 수 있다.
>   2. 올바른 인증 번호를 5분 이내에 제출하면 비밀번호 변경 창이 활성화된다.
>   3. 올바른 양식의 새 비밀번호 / 비밀번호 확인을 제출하여 비밀번호를 변경할 수 있다.



4. Settings

![img](README.assets/settings.png)

> * 유저 닉네임, 선호 영화 장르 변경 가능



## 느낀점

### 이동준

> 협업할 때 주로 프론트엔드와 백엔드로 나누는 이유를 알 수 있었다. 백엔드를 담당하면서 프론트에 어떻게 데이터를 넘겨주어야 하는지 고민해보려 노력했다.
>
> 개발 중간 과정에서 모델을 수정해야 할 일이 몇 번 있었다. 그 때마다 여러 부분의 코드를 고치는 과정이 매우 힘들었다. 개발 전 왜 모델을 확실하게 정하고 가야하는 지 느꼈다.  
>
> Naver Cloud를 이용한 전화번호 인증을 굉장히 막연한 기술이라고 생각했는데, 마지막 날 구현에 성공해 몹시 뿌듯하다.



### 조혜림

> 처음에 같이 모델 짜고 조장님이 Django로 모델 구현하는 동안 시간을 아끼기 위해 템플릿을 만들었는데
>
> 그게 역할이 되어서 프로젝트 마지막까지 템플릿과 프론트를 담당했다. 근데 사실 프론트라고 하기엔 데이터 요청같은 것을 많이 다루어보지 않은 것 같아서 아쉽다 :joy:
>
> 그래도 이전 프로젝트를 진행했을 때엔 Django로만 했어서 Vue나 JS를 만질 기회가 적었는데 이번 기회에 조금은 친숙해진 것 같다는 생각이 들었다
>
> 남들보다 일찍 조를 짜고 일찍 회의를 시작해서 시간이 여유로울 것 같다고 생각했는데 역시 사람 일은 생각하는 것 처럼 쉽지 않다는 것도 느꼈다.... 마지막주는 항상 동준님과 새소리를 들으며 디스코드를 종료했다 
>
> 몸이랑 정신 둘 다 힘들었지만 그래도 완성되어가는 페이지를 보며 뿌듯함을 느꼈다 하지만 이것도 나중에 보면 엄청 부족해보이겠지? 
>
> 사실 지금도 아쉬운 점이 많지만 그래도 시간 내에서 최선을 다했다고 생각하니까 후련하게 보내주려한다..!
>
> 그래도 계속 넣고 싶었던 음성인식 기능을 마지막 날 성공해서 뿌듯하다 :smiling_imp:
>
> 항상 새벽까지 함께 공부해주신 동준님께 감사인사를 드린다 방학해도 모토코에서 만나자구여 :ghost:
