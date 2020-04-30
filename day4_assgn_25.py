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
        self.__purchase_id='P'+str(Purchase.__counter)
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        Purchase.__counter+=1 
        
    
    def get_purchase_id(self):
        return self.__purchase_id
    def get_customer(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity
        
    def calculate_price(self):
        fruit_name_list=FruitInfo.get_fruit_name_list()
        max_price=max(FruitInfo.get_fruit_price_list())
        min_price=min(FruitInfo.get_fruit_price_list())
        
        if self.__fruit_name in fruit_name_list:
            price_kg=FruitInfo.get_fruit_price(self.__fruit_name)
            bill_amount=self.__quantity*price_kg
            if self.__customer.get_cust_type()=="wholesale":
                if price_kg==max_price:
                    if self.__quantity>1:
                        bill_amount=bill_amount - bill_amount*0.02
                        bill_amount=bill_amount - bill_amount*0.10
                    else:
                        bill_amount=bill_amount - bill_amount*0.10 
                        
                elif price_kg==min_price:
                    if self.quantity>4:
                        bill_amount=bill_amount - bill_amount*0.05
                        bill_amount=bill_amount - bill_amount*0.10
                    else:
                        bill_amount=bill_amount - bill_amount*0.10
                else:
                    bill_amount=bill_amount - bill_amount*0.10
                    
            elif self.__customer.get_cust_type()=="Retailer":
                if price_kg==max_price and self.__quantity>1:
                    bill_amount=bill_amount - bill_amount*0.02
                elif price_kg==min_price and self.__quantity>4:
                    bill_amount=bill_amount - bill_amount*0.10
                    
            return bill_amount
        else:
            return -1
        
    
c1=Customer("Tom",1)

p1=Purchase(c1,"Apple",1)
print(p1.calculate_price())
            
        
