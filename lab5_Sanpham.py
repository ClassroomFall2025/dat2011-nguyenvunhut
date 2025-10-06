#class bài 2
class Product:
    def __init__(self):
        pass

    def nhap(self):
        self.name = input("Enter product name: ")
        self.price = float(input("Enter product price: "))
        self.discount = float(input("Enter product's discount: "))

    def import_tax(self):
        return self.price * 0.1

    def xuat(self):
        print(f"Name: {self.name}, Price: {self.price}, Discount: {self.discount}, Import Tax: {self.import_tax()}")

#class bài 3
class ProductProtected:
    def __init__(self):
        pass

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_discount(self):
        return self.__discount

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def set_discount(self, discount):
        if discount < 0:
            raise ValueError("Discount cannot be negative")
        self.__discount = discount

    def import_tax(self):
        return self.__price * 0.1

    def nhap(self):
        self.__name = input("Enter product name: ")
        self.set_price(float(input("Enter product price: "))) 
        self.set_discount(float(input("Enter product's discount: "))) 

    def xuat(self):
        print(f"Name: {self.__name}, Price: {self.__price}, Discount: {self.__discount}, Import Tax: {self.import_tax():.2f}")

#class bài4
class ProductWithInit:
    def __init__(self, _name, _price, _discount):
        self.__name = _name
        self.__price = _price
        self.__discount = _discount

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_discount(self):
        return self.__discount

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def set_discount(self, discount):
        if discount < 0:
            raise ValueError("Discount cannot be negative")
        self.__discount = discount

    def import_tax(self):
        return self.__price * 0.1

    def xuat(self):
        print(f"Name: {self.__name}, Price: {self.__price}, Discount: {self.__discount}, Import Tax: {self.import_tax():.2f}")
