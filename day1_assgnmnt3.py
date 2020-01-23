#OOPR-Assgn-3
#Start writing your code here
class Customer:
    
    def __init__(self):
        self.customer_name=None
        self.bill_amount=0
    
    def pays_bill(self,amount):
        print(self.customer_name," pays", amount)
    
    def purchases(self):
        discount=self.bill_amount*0.05
        final_amount=self.bill_amount-discount
        self.pays_bill(final_amount)
        
c1=Customer()
c2=Customer()
c1.purchases()
c2.purchases()
