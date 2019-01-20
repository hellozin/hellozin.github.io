---
title: Python으로 간단한 Jekyll 포스트 설정하기
date: 2019-01-20 17:25:26
categories: 
 - Script
tags: 
---

## Github Blog (Jekyll) 포스트 생성 스크립트

**Github Blog**에 글을 쓰기 위해서는 우선 `_posts/` 폴더에 **마크다운 파일**을 생성해야 한다. 동시에 파일명이나 파일 내부의 기본 구성요소 등 일정한 기준에 맞추어 작성해야 올바르게 적용되는데 **파이썬 스크립트**를 통해 이를 조금 더 간단하게 처리해보고 싶었다.

## 스크립트 적용 사항

스크립트를 적용시키려는 항목은 아래와 같으며 **Jekyll Theme**에 따라 항목이 달라질 수 있다.

- 파일명 앞에는 `YYYY-MM-DD`형식의 날짜 정보가 있어야 한다.
- 파일명의 공백은 `'-'` 문자로 대체한다.
- 모든 파일의 최상단에 title, date, categories, tags 정보를 입력한다.

```python
파일명 형식 : YYYY-MM-DD-File-Name.md

포스트 정보
---
title: 여기에 포스트 제목을 작성합니다.
date: YYYY-MM-DD HH:MM:SS (MD 파일을 만든 시간)
categories:
 - 여기에 카테고리명을 입력합니다.
tags:
 - 여기에 태그명을 입력합니다. (선택)
---
```

## 스크립트 작성

처리할 내용도 간단하고 성능에 크게 민감한 부분이 아니기 때문에 스크립트는 단순하게 작성하였고 [전체코드](#전체-코드)는 아래에서 확인할 수 있다.

먼저 스크립트를 실행하면 생성될 마크다운 파일의 파일명을 입력받는다. 이 파일명은 새 포스트의 제목이 아니라 블로그 저장소 내 `_posts` 폴더에 저장될 파일명을 의미하며 뒤에 설명할 날짜정보와 함께 `YYYY-MM-DD-File-Name.md` 형식으로 저장된다.

```py
import datetime

print("파일 이름을 입력하세요. (입력하지 않으면 'YYYY-MM-DD-Undefined.md'로 지정됩니다.)")
fileName = input("파일명 : ")
```

만약 파일명을 입력하지 않고 `Enter` 를 입력하면 파일명을 `"Undefined"`로 저장한다.

```py
if len(fileName) is 0:
    fileName = "Undefined"
```

 파일명에 존재하는 `공백(space)`은 `'-'` 로 대체된다.

```python
fileName = fileName.replace(" ", "-")
```

다음으로 `_posts` 폴더에 날짜정보를 추가한 파일명으로 `_posts` 폴더에 마크다운 파일을 생성한다.  
**이미 존재하는 파일에 대한 중복 접근은 아직 처리되지 않았다.**

```python
now = datetime.datetime.now()
fullFileName = now.strftime("%Y-%m-%d-"+fileName+".md")

newFile = open("./_posts/"+fullFileName, "w+")
```

> 스크립트 파일 위치 : `hellozin.github.io/make.py`  
> 생성될 MD 파일 위치 : `hellozin.github.io/_posts/새로운MD파일`

마지막으로 파일 최상단에 포스트 정보를 `write` 하고 `open` 된 `파일 객체` 를 `close` 해준다.  
`date` 정보는 앞서 사용한 날짜 정보를 이용해 작성한다.

```python
newFile.write("---\n")
newFile.write("title: \n")
newFile.write("date: "+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
newFile.write("categories: \n")
newFile.write("tags: \n")
newFile.write("---\n")
newFile.write("\nWrite Here!\n")

newFile.close()
```

## 전체 코드

```python
import datetime

print("파일 이름을 입력하세요. (입력하지 않으면 'YYYY-MM-DD-Undefined.md'로 지정됩니다.)")
fileName = input("파일명 : ")

if len(fileName) is 0:
    fileName = "Undefined"

fileName = fileName.replace(" ", "-")

now = datetime.datetime.now()
fullFileName = now.strftime("%Y-%m-%d-"+fileName+".md")

newFile = open("./_posts/"+fullFileName, "w+")

newFile.write("---\n")
newFile.write("title: \n")
newFile.write("date: "+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
newFile.write("categories: \n")
newFile.write("tags: \n")
newFile.write("---\n")
newFile.write("\nWrite Here!\n")

newFile.close()
```