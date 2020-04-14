#OOPR-Assgn-18
#Start writing your code here

    
class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity
    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__descriprion
    def get_price_per_quantity(self):
        return self.__price_per_quantity
        
class Customer:
    def __init__(self, customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None
        
    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.__payment_status
    
    def pays_bill(self,bill):
        self.__payment_status="Paid"
        print(self.__customer_name, bill.get_bill_id(),bill.get_bill_amount())
        
    
class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id=None
        self.__bill_amount=0
    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount
    
    def generate_bill_amount(self, item_quantity,items):
        Bill.counter+=1 
        self.__bill_id='B'+str(Bill.counter)
        for key,value in item_quantity.items():
            for item in items:
                if key.upper()==item.get_item_id().upper():
                    self.__bill_amount+=value*item.get_price_per_quantity()
                    break
                

item_quantity={'IR658':4, 'Ir987':3, 'IR123':2}
items=[Item('IR987','Rice',100.0), Item('ir658','Wheat',151.0),Item('Ir346','Banana',35.75)]

bill1=Bill()
bill1.generate_bill_amount(item_quantity,items)

cust1=Customer("Vetri")
cust1.pays_bill(bill1)
