# 입력값이 몇개인지 모르는 함수
# 저 *args 값을 어떤걸 넣을지 몇개를 넣을지 일단 모르지만 함수를 일단 만들어놔
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# 그 다음에 만들어놓은 함수를 사용하는검니다
result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

# 매개변수 한개 아니라 두개도 가능
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul("add", 1, 2, 3, 4, 5)
print(result)

# 키워드 매개변수
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='huoguo', age=10)

# 매개변수 초기값 미리 설정하기
def say_myself(name, age, female=True):
    print("내 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %age)
    if female:
        print("여자입니다.")
    else:
        print("남자입니다.")

say_myself("박훠궈", 20, True)  # 내 이름은 박훠궈 입니다. 나이는 20살 입니다. 여자입니다.
say_myself("박훠궈", 20, False) # 내 이름은 박훠궈 입니다. 나이는 20살 입니다. 남자입니다.
# 저 True 라는 매개변수의 위치가 만약 가운데라면 에러가 발생할 것. 매개변수는 항상 뒤쪽에 위치해야 한다.

# 기본적으로 함수 밖의 변수는 함수내에 어떤 영향도 미치지 못한다. 이름이 같아도
# 영향을 끼칠수 있는 2가지 방법
# 만약
a = 1               # -> 전역변수
def vartest(a):
    a = a + 1       # -> 지역변수

vartest(a)          # -> 함수 내부에서 a의 값을 변경했지만 전역변수에는 미치지 못한다. 
print(a)

# 1. return 사용하기 -> 이때도 여전히 두 a의 값은 다른 값이다.
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 2. global 사용하기(비추천) -> 함수 안에서 밖의 변수를 직접 사용하겠다는 뜻. 함수는 독립적인게 좋으므로 비추천
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)