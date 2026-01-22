
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Toyota", "Corolla")
car1.display()















class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Ali", 20)
student1.display()












class Grandparent:
    def __init__(self, family_name):
        self.family_name = family_name

class Parent(Grandparent):
    def __init__(self, family_name, parent_name):
        super().__init__(family_name)
        self.parent_name = parent_name

class Child(Parent):
    def __init__(self, family_name, parent_name, child_name):
        super().__init__(family_name, parent_name)
        self.child_name = child_name

    def display(self):
        print("Family Name:", self.family_name)
        print("Parent Name:", self.parent_name)
        print("Child Name:", self.child_name)

child1 = Child("Khan", "Ahmed", "Usman")
child1.display()
















class Device:
    def __init__(self, brand):
        self.brand = brand

class Computer(Device):
    pass

class Laptop(Computer):
    def display(self):
        print("Laptop Brand:", self.brand)

laptop1 = Laptop("Dell")
laptop1.display()














class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    pass

class Manager(Employee):
    def display(self):
        print("Manager Name:", self.name)

manager1 = Manager("Ayesha")
manager1.display()





















class Academics:
    def __init__(self, subject):
        self.subject = subject

class Sports:
    def __init__(self, sport):
        self.sport = sport

class Student(Academics, Sports):
    def __init__(self, subject, sport):
        Academics.__init__(self, subject)
        Sports.__init__(self, sport)

    def display(self):
        print("Subject:", self.subject)
        print("Sport:", self.sport)

student1 = Student("Computer Science", "Cricket")
student1.display()




















class Camera:
    def camera_feature(self):
        print("Camera: 48MP")

class MusicPlayer:
    def music_feature(self):
        print("Music Player: MP3 Support")

class Smartphone(Camera, MusicPlayer):
    def display(self):
        self.camera_feature()
        self.music_feature()

phone = Smartphone()
phone.display()
