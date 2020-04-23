#OOPR-Assgn-24
#Start writing your code here
class Apparel:
    counter=100
    def __init__(self,price,item_type):
        Apparel.counter+=1
        self.__item_type=item_type
        self.__price=price
        self.__item_id=item_type[0]+str(Apparel.counter)

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price
    def get_item_id(self):
        return self.__item_id
    def get_item_type(self):
        return self.__item_type
    
    def calculate_price(self):
        self.__price=self.__price + (self.__price*0.05)
    
class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price,"Cotton")
        self.__discount=discount
        
    def get_discount(self):
        return self.__discount
    
    def calculate_price(self):
        super().calculate_price()
        price=self.get_price()
        price=price-(price*self.__discount/100)
        price=price+(price*0.05)
        self.set_price(price)
        
class Silk(Apparel):
    def __init__(self,price):
        self.__points=0 
        super().__init__(price,"Silk")
    
    def get_points(self):
        return self.__points
        
    def calculate_price(self):
        super().calculate_price()
        price=self.get_price()
        if price > 10000:
            self.__points=10
        else:
            self.__points=3
        price=price+price*0.1
        self.set_price(price)
    
c1=Cotton(8000,2)
s1=Silk(1000)
c1.calculate_price()
print(c1.get_price(),c1.get_item_type(),c1.get_item_id(),c1.get_discount())
