class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        print("Setter called")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleter called")
        del self._price


p1 = Product(5000)

# 🔸 Access
print(p1.price)

# 🔸 Update
p1.price = 3000  
print(p1.price)  

# 🔸 Delete
del p1.price     
