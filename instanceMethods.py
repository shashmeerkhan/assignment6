class Dog:
    def __init__(self,name, breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} is barking")

d1=Dog("BullDog","xyz")
print(d1.bark())
       