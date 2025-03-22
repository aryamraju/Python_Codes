class BankAccount:
    def __init__(self):
        self.__salary = 50000 #private attribute
    def salary(self): #function Public
        return self.__salary
obj=BankAccount()
print(obj.salary())
