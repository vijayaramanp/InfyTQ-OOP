#OOPR-Assgn-16

class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phone_no,called_no,duration):
        self.phone_no=phone_no
        self.called_no=called_no
        self.duration=duration

class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects=[]
        
    def parse_customer(self,list_of_customers,list_of_calls):
        for customer in list_of_customers:
            tmp=[]
            for call in list_of_calls:
                if customer.phone_no==call.phone_no:
                    tmp.append(call)
            customer.list_of_calls=tmp
            self.list_of_customer_calldetail_objects.append(customer)
        

cust1=Customer(9900009901,'cust1',23)
list_of_customers=[cust1]

call1=CallDetail(9900009901,8800123401,5)
list_of_calls=[call1]

Util().parse_customer(list_of_customers, list_of_calls)
