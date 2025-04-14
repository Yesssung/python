# 백준 파이썬 배우기 사칙연산
# 정석 바보버전..
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first // self.second
        return result
    def div2(self):
        result = self.first % self.second
        return result
    
a, b = map(int, input().split())  
calc = FourCal(a, b)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
print(calc.mod())



# 쥰나 간단 최고 버전..
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

# input 으로 입력 받고 클래스 없이 바로 사칙연산 써서 처리하는 방법..
# class사용할때
# 1. 여러 연산이나 상태를 계속 기억해야 하는 경우
# 2. 객체지향적으로 구조를 잡아야 할 때
# 3. 테스트용 계산기 만들 때 (예: 계산기 앱)
# 4. 실제 서비스 코드처럼 연습할 때