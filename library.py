# 원하는 라이브러리 찾아서 가져다 쓰기만 하면 된다
# 라이브러리 사용 전에는 "import" 꼭 해줘야 한다는거 잊지 말기

# datetime.date : 연, 월, 일
import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2025, 4, 5)

# 최대 공약수 구하기
# math.gcd
# 어린이집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비 똑같이 최대 몇 봉가능?
import math
math.gcd(60, 100, 80)

# 최소 공배수 구하기
# math.lcm
# 시내버스는 15분, 마을버스는 25분 마다 도착 동시에 도착하는 다음 시간은?
import math
math.lcm(15, 25)

##############

# random vs randint : 둘다 무작위 출력은 맞지만 차이가 있다.

# random : 0과 1사이의 난수
# randint : 일정 범위 내에(매개변수 설정) 난수  
# random 은 매개변수 x, randint는 매개변수 o

import random
random.random()         # 무작위로 0과 1사이의 실수 출력
random.randint(1, 10)   # 1 ~ 10 사이의 정수중에서 출력

import random
def random_pop(data):
    number = random.randint(0, len(data) - 1) # len(data) - 1 : data list 의 마지막 인덱스를 나타냄 -> 리스트의 길이를 모른다고 가정 마지막 인덱스를 동적으로 나타내는 장치 만약 리스트의 길이를 알고 있다면 그냥 정수로 써도 됌
    return data.pop(number)

if __name__== "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
