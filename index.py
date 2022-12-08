import math
# class Bankamat():
#     def __init__(self,a,b) -> None:
#         if a>b:
#             print("Pul yachildi")
#         elif a<b:
#             print("Pul yatarli emas")
# obj1 = Bankamat(a=int(input()),b=int(input()))

# class Bankomat():
#     def __init__(self,plastik,summa) -> None:
#         self.plastik = plastik

#     def deposit(self,emount):
#         self.emount = emount
#         if self.plastik > self.emount:
#             return "Pul mablagingiz olishingiz mumkin"
#         else:
#             return "Iltimos kartangiz qaytadan tekshiring mablag' yetarli emas"

# obj2 = Bankomat(10000000000,124356789)
# print(obj2.deposit(12432567))

# class Bankomat():
#     def __init__(self,ism,familiya) -> None:
#         self.ism = ism
#         self.familiya = familiya

#     def add(self,mng):
#         self.ism.append(mng)

#     def uchirish(self,feruz):
#         self.ism.remove(feruz)

#     def managerlar(self):
#         for i in obj1.ism:
#             return i

# obj1 = Bankomat(["kdjfask"],'aljf')
# obj1.add('Feruz')
# # obj1.uchirish(["Feruz"])
# print(obj1.ism)
# print(obj1.managerlar())

# def __init__ => metod

1 # class PowerA3:
#     def __init__(self,A,B,C,D,E) -> None:
#         self.A = A
#         self.B = B
#         self.C = C
#         self.D = D
#         self.E = E
#     def daraja(self):
#         return self.A**3,self.B**3,self.C**3,self.D**3,self.E**3

# obj1 = PowerA3(1,2,3,4,5)
# print(obj1.daraja())





class Employee():
    amount = 0
    def __init__(self,name,surname,money) -> None:
        self.name = name
        self.surname = surname
        self.money = money
    def fullname(self):
        return f"{self.name} {self.surname}"
    def oyligi(self):
        self.money = int(self.money*self.amount)

# obj1 = Employee('Roziqbek',14,'Olimjonov',200000)
# print(obj1.fullname())
# Employee.amount = float(input())
# obj1.oyligi()
# print(obj1.money)

class Developer(Employee):
    amount = 1.2
    def __init__(self, name, surname, money,prog_lang) -> None:
        super().__init__(name, surname, money)
        self.prog_lang = prog_lang

# empl1 = Developer('Abbos',22,"Teshayev",10000000,'Python')
# empl2 = Developer('Roziqbek',15,'Olimjonov',1000000,"Python")
# print(empl1.__dict__)

class Manager(Employee):
    def __init__(self, name, surname, money, employees=None):
        super().__init__(name, surname, money)
        if employees is None:
            self.employees = None
        else:
            self.employees = employees
    def add_employee(self,emp):
        self.employees.append(emp)
    def print_employee(self):
        for i in self.employees:
            print(f"Employee - {i.fullname()}")

empl1 = Developer('Abbos',"Teshayev",1000000,'Python')
empl2 = Developer('Roziqbek','Olimjonov',123456667,"java")
empl3 = Developer('Oybekxoja','Kuchuk',1,'None')
mng = Manager('Abbos','Teshaev',12345678,[empl1])
mng.add_employee(empl2)
mng.add_employee(empl3)
mng.print_employee()





