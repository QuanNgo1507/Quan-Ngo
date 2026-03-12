class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print(f"Loi gia cua '{self.name}'phai lon hon 0 (Dang thu gan: {value})")
            self._price = 0
    def __str__(self):
        return f"San Pham:{self.name}/Gia: {self.price}"
p1 = Product("Pepsi", 15000)
print(p1)
p1.price = -500
print(p1)
p2 = Product("Coca", -10000)
print(p2)