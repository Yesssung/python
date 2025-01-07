# class 와 객체, 인스턴스를 알아봅시다

class FourCal: # FourCal 이라는 이름의 클래스
    def setdata(self, first, second): # 그 클래스 안에 있는 setdata라는 함수는 / self, first, second 라는 세개의 매개변수 존재
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


# self 자기 자신을 가르키는 매개변수
# 호출할 객체 자신 그 자체라는 말
# 파이썬은 관례상 self 라고 쓰지만 다른 이름을 써도 상관 없음!

a = FourCal()
a.setdata(4, 2) # 여기서 매개변수가 2개인 이유는 self는 a 객체에 자동 전달이기 때문


# 만약 setdata를 하지 않고 바로 add나 다른 메서드를 호출하면 에러가 난다. 값이 없기 때문

# 생성자 : 객체 생성시 자동으로 호출되는 메서드 : __init__

class FourCal: 
    def __init__(self, first, second): 
        self.first = first
        self.second = second

    def setdata(self, first, second): 
        self.first = first
        self.second = second



# setdata와 모든게 동일 but 자동으로 생성되는 생성자로 인식되어서 객체가 생성될때 자동으로 해당 함수가 호출된다
a = FourCal() # 그렇기 때문에 이 경우 이미 init이 자동 호출 되었으므로 값이 없으면 에러표시가 뜸
a = FourCal(4, 2) # 이렇게 값을 바로 추가해줘야 한다. 


# 상속 상속은 추가 및 기능 확장용!
class MoreFour(FourCal): # 상속받을 클래스를 괄호 안에 넣기! -> FourCal을 상속 받았으므로 해당 클래스 안에 있는 메서드 전부 사용 가능!
    def pow(self):
        result = self.first ** self.second
        return result # FourCal의 메서드를 전부 사용하면서도 pow 메서드 기능 추가 가능!
    
# 메서드 오버라이딩
class SafeFourCal(FourCal):  # FourCal을 상속할거구요
    def div(self):           # 원래 FourCal 안에 있는 div 메서드를 동일한 이름으로 새로 구성하겠다 -> 메서드 오버라이딩 이때 부모클래스에서 상속받은 메서드 대신에 오버라이드 한 메서드가 호출됩니다요 오키?
        if self.second == 0:
            return 0
        else:
            return self.first / self.second