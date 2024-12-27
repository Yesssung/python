# for문 사용해서 1부터 100까지 숫자 출력해보기
# for i in range(101):
#     print(i)

# 평균 점수 구하기
# 내답(오답..ㅜㅠㅜㅠㅜ)
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total/score  # -> 점수 그대로 나누는게 아니라 학생의 수로 나눠야지!!
print(average)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)

# 리스트 컴프리헨션 사용하기
# 컴프리헨션? -> 파이썬 리스트를 간결하고 효율적으로 생성할 수 있도록 도와주는 문법
# 홀수만 골라서 *2 하기
# 기본형
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

# 컴프리헨션형
numbers=[1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)