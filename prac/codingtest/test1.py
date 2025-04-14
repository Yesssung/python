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