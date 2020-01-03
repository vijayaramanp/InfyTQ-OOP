#OOPR-Assgn-3
#Start writing your code here
class Customer:
    
    def __init__(self,name,total_amt):
        self.customer_name=name
        self.bill_amt=total_amt
    
    def pays_bill(self,amt):
        print(self.customer_name," pays", amt)
    
    def purchases(self):
        self.bill_amt=self.bill_amt-(self.bill_amt*0.05)
        self.pays_bill(self.bill_amt)
        
        
c1=Customer("Vetri",20000)
c2=Customer("Raam",4555)
c1.purchases()
c2.purchases()
        
