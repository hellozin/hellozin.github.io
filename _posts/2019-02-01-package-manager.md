---
title: package manager 는 왜 사용할까?
date: 2019-02-01 20:54:10
categories: 
 - TIL
tags: 
 - web
---

개발을 하다 보면 `apt`, `yum`, `npm`, `pip`, `gem` 등 다양한 **javascript package manager** 를 접하게 된다. 이를 사용하면 무언가를 설치하고 관리한다는 것은 알고 있었지만 자세한 용도나 목적을 몰라 이번 기회에 알아보게 되었다.

### Package 란?

우선 **package** 가 무었인지 알아보자.

**package** 란 누군가 만들어 놓은 완성된 소프트웨어 혹은 다른 소프트웨어를 완성시키기 위해 필요한 부품이 되는 소프트웨어를 의미한다. 

이러한 **package** 들을 설치하기 위해서는 다운로드, 설치, 빌드, 테스트, 업그레이드, 의존성 관리 등 다양한 상황을 고려해야 하는데 이를 **package manager** 가 도와준다.

### Package Manager 란?

**package manager** 에는 여러가지가 있지만 자바스크립트 패키지 매니저 중 하나인 `yarn` 을 중심으로 알아보려 한다.

### Reference

- [생활코딩-패키지매니저](https://opentutorials.org/course/1750/10064)