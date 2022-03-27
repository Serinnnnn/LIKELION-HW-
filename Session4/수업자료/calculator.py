from tkinter.font import names


class Calculator:
    def __init__(self,name, age):
        self.name = name
        self.result = 0
        self.age = age

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        if (num == 0):
            print("0으로 나눌 수 없습니다")
            return None
        self.result /= num
        return self.result

calculator1 = Calculator("홍세린", 24)
calculator1.add(2)
calculator1.add(3)
calculator1.sub(1)
print(calculator1.result)
print(calculator1.age)
print(calculator1.name)








# __init__ 생성자함수 : 소유자의 기초적 정보 
# self: 인스턴스 본인을 의미, 본인
