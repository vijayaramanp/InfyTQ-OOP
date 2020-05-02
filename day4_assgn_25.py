#OOPR-Assgn-25
#Start writing your code here
class FruitInfo:
    __fruit_name_list=["Apple","Guava","Orange","Grape","Sweet Lime"]
    __fruit_price_list=[200,80,70,110,60]
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            frut_indx=FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[frut_indx]
        else:
            return -1
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type
        
    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type
        
class Purchase:
    __counter=101
    
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id=None
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        
    def get_purchase_id(self):
        return self.__purchase_id
    def get_customer(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity
        
    def calculate_price(self):
        max_price=max(FruitInfo.get_fruit_price_list())
        min_price=min(FruitInfo.get_fruit_price_list())
        
        price_kg=FruitInfo.get_fruit_price(self.__fruit_name)
        if price_kg>0:
            self.__purchase_id='P'+str(Purchase.__counter)
            Purchase.__counter+=1
            bill_amount=self.__quantity*price_kg
            if price_kg==max_price and self.__quantity>1:
                    bill_amount=bill_amount - bill_amount*0.02
            elif price_kg==min_price and self.__quantity>4:
                    bill_amount=bill_amount - bill_amount*0.05   
                    
            if Customer.get_cust_type(self.__customer)=="wholesale":
                    bill_amount=bill_amount - bill_amount*0.10
                    
            return bill_amount
        else:
            return -1
        
    
c1=Customer("Tom",1)

p1=Purchase(c1,"Apple",1)
print(p1.calculate_price())
            
        
