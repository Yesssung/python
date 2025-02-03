class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCaldulator(Calculator):
    def minus(self):
        result = self.val