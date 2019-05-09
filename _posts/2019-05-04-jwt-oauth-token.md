---
title: JWT | Json Web Token
date: 2019-05-04 20:29:49
categories: 
  - WEB
tags: 
---

최근 세션 대신 사용자 인증에 주로 사용되는 JWT와 OAuth. 그 중 JWT에 대해 아주 기본적인 내용까지만 알아보도록 하겠습니다.

<!-- more -->

혹시 틀린 내용이 있다면 지적 부탁드립니다.

### JWT 란?

Json Web Token의 줄임말로 JWT 라이브러리인 [JJWT의 Docs](https://java.jsonwebtoken.io/jjwtdocs.html)에서는 다음과 같이 정의하고 있습니다.

> JWT is a means of transmitting information between two parties in a compact, verifiable form.  
> JWT는 두 지점 사이에 정보를 전달할 수 있는 컴팩트하고 검증 가능한 수단입니다. 

간단히 설명하자면 
- JSON 형식의 본문(body)을 가지며 
- 두 지점 사이에 정보를 전달하는데 사용되고
- 컴팩트(?)하고 검증이 가능하다.

라고 정리할 수 있겠습니다.

JWT는 claim방식의 토큰을 사용하는데 claim이란 사용자에 대한 속성 등을 의미합니다.   
JWT는 JSON을 사용하여 claim을 정의하며 아래와 같이 나타낼 수 있습니다.

```json
{
  "name": "hellozin",
  "job": "developer"
}
```
그런데 JSON은 "\n" 등 개행문자를 포함하고 있기 때문에 HTTP Header 등에 넣기가 불편합니다. 그래서 JWT는 Base64 기반으로 인코딩해 하나의 문자열로 변환해서 사용합니다.

Base64로 인코딩 된 JSON:  
`ewogICJpZCI6ICJoZWxsb3ppbiIsCiAgImpvYiI6ICJkZXZlbG9wZXIiCn0=`

> 개행문자가 불편한 이유로는 CR, LF의 구분과 HTTP 응답 분할 취약점 등이 있는것 같지만 확실하지 않아 좀 더 공부한 뒤에 추가하도록 하겠습니다.

그럼 여기서 문제가 하나 생깁니다. 이렇게 토큰 자체가 정보를 담고 있기 때문에 토큰을 탈취해 변조가 가능해진다는 점입니다. 그래서 JWT는 토큰에 서명(Signature)을 적용해 이를 방지합니다.

### JWT 서명

토큰의 변조를 방지(무결성)하기 위해 HMAC(Hash-based Message Authentication)라는 방법을 사용하는데 원래의 메시지의 Hash값을 추출해 비밀키로 복호화한 뒤 토큰의 뒤에 붙여줍니다. 이를 통해 메시지가 변경되었는지 HMAC값을 통해 알 수 있고 새로 HMAC값을 만드려고 해도 비밀키를 알 수 없기 때문에 변조가 어려워집니다.

```
HMAC값 = hash(원본메시지)
메시지 = {원본메시지}.{HMAC값}
```

위의 JSON 메시지를 SHA256 알고리즘과 비밀키 "hello"를 사용해 HMAC값을 생성하면 아래의 문자열이 생성됩니다.

알고리즘: SHA256, 비밀키: "hello"
`4C136E93C7720EE7C20F8375A487101D1142112DAF7A7A48960A5991220D8B11`

서명에는 SHA256 뿐만 아니라 SHA384, SHA512, RS256 등 다양한 알고리즘이 사용될 수 있기 때문에 토큰의 앞부분에는 어떤 알고리즘이 사용되었는지 JSON 형태로 정의한 후 base64 방식으로 인코딩한 문자열을 붙여줍니다.

```json
{
  "alg": "SHA256",
  "typ": "JWT"
}

// json to base64
ewogICJhbGciOiAiU0hBMjU2IiwKICAidHlwIjogIkpXVCIKfQ==
```

### JWT 생성 과정

전체 과정을 간단하게 다시 확인해보겠습니다.

1.JSON 형식으로 claim 정의합니다.

```json
{
  "name": "hellozin",
  "job": "developer"
}
```

2.JSON으로 정의된 claim을 base64 방식으로 인코딩합니다.
   
```
ewogICJpZCI6ICJoZWxsb3ppbiIsCiAgImpvYiI6ICJkZXZlbG9wZXIiCn0=
```

3.JSON으로 정의된 claim으로 HMAC값을 생성합니다. 

```
// 알고리즘="SHA256", 비밀키="hello"
4C136E93C7720EE7C20F8375A487101D1142112DAF7A7A48960A5991220D8B11
```

4.사용된 알고리즘 정보를 JSON으로 정의한 뒤 base64 방식으로 인코딩합니다.

```json
// 알고리즘 정보
{
  "alg": "SHA256",
  "typ": "JWT"
}
// base64 방식으로 인코딩
ewogICJhbGciOiAiU0hBMjU2IiwKICAidHlwIjogIkpXVCIKfQ==
```

5.생성된 정보들로 토큰을 생성합니다.

```
{알고리즘정보}.{메시지}.{HMAC}

ewogICJhbGciOiAiU0hBMjU2IiwKICAidHlwIjogIkpXVCIKfQ==.ewogICJpZCI6ICJoZWxsb3ppbiIsCiAgImpvYiI6ICJkZXZlbG9wZXIiCn0=.4C136E93C7720EE7C20F8375A487101D1142112DAF7A7A48960A5991220D8B11
```

### JJWT Quick Stater

다음은 JJWT 라이브러리를 통해 JWT를 생성하는 코드를 살펴보겠습니다. 아래의 코드는 JJWT Docs페이지의 Quick Start 코드를 가져온 것입니다.

의존성 추가
```java
dependencies {
    compile 'io.jsonwebtoken:jjwt:0.7.0'
}
```

#### JWS(Signed JWT) 생성

1. Jwts.builder() 메서드로 JwtBuilder 인스턴스를 생성합니다.
2. JwtBuilder의 메서드로 header 매개변수와 claims를 정의합니다.
3. JWT를 서명하고 싶다면 비밀키나 공유키를 지정합니다.
4. compact() 메서드로 JWS를 생성합니다.

```java
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import java.security.Key;
import org.junit.Test;

// We need a signing key, so we'll create one just for this example. Usually
// the key would be read from your application configuration instead.
Key key = Keys.secretKeyFor(SignatureAlgorithm.HS256);

String jws = Jwts.builder()     // (1)
            .setSubject("Joe")  // (2)
            .signWith(key)      // (3)
            .compact();         // (4)
```

JWT 토큰을 생성하며 "sub" 속성에 "Joe" 라는 값을 넣고 HS256 알고리즘을 사용해 서명하는 코드입니다. 이를 확인하기 위해 JWT를 출력해보겠습니다.

```java
System.out.println("Signed JWT:");
System.out.println(jws);

Signed JWT:
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKb2UifQ.qre7ZfknCkwabjzRWpVgv6Sz93cNPEO2dJF1AqZjnjE
```

앞서 살펴본것과 같이 {알고리즘정보}.{메시지}.{HMAC} 세가지 정보로 이루어진 문자열을 확인할 수 있습니다.

토큰의 내용은 서명에 사용된 key와 parse함수를 사용해 확인할 수 있습니다.

```java
System.out.println("JWT parseClaimsJws:");
System.out.println(Jwts.parser().setSigningKey(key).parseClaimsJws(jws));

JWT parseClaimsJws:
header={alg=HS256},body={sub=Joe},signature=qre7ZfknCkwabjzRWpVgv6Sz93cNPEO2dJF1AqZjnjE
```

getHeader(), getBody(), getSignature() 함수를 사용해 각각의 정보를 가져올 수 있고 JWT를 생성할 때의 정보와 일치한다는 것을 확인할 수 있습니다.

지금까지 JWT의 생성과정과 간단한 구현에 대해 알아보았습니다. 다음포스트에서는 Custom Claim의 구현과 Spring Web Mvc에서의 사용방법에 대해 알아보도록 하겠습니다.

### Reference

- [Java JWT - JJWT Docs](https://java.jsonwebtoken.io/jjwtdocs.html)
- [REST JWT(JSON Web Token)소개 - 조대협의 블로그](https://bcho.tistory.com/999)
