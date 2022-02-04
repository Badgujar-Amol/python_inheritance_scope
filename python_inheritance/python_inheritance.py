# single level inheritance
class collage:
    def cmethod(self):
        print("this is collage class")

class student(collage):
    def smethod(self):
        print("this is student class")

s = student()
s.smethod()
s.cmethod()

# multi level inheritence
class books:
    def bmethod1(self):
        print("This is from books class")


class subject(books):
    def smethod2(self):
        print("This if from subject class")


class subject1(subject):
    def ssmethod3(self):
        print("This is from subject1 class")

s = subject1()
s.bmethod1()
s.smethod2()
s.ssmethod3()

# multiple inheritance
class animal:
    def method1(self, name):
        print("animal name is", name)

class dog(animal):
    def method2(self, name):
        print("animal dog name is", name)

class cat(animal):
    def method3(self, name):
        print("animal cat name is", name)

d = dog()
d.method1('peacock')
d.method2('sam')

c = cat()
c.method1('lion')
c.method3('mauuu')

#Hierarchical inheritance
class Parent:
    def pDisplay(self):
        print('Parent')
class Child1(Parent):
    def c1Display(self):
        print('Child1')
class Child2(Parent):
    def c2Display(self):
        print('Child1')
c1 = Child1()
c1.pDisplay()
c1.c1Display()
c2 = Child2()
c2.pDisplay()
c2.c2Display()

# Method Overiding
class Bank:
    def getroi(self):
        return 10

class SBI(Bank):
    def getroi(self):
        return 7

class ICICI(Bank):
    def getroi(self):
        return 8

b1 = Bank()
b2 = SBI()
b3 = ICICI()