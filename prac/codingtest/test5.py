# 백준 파이썬 A+B - 7
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 문제 생각하기
T = int,input()
A,B = map(int, input().split())

for x in T :
    print("case %d : " + (A+B), x)

# 런타임 에러..ㅠ

# 재도전
T = int,input()
A,B = map(int, input().split())

for i in range(T) :
    print(f"case %{i} : " + (A+B))

# 오답 3개 틀림..
T = int,input()                             # -> 괄호주의...........
A,B = map(int, input().split())             # 계산도 반복이기 때문에 for문 안에 있어야해!

for i in range(T) :                         # range에 범위가 없음!
    print(f"case %{i} : " + (A+B))          # % -> # / f-string: {} 중괄호 안에서 바로 계산해서 출력 가능 (지금 내가 쓴 방식은 자바에 가까움)


# 수정 최종 버전
T = int(input())

for i in range(1, T + 1):                     # 왜 입력값의 +1 이냐면 파이썬은 범위가 해당숫자에 전까지만 해당하기 때문(끝숫자는 포함 안됌!)
    A, B = map(int, input().split())
    print(f"Case #{i}: {A + B}")             # 파이썬은 {}안에 자료형 직접 표시 (자바처럼 형식 지정해서 할 필요 없음)