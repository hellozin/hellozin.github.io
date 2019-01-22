---
title: JavaScript 공부 중 궁금한 내용들
date: 2019-01-22 23:56:05
categories: 
 - Study
tags:
---

## JavaScript

JavaScript를 이제 막 공부하기 시작한 취준생이 공부하며 궁금한 내용들을 정리하는 포스트입니다. **내용이 정확하지 않을 수 있으며** 틀린 내용에 대한 지적은 굉장히 감사합니다.

<!-- more -->

## 목록

- [Node 객체와 Element 객체의 차이점](#Node-객체와-Element-객체의-차이점)

### Node 객체와 Element 객체의 차이점

**DOM (Document Object Model)** 에 대해 공부하던 도중 **nodeName** 이라는 프로퍼티를 사용하다가 생각과는 다른 결과를 발견했다.

```html
HTML
...
<p id="hello">단락입니다.</p>
...
```

```javascript
JavaScript
var node = document.getElementById("hello");
console.log(node.nodeName);
```

`<P>` 태그인 객체를 가져와 `nodeName` 프로퍼티를 사용했으니 `P` 라는 문자열이 출력될 것이라고 생각했지만

실행결과  
`Uncaught TypeError: Cannot read property 'nodeName' of null at main.js:2`

`TypeError` 와 함께 아무런 결과도 출력되지 않았다.

