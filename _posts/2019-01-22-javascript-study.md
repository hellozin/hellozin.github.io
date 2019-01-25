---
title: JavaScript 공부 중 궁금한 내용들
date: 2019-01-22 23:56:05
categories: 
 - study/javascript
tags:
 - web
 - study
 - javascript
 - error
---

## JavaScript

JavaScript를 이제 막 공부하기 시작한 취준생이 공부하며 궁금한 내용들을 정리하는 포스트입니다. **내용이 정확하지 않을 수 있으며** 틀린 내용에 대한 지적은 굉장히 감사합니다.

<!-- more -->

## 목록

- [Node Clone 시 Text Node 없는 경우](#node-clone)
- [Nodes of type '#document' may not be inserted inside nodes of type 'DIV'](#insert-inside-div)

### Node Clone 시 Text Node 없는 경우<a name="node-clone"></a>

`추가` 버튼과 `삭제` 버튼으로 리스트 생성 및 삭제

```html
<body>
    <button onclick="appendNode()">추가</button>
    <button onclick="removeNode()">제거</button>

    <ul id="list">
        <li>첫번째</li>
        <li>두번째</li>
    </ul>
</body>
<script>
    function appendNode() {
        var parent = document.getElementById("list");
        var newItem = parent.childNodes[1].cloneNode();
        
        newItem.firstChild.nodeValue = "추가된 리스트";
        parent.append(newItem);
    }
    function removeNode() {
        var parent = document.getElementById("list");
        var lastItem = parent.lastChild;
        parent.removeChild(lastItem);
    }
</script>
```

html 에서 추가한 `li` 태그에는 `Text Node` 가 붙어있어 `removeNode()` 를 두번 실행해야 `li` 태그 내의 문자열이 사라진다. 하지만 `appendNode()` 를 통해 추가된 Node는 `Text Node` 가 생성되지 않아 바로 삭제되는 문제

---

### Nodes of type '#document' may not be inserted inside nodes of type 'DIV'.<a name="insert-inside-div"></a>