from datetime import date, datetime
from unicodedata import name

class Product():
    def __init__(self, id, name, price):
        self.id= id
        self.name=name
        self.price= price
        self.price_history= {date: date.today(), price: price}
    
    def update_price(self, new_price):
        self.price= new_price
 

class User():
    def __init__(self, id, user_name, balance):    #el balance es el "dinero" que tiene 
        self.id=id
        self.u_name= user_name
        self.balance=balance
        self.order_list=[]
        self.compras=[]
    
    def add_product_to_car(self, products):
        for a in range (len(products)):
            self.compras.append(products[a])
        
    


class Order():
    def __init__(self, id, date, total, status):
        self.id=id
        self.date=date
        self.total=total
        self.status=status

##########################################

product1= Product(1, "Carne", 20000)
product2= Product(2, "Huevo", 500)
product3= Product(3, "Pan", 200)

print(product1.name)
print(product2.price_history)
product1.update_price(4)
print(product1.price)



############################################

user1= User(101, "pipe", 20000)
user2= User(101, "juli", 40000)
user3= User(101, "samu", 60000)


user1.add_product_to_car([product1])


