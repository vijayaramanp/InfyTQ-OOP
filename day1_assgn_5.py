#OOPR-Assgn-5
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None 
        self.__vehicle_type=None  
        self.__vehicle_cost=None 
        self.__premium_amount=None 
    
    def set_vehicle_id(self,val):
        self.__vehicle_id=val
    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def set_vehicle_type(self,val):
        self.__vehicle_type=val 
    def get_vehicle_type(self):
        return self.__vehicle_type
        
    def set_vehicle_cost(self,val):
        self.__vehicle_cost=val 
    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    def set_premium_amount(self,val):
        self.__premium_amount=val 
    def get_premium_amount(self):
        return self.__premium_amount
    
    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            tmp=self.get_vehicle_cost()*0.02
            return tmp
        elif self.__vehicle_type=="Four Wheeler":
            tmp=self.get_vehicle_cost()*0.05
            return tmp
        else:
            return 1
    
    def display_vehicle_details(self):
        tmp=self.calculate_premium()
        if tmp!=1:
            self.set_premium_amount(tmp)
            print("Vehicle details")
            print("Vehicle ID:",self.get_vehicle_id(), "\nVehicle Type:",self.get_vehicle_type(), "\nVehicle Cost:", self.get_vehicle_cost(), "\nPremium amount", self.get_premium_amount())
        else:
            print("Invalid Vehicle Type")
        
v1=Vehicle()
v1.set_vehicle_id(1111)
v1.set_vehicle_type("Three Wheeler")
v1.set_vehicle_cost(105000)
v1.display_vehicle_details()
