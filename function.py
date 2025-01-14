# 파이썬 내장함수들 모음

# dir : 객체가 지닌 변수, 함수 보여주는 함수

# filter(함수, 반복 가능한 데이터) : 함수에 차례로 들어갈 반복 가능한 데이터 -> return 참일때만 묶어서 리턴
# 아래 positive 함수를 fileter version으로 변경해보기
def positive(l):
    result=[]       # 양수만 걸러 내서 저장할 변수
    for i in l:
        if i > 0:
            result.append(i) # 리스트에 i추가
    return result

print(positive([ 1, -3, 2, 0, -5, 6]))


def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
