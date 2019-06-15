---
title: Annotation Valid 결과 직접 처리하기
date: 2019-06-16 08:03:47
categories: 
 - spring
tags: 
 - valid
 - controller advice
---

**Spring**을 사용하면 입력값을 받을 때 `@Valid`를 사용해서 쉽게 검증을 할 수 있는데 기본적으로 반환하는 에러 메시지는 너무 길고 복잡해 필요에 따라 처리하는 방법을 알아보았습니다.

우선 간단한 `POST` 요청을 처리하는 과정을 살펴보겠습니다.

```json
HTTP POST /api/user
{
  "name": "hello",
  "age": 20
}
```

이와 같은 요청을 처리하기 위해 다음과 같은 `Controller`를 작성합니다.

```java
@PostMapping("/api/user")
@ResponseBody
public String joinUser(@RequestBody User user) {
  /* user 정보 저장 */
  return "success";
}
```

입력받는 값을 **검증**하고 싶다면 `User` 클래스에서 **Annotation**을 통해 명시하고 `Controller`의 매개변수 앞에 `@Valid`를 붙여 편리하게 검사할 수 있습니다.

```java
class User {

  @NotBlank   // name은 비어있지 않은 문자열만 허용
  String name;

  @Min(0)     // age는 0 이상의 값만 허용
  int age;

}

@PostMapping("/api/user")
@ResponseBody
public String joinUser(@RequestBody @Valid User user) { // @Valid 추가
  /* user 정보 저장 */
  return "success";
}

```

이제 해당 요청 시 정의한 **Validation**을 어길 경우 `MethodArgumentNotValidException`이 발생하며 다음과 같은 결과를 반환합니다.

```json
HTTP POST /api/user
{
  "name": "hello",
  "age": -1         // @Min(0) 위반
}

반환값
{
  "timestamp": "2019-06-15T23:26:33.542+0000",
  "status": 400,
  "error": "Bad Request",
  "errors": [
    {
      "codes": [
        "NotBlank.user.name",
        "NotBlank.name",
        "NotBlank"
      ],
      "arguments": [
        {
          "codes": [
            "user.name",
            "name"
          ],
          "arguments": null,
          "defaultMessage": "name",
          "code": "name"
        }
      ],
      "defaultMessage": "반드시 값이 존재하고 공백 문자를 제외한 길이가 0보다 커야 합니다.",
      "objectName": "user",
      "field": "name",
      "rejectedValue": null,
      "bindingFailure": false,
      "code": "NotBlank"
    }
  ],
  "message": "Validation failed for object='user'. Error count: 1",
  "trace": "org.springframework.web.bind.MethodArgumentNotValidException: Validation failed for argument [0] in public java.lang.String me.hello.blog.SimpleController.joinUser(me.hello.blog.User): [Field error in object 'user' on field 'name': rejected value [null]; 
  codes [NotBlank.user.name,NotBlank.name,NotBlank]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; 
  arguments []; default message [name]]; 
  default message [반드시 값이 존재하고 공백 문자를 제외한 길이가 0보다 커야 합니다.]]
  ...(생략)
```

굉장히 길고 자세한 결과가 반환되지만 경우에 따라 간단한 결과만 반환할수도 있기 때문에 `Controller`의 예외를 처리할 수 있는 `ExceptionHandler`로 해당 메시지를 줄여보도록 하겠습니다.

`Controller`내에 정의해도 되고 전역 설정을 위해 `@ControllerAdvice`를 정의해도 되는데 여기서는 `@ControllerAdvice`를 사용해서 처리해 보도록 하겠다.

```java
[ ExceptionAdvisor.java ]

@ControllerAdvice   // 전역 설정을 위한 annotaion
@RestController
public class ExceptionAdvisor {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public String processValidationError(MethodArgumentNotValidException exception) {
        BindingResult bindingResult = exception.getBindingResult();

        StringBuilder builder = new StringBuilder();
        for (FieldError fieldError : bindingResult.getFieldErrors()) {
            builder.append("[");
            builder.append(fieldError.getField());
            builder.append("](은)는 ");
            builder.append(fieldError.getDefaultMessage());
            builder.append(" 입력된 값: [");
            builder.append(fieldError.getRejectedValue());
            builder.append("]");
        }

        return builder.toString();
    }

}
```

`BindingResult`의 `FieldError`에서 검증이 실패한 **필드명**, 실패에 대한 **메시지**, 검증이 실패한 **입력값**을 가져와 메시지를 만들어 반환하고 있습니다.

위의 코드를 작성한 뒤의 **반환값**은 다음과 같이 나옵니다.

```json
[age](은)는 반드시 0보다 같거나 커야 합니다. 입력된 값: [-1]
```

훨씬 간결해진 메시지를 볼 수 있습니다. 물론 이렇게 바꾸는 것이 정답이 아니니 필요에 따라 반환하는 메시지를 처리하면 됩니다.