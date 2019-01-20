---
title: Python으로 간단한 Jekyll 포스트 설정하기
date: 2019-01-20 17:25:26
categories: 
 - Script
tags: 
---

### Github Blog (Jekyll) 포스트 생성 스크립트

Github Blog에 글을 쓰려고 하면 마크다운 파일을 생성해야 하는데 파일 생성과 더불어 몇가지 귀찮은 설정들을 조금이나마 쉽게 처리할 수 있도록 파이썬 스크립트를 사용해 보았다.

<br/>

#### 스크립트 적용 사항

모든 Jekyll 블로그 제약이 같은지는 모르겠지만 스크립트에 적용한 제약은 다음과 같다.

**파일명**

`YYYY-MM-DD-File-Name.md`

- 파일명 앞에는 YYYY-MM-DD형식의 날짜 정보가 있어야 한다.
- 파일명의 공백은 '-' 문자로 대체한다.

**포스트 정보**

```python
---
title: 여기에 포스트 제목을 작성합니다.
date: YYYY-MM-DD HH:MM:SS
categories:
 - 여기에 카테고리명을 입력합니다.
tags:
 - 여기에 태그명을 입력합니다. (선택)
---
```

- 모든 파일의 최상단에 위와 같은 내용이 포함되어야 한다.

<br/>

#### 스크립트 작성

제약조건도 간단하고 성능에 크게 민감한 부분이 아니기 때문에 스크립트는 최대한 단순하게 작성하였다.<br>
[전체코드](#전체-코드)는 아래에서 볼 수 있다.



먼저 생성될 마크다운 파일의 파일명을 입력받는다. 이 파일명은 새 포스트의 제목이 아니라 블로그 저장소 내 `_posts_`에 저장될 파일명을 의마하며 뒤에 설명할 날짜정보와 함께 `YYYY-MM-DD-File-Name.md` 형식으로 저장된다.

만약 파일명을 입력하지 않고 `Enter` 를 입력하면 파일명이 `"Undefined"`로 지정되며 파일명에 존재하는 `공백(space)`은 `'-'` 로 대체된다.

```python
import datetime

print("파일 이름을 입력하세요. (입력하지 않으면 'YYYY-MM-DD-Undefined.md'로 지정됩니다.)")
fileName = input("파일명 : ")

if len(fileName) is 0:
    fileName = "Undefined"

fileName = fileName.replace(" ", "-")
```

<br>

다음으로 파일명과 포스트 정보에 사용될 날짜 및 시간정보를 가져와 가공하고 파일이름 앞에 날짜정보를 추가한 뒤 완성된 파일명으로 _posts 폴더에 마크다운 파일을 생성한다.

**아직 파일명 중복이나 생성된 파일을 잘못 수정하는 부분은 처리하지 않았다.**

```python
now = datetime.datetime.now()
fullFileName = now.strftime("%Y-%m-%d-"+fileName+".md")

newFile = open("./_posts/"+fullFileName, "w+")
```

<br>

마지막으로 파일 최상단에 포스트 정보를 `write` 하고 `open` 된 `파일 객체` 를 `close` 해준다. `date` 정보는 앞서 사용한 날짜 정보를 이용해 작성한다.

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

<br>

#### 전체 코드

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