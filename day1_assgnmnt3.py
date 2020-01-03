#OOPR-Assgn-3
#Start writing your code here
class Customer:
    
    def __init__(self,name,total_amount):
        self.customer_name=name
        self.bill_amount=total_amount
    
    def pays_bill(self,amount):
        print(self.customer_name," pays", amount)
    
    def purchases(self):
        discount=self.bill_amount*0.05
        final_amount=self.bill_amount-discount
        self.pays_bill(final_amount)
        
c1=Customer("Vetri",20000)
c2=Customer("Raam",4555)
c1.purchases()
c2.purchases()
