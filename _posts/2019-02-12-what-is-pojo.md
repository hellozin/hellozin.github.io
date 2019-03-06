---
title: POJO란?
date: 2019-02-12 21:46:22
categories: 
 - TIL
 - Spring
tags: 
 - web
 - spring
 - term
---

Spring을 처음 시작하다보면 만나게 되는 POJO. 다른 블로그들이 그러하듯 이 POJO란 어떤 녀석인지 무슨일을 하는지 왜 존재하는지, 최대한 간단하게 알아보도록 하자.

<!-- more -->

### POJO (Enterprise Java Beans)

POJO에 대해 알아보기에 앞서 먼저 EJB라는 녀석에 대해 간략하게 알고 넘어가야한다.

기존의 서버측 어플리케이션 개발에는 몇 가지 문제점이 있었다. 개발자가 비즈니스 로직 뿐만 아니라 시스템 서비스나 DB 트랙젝션 처리 등 또한 구현해야했기 때문에 상당한 부담이 되었다.

이와 같은 문제점을 해결해 보자하며 Sun Mycrosystems에서 EJB를 세상에 내놓았다.  
(EJB는 어떠한 부품이 아닌 규약이라고 한다. 나중에 이해가 되면 무슨소리인지 써보겠다.)

EJB은 비즈니스로직을 Enterprise Bean으로, DB 처리와 트랜젝션 처리 등의 시스템 로직을 Container로 분리했다.

뭐 그렇단다. 사실 EJB 만으로도 내용이 많아 여기까지 써야할 것 같다.  
결국 EJB가 점점 복잡하고 불필요하게 사이즈가 커지는 경우가 많아 불만사항이 늘어났다.

그래서 이런 복잡한 구조가 아닌 그저 '평범한 자바 오브젝트'를 사용하기 시작했고 그럴듯한 이름을 지은것이 POJO, Plain Old Java Object 인 것이다.

### Reference

- EJB란? [Grim Reaper의 IT-Story](https://pokey.tistory.com/7)
- POJO (Plain Old Java Object) [DeveloperGatsby.com](https://itewbm.tistory.com/entry/POJOPlain-Old-Java-Object)
- [Java] POJO란? [Dreamy](https://m.blog.naver.com/writer0713/220700687650)