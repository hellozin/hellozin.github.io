---
title: BS Code commit 시 configure 문제
description: VS Code commit 시 name, email configure 문제 발생
categories:
 - ERROR/VCS
---

VS Code는 다양한 기능을 지원하는 Editor로 내장된 Source Control 기능을 이용해 쉽고 간편하게 버전관리를 할 수 있다.

보통 Git Bash 나 VSC 터미널에서 Git을 사용했는데 VSC 내부에 Source Control 패널이 있어 사용해보았더니

![](https://www.github.com/hellozin/hellozin.github.io/assets/images/post/2019-01-06-vs-code-error-errormsg.png)

`Make sure you configure your 'user.name' and 'user.email' in git.`

name 과 email 을 설정했는지 물어보는 팝업창이 나타났다.

간단한 해결책으로는 Git Bash에서 설정해 주면 해결이 된다.

```python
git config --global user.name '이름'
git config --global user.email '이메일'
```