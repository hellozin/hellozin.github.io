---
title: (작성중) 쿠키, 세션 그리고 웹 스토리지
date: 2019-04-16 22:59:48
categories: 
  - Web
tags: 
  - study
---

쿠키, 세션, 웹 스토리지를 설명하기에 앞서 왜 사용하는지를 더 쉽게 이해하기 위해 HTTP 프로토콜의 특징을 알아보겠습니다.

### HTTP 프로토콜의 특징

- **비연결지향 (Connectionless)**  
  클라이언트가 서버에게 Request를 보내고 서버가 클라이언트에게 Response를 보내면 접속을 종료한다.

- **무상태 (Stateless)**  
  통신이 끝나면 상태 정보를 유지하지 않는다.

즉, 클라이언트의 로그인 정보나 브라우저에서 입력한 값 등이 페이지를 이동할 때 마다 초기화 되는 것입니다. 이러한 문제점을 해결하기 위해 데이터 저장에 사용하는 것이 `쿠키`, `세션` 그리고 `웹 스토리지`입니다.

### 쿠키

쿠키는 클라이언트 로컬에 저장되는 키와 값 형태의 작은 파일로 이름, 값, 만료 시간, 경로 정보가 들어있습니다.
쿠키는 주로 세 가지 목적을 위해 사용됩니다.  
- **세션 관리**: 서버에 저장해야 할 로그인, 장바구니, 게임 스코어 등의 정보 관리
- **사용자 맞춤**: 사용자가 선호하는 옵션이나 테마 등의 세팅
- **사용자 추적**: 사용자의 행동을 기록하고 분석하는 용도 

`Response Header`의 `Set-Cookie` 속성을 사용하면 클라이언트에 쿠키를 만들 수 있으며 만들어진 쿠키는 클라이언트가 따로 설정하지 않아도 브라우저가 `Request Header`에 넣어서 서버로 전송하게 됩니다.

서버의 HTTP 응답 헤더에서 쿠키를 설정합니다.

```
HTTP/1.0 200 OK
Content-type: text/html
Set-Cookie: name=hellozin
Set-Cookie: job=developer
```

이후 클라이언트에서 보내는 모든 요청에 브라우저는 `Cookie` 헤더를 통해 저장된 모든 쿠키를 전송합니다.

```
GET /sample_page.html HTTP/1.1
Host: www.example.org
Cookie: name=hellozin; job=developer
```

이렇게 만들어진 쿠키는 스코프에 의해 크게 두가지로 나눌 수 있습니다.

- 클라이언트가 종료되면 삭제되는 휘발성 쿠키인 `Session Cookie`
- 클라이언트가 종료되어도 일정 기간 유지되는 `Permanent Cookie`

`Expires(날짜와 시간)` 혹은 `Max-Age(초)` 를 명시해 해당 날짜, 혹은 시간까지 쿠키를 유지할 수 있고 아무것도 명시하지 않을 경우 `Session Cookie` 가 됩니다.

```
Set-Cookie: name=hellozin; Expires=Wed, 21 Oct 2019 07:28:00 GMT;
```
> 명시된 만료일, 시간은 서버가 아닌 클라이언트를 기준으로 계산됩니다.

`Domain` 과 `Path` 속성은 쿠키의 스코프를 정의합니다.  
`Domain` 속성이 명시되면 해당 쿠키는 서브 도메인에도 포함되고 명시되지 않을 경우 현재 문서 위치의 호스트 일부를 기본값으로 합니다.

`Domain=naver.com` 의 쿠키가 포함되는 서브도메인의 예
- `news.naver.com`
- `m.naver.com`

`Path` 속성이 명시되면 해당 쿠키는 명시된 path가 포함된 서브 디렉토리에 포함됩니다.

`Path=/docs` 의 쿠키가 포함되는 서브디렉토리의 예
- `/docs`
- `/docs/Web/`
- `/docs/Web/HTTP`



### Reference

- [HTTP 쿠키 / MDN](https://developer.mozilla.org/ko/docs/Web/HTTP/Cookies)
- [쿠키 옵션 - path & domain / 생활코딩](https://opentutorials.org/course/3387/21745)