
# class Animals:
#     def __init__(self, name):
#         self.name = name
# class Dog(Animals):
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print("Vov-vov_vovovov")
#
# class Cat(Animals):
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print("Myau-myau")
# class Cow:
#     def speak(self):
#         print("Muuuuu-muuuu")
#
# a = Dog("Gitler")
# b = Cat("Tommy")
# c = Cow()
#
# a.speak()
# b.speak()
# c.speak()





# class Triangle:
#     def __init__(self, highA, tomonA):
#         self.tomonA = tomonA
#         self.highA = highA
#     def yuza(self):
#         print(f"Uchburchak yuzi: {(self.highA*self.tomonA)/2}")
# class Square:
#     def __init__(self, tomonA, tomonB):
#         self.tomonA = tomonA
#         self.tomonB = tomonB
#     def yuza(self):
#         print(f"To'rtburchak yuzi: {self.tomonA*self.tomonB}")
# class Circle:
#     def __init__(self, radius, pi):
#         self.radius = radius
#         self.pi = pi
#     def yuza(self):
#         print(f"Doiraning yuzi: {self.pi*(self.radius**2)}")
#
# a = Triangle(5,12)
# b = Square(7, 9)
# c = Circle(5, 3.14)
#
# a.yuza()
# b.yuza()
# c.yuza()







# class Vehicle:
#     def start_engine(self):
#         pass
# class Car(Vehicle):
#     def start_engine(self):
#         print("Avtomobilning dvigateli ishga tushirildi.")
# class Mototsikl(Vehicle):
#     def start_engine(self):
#         print("Mototsiklning dvigateli ishga tushirildi.")
#
# a = Car()
# b = Mototsikl()
# a.start_engine()
# b.start_engine()






# class Employee:
#     def __init__(self, kunlik):
#         self.kunlik = kunlik
#
# n = int(input("Menejerning ishlagan kunlari sonini kiriting: "))
# class Menejer(Employee):
#     def __init__(self, kunlik):
#         super().__init__(kunlik)
#     def calculate_salary(self):
#         print(f"Menejerning oyligi: ${n*self.kunlik}")
#
# m = int(input("Dasturchining ishlagan kunlari sonini kiriting: "))
# class Developer(Employee):
#     def __init__(self, kunlik):
#         super().__init__(kunlik)
#     def calculate_salary(self):
#         print(f"Dasturchining oyligi: ${m*self.kunlik}")
#
# n1 = int(input("Menejerning kunlik ish xaqqini kiriting: "))
# m1 = int(input("Dasturchining kunlik ish xaqqini kiriting: "))
# a = Menejer(n1)
# b = Developer(m1)
#
# a.calculate_salary()
# b.calculate_salary()






# class Fruits:
#     def __init__(self, name):
#         self.name = name
#
# class Apple(Fruits):
#     def __init__(self, name):
#         super().__init__(name)
#     def taste(self):
#         print(f"{self.name}ning ta'mi o'zgacha!")
#
# class Banana(Fruits):
#     def __init__(self, name):
#         super().__init__(name)
#     def taste(self):
#         print(f"{self.name}ning tami juda mazali.")
#
# class Orange(Fruits):
#     def __init__(self, name):
#         super().__init__(name)
#     def taste(self):
#         print(f"{self.name}ning tami ajoyib!!!")
#
# olma = Apple("Olma")
# banan = Banana("Banana")
# apelsin = Orange("Apelsin")
#
# olma.taste()
# banan.taste()
# apelsin.taste()




# import _thread
# import turtle
# class Shape:
#     def __init__(self, size, color, shape, speed, x, y):
#         self.t = turtle.Turtle()
#         self.t.pensize(size)
#         self.t.color(color)
#         self.t.shape(shape)
#         self.t.speed(speed)
#         self.t.up()
#         self.t.goto(x, y)
#         self.t.down()
#
#     def drw(self):
#         raise NotImplementedError("chiz metodi yartilmagan!!!")
#
# class Circle(Shape):
#     def __init__(self, size, color, shape, speed, x, y):
#         super().__init__(size, color, shape, speed, x, y)
#     def draw(self, a):
#         self.t.circle(a)
#
# class Rectangle(Shape):
#     def __init__(self, size, color, shape, speed, x, y):
#         super().__init__(size, color, shape, speed, x, y)
#
#     def draw(self, a):
#         for i in range(4):
#             self.t.fd(a)
#             self.t.right(90)
#         self.t.end_fill()
#
#
# a = Circle(10, "Yellow", "turtle", 6, 350, -450)
# b = Rectangle(10, "Red", "circle", 3, -300, 250)
#
# _thread.start_new_thread(a.draw, (350, ))
# _thread.start_new_thread(b.draw, (400,))
#
# turtle.done()





# class Instrument:
#     def __init__(self):
#         pass
#
#     def play(self):
#         raise NotImplementedError("play metodi yartilmagan!!!")
#
# class Piano(Instrument):
#     def play(self):
#         print("Pianina chalindi.")
#
# class Guitar(Instrument):
#     def play(self):
#         print("Gitara chalindi")
# class Dump(Instrument):
#     def play(self):
#         print("Baraban chalindi")
#
# p = Piano()
# g = Guitar()
# d = Dump()
#
# p.play()
# g.play()
# d.play()









# class Animal:
#     def move(self):
#         pass
#
# class Bird(Animal):
#     def move(self):
#         print("Qush uchadi.")
#
# class Fish(Animal):
#     def move(self):
#         print("Baliq suziladi.")
#
# class Mammal(Animal):
#     def move(self):
#         print("Sutemizuvchi yuradi.")
#
# a = Bird()
# b = Fish()
# c = Mammal()
#
# a.move()
# b.move()
# c.move()






# class Vehicle:
#     def __init__(self, fuel_efficiency):
#         self.fuel_efficiency = fuel_efficiency
#     def cal_fuel(self, masofa):
#         return masofa / self.fuel_efficiency
#
# class Car(Vehicle):
#     def __init__(self, fuel_efficiency):
#         super().__init__(fuel_efficiency)
# class Mototsikl(Vehicle):
#     def __init__(self, fuel_efficiency):
#         super().__init__(fuel_efficiency)
#
# car1 = Car(12)
# car2 = Car(14)
# moto1 = Mototsikl(20)
# moto2 = Mototsikl(22)
#
# masofa = 200
#
# car1 = car1.cal_fuel(masofa)
# car2 = car2.cal_fuel(masofa)
# moto1 = moto1.cal_fuel(masofa)
# moto2 = moto2.cal_fuel(masofa)
#
# print("1-Avtomobil  yoqilg'i samaradorligi:", car1, "litr")
# print("2-Avtomobil  yoqilg'i samaradorligi:", car2, "litr")
# print("1-Mototsikl  yoqilg'i samaradorligi:", moto1, "litr")
# print("2-Mototsikl  yoqilg'i samaradorligi:", moto2, "litr")
