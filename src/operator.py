class OperatorList:
    def __init__(self, x:float = 1, y:float = 2):
        self.x = x
        self.y = y

    def add(self, x:float, y:float):
        return x + y

    def substract(self, x:float, y:float):
        return x - y

    def multiply(self, x:float, y:float):
        return x * y

    def divide(self, x:float, y:float):
        return x / y