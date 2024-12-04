## 👑 팀명 : 퀸🫅 & 킹🤴 그리고 잼민이들🤦‍♂️<br>

<p align="center"><img src="./img/sk.png" width="900" height="300"/></p>

### 🐿️ 팀원

|                                                        오정연                                                        |                                                        이호재                                                        |                                                        변가원                                                        |                                                        이진섭                                                        |                                                        김태욱                                                        |
| :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
| <img src="https://github.com/user-attachments/assets/d920daaf-3baa-441d-ab1c-babb240b307b" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/23848016-2562-40b7-82ad-69c0edc6c8cb" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/a2497f47-8214-43c4-81f3-ed3ee637bbf5" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/90d30dde-dfe5-4929-938f-2941dec79d65" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/60a82e31-52ef-4de3-8d52-a50037491b56" width="140" height="140"> |
|                                       [@Jungyunn](https://github.com/Jungyunn)                                       |                                           [@HoJL](https://github.com/HoJL)                                           |                                         [@dnjsrk](https://github.com/dnjsrk)                                         |                                        [@jururuj](https://github.com/jururuj)                                        |                                      [@Taeuk-Dog](https://github.com/Taeuk-Dog)                                      |
|                                              **Project Leader**<br/>LLM                                              |                                                LLM<br>Data Debugging                                                 |                                                 Frontend <br>ReadMe                                                  |                                                  Backend<br>ReadMe                                                   |                                                         AWS                                                          |

</div>

<hr>

### 🎖️ 프로젝트 개요

hallucination이 없는 챗봇 시스템 페이지 구현

<hr>

### 🎖️ 프로젝트 목표

'Enco Library Chatbot'은 'Enco Library'가 소장한 도서에 대해 검색을 했을 때 hallucination이 없는 답변을 제공하는 채팅 페이지를 보여주는 것을 목표로 합니다.

<hr>

### 🔨 기술 스택

<div>

_Environment_
<br><br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"/>
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"/>

_Development_
<br><br>
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white">
<img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
<img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white">

<hr>

### Prerequisites

**이 프로젝트를 실행하기 위해 필요한 패키지 등을 정의**

```cmd
pip install -r requirements.txt, langchain을 이용하기위한 .env파일 정의, docker env 파일
```

<hr>

### Usage

**이 코드를 실행하기 위해 어떠한 코드를 어떻게 실행해야 하는지 작성**

```cmd
python manage.py runserver
```

<hr>

### Data

국립중앙도서관 Linked Open Data(LOD)의 텍스트 기반의 일반 도서 정보 데이터셋 (이미지 클릭)
<br>
<br>
<a href='https://lod.nl.go.kr/home/dataset/datadownload.do'><img src='./img/lod.png'></a>
<br>
<br>

네이버 책 api (이미지 클릭)
<br>
<br>
<a href='https://developers.naver.com/docs/serviceapi/search/book/book.md'><img src='./img/naver.jpg'></a>
<br>
<br>
_data column_

```
"title": 제목
"author": 작가
"publisher": 출판사
"pubdate": 출판연도
"description": 책소개
```

<br>

<hr>

### Preprocess

국립중앙도서관에서 약 20,000개의 책 제목만 추출하여,
네이버 책 api를 통해 제목, 작가, 출판사, 출판연도, 책소개를 크롤링하여 데이터를 만들었습니다

<hr>

### System Architecture

<img src='./img/아키텍쳐.png'> <br>

<hr>

### 수행 결과

<hr>

### 한 줄 회고

오정연 -
<br>
이호재 -
<br>
변가원 - 최종 플젝까지 화이팅!
<br>
이진섭 - 이젠 최종 플젝만 남았구나... 풀스택 가보자고..
<br>
김태욱 - aws를 통해 프로젝트를 진행할 수 있어서 좋았다.
