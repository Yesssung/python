# 1. 상속
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCaldulator(Calculator):
    def minus(self, val):
        self.value -= val


# 2. 오버라이딩
class MaxLimitCalulator(Calculator):
    def add(self, val):
        if self.val > 100:
            self.val = 100