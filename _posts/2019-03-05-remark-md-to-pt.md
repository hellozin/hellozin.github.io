---
title: (작성중) Remark | 마크다운으로 PT 만들기
date: 2019-03-05 05:55:09
categories: 
 - Tools
tags: 
 - markdown
 - presentation
 - tools
---

스터디나 모임에서 간단하게 발표할 일이 있으면 보통 마크다운으로 정리한 문서를 보면서 진행을 했는데 아무래도 PT형식이 가독성에 도움이 될 것 같아 찾아보던 중 마크다운 포맷으로 PT를 만드는 툴을 발견했다.

<!-- more -->

# Remark

> 깃허브 링크 : [https://github.com/gnab/remark](https://github.com/gnab/remark)  
> 샘플 : [https://remarkjs.com/#1](https://remarkjs.com/#1)

쉬운 이해를 위해 간단한 예제 코드를 보자.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Title</title>
    <meta charset="utf-8">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
      @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
      @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);

      body { font-family: 'Droid Serif'; }
      h1, h2, h3 {
        font-family: 'Yanone Kaffeesatz';
        font-weight: normal;
      }
      .remark-code, .remark-inline-code { font-family: 'Ubuntu Mono'; }
    </style>
  </head>
  <body>
    <textarea id="source">

    # 슬라이드 제목1  
    첫번째 슬라이드입니다.  
    ---
    # 슬라이드 제목2
    두번째 슬라이드입니다.

    </textarea>
    <script src="https://remarkjs.com/downloads/remark-latest.min.js">
    </script>
    <script>
      var slideshow = remark.create();
    </script>
  </body>
</html>
```

첫 예제 치고는 긴 편이지만 우선 이부분만 주목하면 된다.

```html
<textarea id="source">

  # Slide 1  
  첫번째 슬라이드입니다.  
  This is first slide.
  ---
  # Slide 2
  두번째 슬라이드입니다.
  This is second slide.

</textarea>
```

`<textarea id="source">` 태그 안에 `Remark` 형식에 맞는 마크다운을 작성하고 html을 실행해 보면 다음과 같은 PT를 간단하게 얻을 수 있다.

<img width="80%" src="https://s3.ap-northeast-2.amazonaws.com/img.blog.post/0306-simple-slide-1.PNG">
<img width="80%" src="https://s3.ap-northeast-2.amazonaws.com/img.blog.post/0306-simple-slide-2.PNG">

당연히 마크다운의 헤더, 목록, 코드블럭 등을 사용할 수 있고 약간의 CSS만 사용하면 레이아웃도 나눌 수 있다.(Remark에서 공식적으로 지원하는 방법이 있는지는 아직 확인하지 못했다. 레이아웃을 나누는 방법은 다른 글에서 설명한다.)

## 기본적인 사용법

그럼 다시 간단한 사용법을 알아보자

### 1. 슬라이드 나누기

슬라이드는 `---` 을 기준으로 나누어 진다. `<hr />`이 아님에 유의하자.

```markdown
# Slide 1
첫번째 슬라이드

---

# Slide 2
두번째 슬라이드
```

### 2. 정렬

`class` 프로퍼티를 사용해 해당 슬라이드의 정렬 방법을 지정할 수 있다. 기본적으로 제공하는 클래스는 `left`, `center`, `right`, `top`, `middle`, `bottom` 이 있다.

```markdown
class: center

# Aligned Slide
이 슬라이드는 수평으로 중앙 정렬됩니다.

---
class: center, middle

# Aligned Slide
이 슬라이드는 수직, 수평으로 중앙 정렬됩니다.
```

### 3. 