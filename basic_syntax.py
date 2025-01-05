# Operator
# 기본적으로 하나의 python 파일은 그 자체가 모듈이 된다.(모듈은 직접 실행될 수도 있고 불러와질 수도 있다.)
def arith_oper():
    print("========== 산술 연산")
    print(7/3)       # 파이썬 3 -> int/int -> float
    print(7//3)      # 정수로 몫을 얻고 싶으면 슬래시 두 개!
    print(7%3)       # 정수 나눗셈의 나머지 연산자

    # 나눗셈의 몫과 나머지 동시에 구하고 싶다면?
    print(divmod(7,3)) # 출력 형태: (2,1) 앞에가 몫 뒤에가 나머지(Tuple형태)

    print("7/3의 몫: ", divmod(7,3)[0])            # 7/3의 몫
    print("7/3의 나머지: ", divmod(7,3)[1])         # 7/3의 나머지

    print(7**3)     # 지수 승: 7의 3제곱
    print(pow(7, 3))      # 지수 함수: 7의 3제곱

def rel_oper():
    #pass #함수 구현부 없어도 비워두면 안됩니다.
    print("========== 비교 연산자")
    # >, >=, <, <=, ==, !=

    s1="python"; s2="python"
    print("문자열의 비교: ", s1 == s2)

    # 복합 관계식
    a = 6
    # a가 0 ~ 10 사이의 값인가?
    # 조건 1: a > 0
    # 조건 2: a < 10
    # 조건1 & 조건2
    print(0 < a and a < 10)
    print(0 < a < 10)

    # 다양한 자료 구조의 대소 비교
    print("문자열의 대소: ", "abcd" > "abd")
    print("튜플의 대소: ", (1, 2, 3) > (1, 3, 4))


    # 동질성의 비교 ==, 동일성의 비교 is
    a = 10; b = 20; c = a
    print("a == b ?", a==b)
    print("a is b ?", a is b)
    print("a == c ?", a == c)
    print("a is c ?", a is c)

import keyword # import 키워드 -> 모듈을 불러오는 명령어

def var_ex():
    print("========== 변수")
    # 문자, 숫자, _의 조합
    # 숫자로 시작하면 안됨
    # 예약어는 변수명으로 사용될 수 없다.
    # 파일명도 변수 명명 규칙에 맞춰 줘야 한다.
    print("예약어 목록: ", keyword.kwlist)
    print("예약어 갯수: ", len(keyword.kwlist))

def assignment_ex():
    print("========== 치환문")
    # 변수 선언 절차가 없다

    print("namespace: ", dir())
    a = 2024    # 첫번째 할당이 발생할 때 namespace에 추가된다.
    b = a + 1
    print(a, b)
    print("namespace: ", dir())

    # 여러 변수를 한꺼번에 할당할 수 있다.
    c, d = 3.5, 5.3
    print("c, d = ", c, d)

    # 값의 교환(swap)
    c, d = d, c
    print("c, d = ", c, d)

    # 같은 값을 동시 할당
    x = y = z = 10
    print(x, y, z)
    # 파이썬은 동적 타이핑 언어
    a = 2024                     # 값이 할당될 때 타입이 결정 -> 타입이 뭔지 확인
    print(a, "is", type(a))      # 현재 객체의 형식을 체크
    a = "Hello Python"
    print(a, "is", type(a))      # a의 타입이 뭔지 알려줌!

    # 특정 변수가 특정 개체인지 여부를 판단하는 함수 : isinstance
    print("a는 str의 객체?", isinstance(a, str))

    # 확장 치환문: 산술, 비트 연산자 등은 확장 치환문으로 변경 가능
    a = 10
    a += 10         # a = a + 10
    print(a)


def bool_ex():
    print("========== bool 연습")
    # 참(True), 거짓(False)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판정한다.
    # 조건 분기, 흐름 제어에서 활용되기 때문에 중요하다
    # boolean 판정
    #  - 논리 연산자 비교 연산자의 결과로 출력
    #  - bool 객체 함수를 통해 얻을 수 있음
    print(bool(0))
    a = 2024
    print(a > 0)        # 비교 연산자를 통한 논리 값의 판정
    print(type(a))      # a의 타입은 int

    print(isinstance(True, bool))   # 2
    print(isinstance(True, int))    # 2
    print(True + True)

    # 자료의 형태에 의한 boolean 판정 -> 0이거나 비어있는 부분을 False / 어떤 데이터라도 셋팅 되어있다면 True
    print(bool(2024), bool(0))                       # int 값에 의한 boolean
    print(bool(3.14), bool(0))                       # float 값에 의한 boolean
    print(bool("Python"), bool(""))                  # str 값에 의한 boolean

    print(bool([1, 2, 3]), bool([]))                 # list 값에 의한 boolean
    print(bool({"key": "value"}), bool({}))          # dict 값에 의한 boolean
    print(bool(None))                                # none은 비어있다.(자바에서 null)

    # 논리식의 계산 순서 : Curcuit Break
    # OR : 첫 번째 True 연산 결과를 취한다
    # AND : 둘 다 True면 뒤쪽 결과를 취한다.
    # AND : 전체 논리식이 거짓이라면 None을 반환
    print("CB 1 : ", [] or "logical")               # False or True
    print("CB 2 : ", 'logical' or 'operator')       # True or True
    print("CB 2-1 : ", 'logical' and 'operator')    # True and True
    print("CB 3 : ", '' or 'operator')              # False or True
    print("CB 3-2 : ", '' and 'operator')           # False and True
    print("CB 4 : ", None and 1)                    # False and True
    print("CB 5 : ", None or [])                    # False or False


def type_hint():
    # 파이썬은 동적 타이핑 언어 -> 변수 타입을 명시적으로 지정하지 않음
    # 3.5 부터 타입 힌트를 이용,

    def add(a: int, b: int) -> int:                 # 두 개의 int 입력 받아서 int를 return 하는 함수
        return a + b

    print(add(10, 20))
    # print(add("Python", 3.10))

    def greet(name: str) -> str:                    # str 입력 받아서 str을 return 하는 함수
        # return "Hello, " + name
        return 2024

    untyped = "string"                              # Type Hint가 적용되지 않은 변수
    print(untyped)
    untyped = 2024
    print(untyped)

    typed: str = "string"                           # Type Hint가 적용된 변수
    print(typed)
    typed = 2024
    print(typed)

# 파이썬은 선언만 해두고 나중에 짠다고 해도 저 블로을 비워두면 안된다. -> pass 처리 해놓기
def int_ex():
    print("========== 정수형 연습")

    a = 2024            # 리터럴 선언
    b = int(2024)       # 타입 함수 사용(타입을 써놓은게 타입함수)

    print(a, "is", type(a))
    print(b, "is", type(b))

    # 2진, 8진, 16진 정수 표현 가능
    b = 0b1101          # 0b
    o = 0o23            # 0o
    x = 0xFF            # 0x

    print(b, o, x)

    # 파이썬 3에서는 int 와 long 구분 없음
    # long 데이터의 저장크기 64bit 초과해서 적재할 수 있음
    i = 2 ** 2048
    print(i)
    print(i.bit_length())

    # 진법 변환 함수 -> 어떤 숫자를 진수별로 알고 싶을 때
    i = 48
    print(i, bin(i), oct(i), hex(i))

def float_ex():
    print("========== 실수형 연습")
    a = 3.14159                         # 리터럴로 생성
    print(a, "is", type(a))
    print(isinstance(a, float))         # a가 float인가?

    b = float(3.0)                      # 타입 함수로 생성
    print(b, "is", type(b))
    print(isinstance(b, float))         # b는 float인가?

    # 둘 다 같은 실순데 a는 false, b는 true가 나온데 b소수점 아래 0이기 때문에 정수로 보는 것
    print(a.is_integer(), b.is_integer())

    # 지수 표기법으로도 확인 가능
    c = 3e3         # 3 * 10 ** 3
    d = -2E-5       #-2 * 10 ** -5

    print(c, d)
    print(-2E-5 == -0.00002)    # 같은 표현


def complex_ex():
    print("========== 복소수 연습")
    # 복소수 : 실수부 + 허수부j
    a = 4 + 5j
    print(a, "is", type(a))
    print(isinstance(a, complex))               # a는 복소수 인가?

    b = 7 - 2J
    print(a + b)                                # 복소수는 산술연산이 가능
    print(b.real, b.imag)                        # 실수부, 허수부
    print(a, "의 켤레 복소수는", a.conjugate())    # 켤레 복소수

if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 저 위 코드의 의미는 이름이 main저 자리에 이 프로젝트의 메인 이름이 들어간다. __name__=="python_basics"
    # 직접 실행될 경우 (최상위 모듈일 경우) __name__=="__main__"
    # arith_oper()          # 산술 연산자 연습
    # rel_oper()            # 비교 연산자 연습
    # var_ex()              # 변수 연습
    # assignment_ex()       # 변수 치환 연습
    # bool_ex()
    # type_hint()
    # int_ex()
    # float_ex()
    complex_ex()