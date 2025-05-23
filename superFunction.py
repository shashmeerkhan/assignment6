class Person:
    def __init__(self, name):
        self.name=name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject

p1=Person("Ahmed")
t1=Teacher("Saad","english")
print(p1.name)
print(t1.subject,t1.name)
