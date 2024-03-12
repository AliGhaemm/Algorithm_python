class MyClass:
    x = 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} : {self.age}"

    def intro(self):
        print("Hello my name is " + self.name + " with " + str(self.age) + " years old")


class Student(Person):
    def __init__(self, name, age, major):
        self.major = major
        super().__init__(name=name, age=age)
    

p1 = MyClass()
print(p1.x)

person1 = Person("Ali", 22)
print(person1.name + " : " + str(person1.age))
print(person1)
person1.intro()
person1.age = 30
person1.intro()
person1.name = "mahdi"
person1.intro()
person1.intro()
