---
layout: post
date: 2018-12-15 01:47
title:  "What is Progressive Web Apps?"
permalink: "/web/"
mood: happy
category: 
- information
---

### Progressive Web Apps (PWA)

앱 수준과 같은 사용자경험을 웹에서 제공하는 것이 목적. **한마디로 '앱 같은 웹'**

**특징**

- 불안정한 네트워크, 심지어 오프라인 상황에서도 동작
- 기존 WEB 앱과 달리 모바일 앱 형태를 지님
- 모바일 앱과 달리 설치가 필요없고 링크를 통해 사용 가능

[PWA를 사용하는 기업들](https://pwa.rocks/)

> 비슷한 기술 : 구글의 ‘AMP’(Accelerated Mobile Pages) 프로젝트

### PWA의 기준

PWA는 하나의 기술로 이루어진 것이 아니라 특정 요구사항을 만족하거나 다음 기능들이 구현될 경우 PWA라고 본다. 
( 물론 절대적인 것은 아니며 대략적인 지표일 뿐. 앱의 완성도를 측정하는 도구도 있으며 현재는 [LightHouse](https://developers.google.com/web/tools/lighthouse/)가 가장 유명 )

**웹 앱을 PWA로 식별하는데 사용되는 몇 가지 핵심 원칙**

- **발견 가능(Discoverable)** : 검색 엔진으로 부터 해당 앱을 찾을 수 있어야 한다. 
- **설치 가능(Installable)** : 기기 홈 화면에 설치할 수 있어야 한다.
- **연결 가능(Linkable)** : URL을 통해 앱을 공유할 수 있어야 한다.
- **네트워크 독립성(Network independent)** : 네트워크가 불안정하거나 오프라인 상태에서도 동작되어야 한다.
- **점진성(Progressive)** : 최신 브라우저는 힘들더라도 이전 브라우저의 기본 기능은 사용할 수 있어야 한다.
- **재참여(Re-Engageable)** : 앱에서 사용자에게 알림을 보낼 수 있어야 한다.
- **반응성(Responsive)** : 모든 기기의 화면이나 브라우저에서 사용 가능해야 한다. (모바일, 태블릿, 노트북, TV, 냉장고 등)
- **안전(Safe)** : 민감한 데이터에 접근하려는 제 3자로 부터 안전해야 한다.

> 출처 : MDN

### 주요 기술

- **HTTPS** : 좀 더 안전하고 안정적으로
- **Service Worker** : 오프라인 웹앱, 푸쉬 그리고 백그라운드 실행
- **Web Manifest and Web APK** (Not Yet, but very Soon) : 웹앱 설치 그리고 관리
- **Push Notification** : 네이티브 앱과의 간극을 좁혀줄 마법
- **Performance Enhacement**(점진적 성능 향상)
  - RAIL Pattern, 불편 없는 UX 경험
  - PRPL Pattern, 로딩/실행 성능을 위한 여러가지 방법들
    - Page Load Performance
    - Preloading: Server Side Rendering
    - Lazy-loading/Streaming : preload, Code-splitting, HTTP2 w/ Server push
    - Parallel-loading Patterns: navigation-preload
- **The Next Big Things of the Web: Web Assembly, Newbie Web Fraemworks**

### Server Worker

웹 페이지와 별개로 브라우저가 백그라운드에서 실행되는 스크립트. 

### 주요 개발도구

- Web Starter Kit : 바닐라 자바스크립트를 사용한 웹앱 제작 도구
- Anguler Mobile Kit
- Polymer-CLI
- React
- Lighthouse (구글에서 만든 웹앱의 개발 가이드 및 확인 도구)