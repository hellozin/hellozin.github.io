---
layout: post
date: 2018-12-15 02:47
title:  "Jeklly 관련 에러"
permalink: "/error/"
mood: angry
category: 
- information
---

### 링크 에러

`[구글 링크](www.google.com)`

[구글 링크](www.google.com) 

다음과 같이 일반 링크를 생성했을 때에는 정상적으로 동작하지만

`##### [구글 링크](www.google.com) `

###### [구글 링크](www.google.com) 

헤더와 같이 다른 속성과 함께 사용하면 마우스 hover 이벤트 후 사라지는 현상 발생, 그 중 내부 헤더로 링크하기 위해 다음과 같이 해결


`### [헤더 1](#header1)`  
`### <a name="header1"></a> 헤더 1`