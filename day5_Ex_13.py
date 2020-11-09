#OOPR-Exer-13
#Start writing your code here
from abc import ABCMeta, abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
        
    def get_consumer_number(self):
        return self.__consumer_number
    def get_consumer_name(self):
        return self.__consumer_name
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

    
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
        super().__init__(consumer_name)
        
    def get_base_pack_name(self):
        return self.__base_pak_name
    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if self.__base_pack_name=="Silver" or self.__base_pack_name=="Gold" or self.__base_pack_name=="Platinum":
            return True
            
        else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")
            return True
        
    def calculate_monthly_rent(self):
        if self.__subscription_period>=1 and self.__subscription_period<=24:
            if self.validate_base_pack_name() is True:
                if self.__subscription_period>12:
                    if self.__base_pack_name=="Silver":
                        discount=350
                        monthly_rent=350
                    elif self.__base_pack_name=="Gold":
                        discount=440
                        monthly_rent=440
                    elif self.__base_pack_name=="Platinum":
                        discount=560
                        monthly_rent=560
                else:
                    if self.__base_pack_name=="Silver":
                        discount=0 
                        monthly_rent=350
                    elif self.__base_pack_name=="Gold":
                        discount=0 
                        monthly_rent=440
                    elif self.__base_pack_name=="Platinum":
                        discount=0 
                        monthly_rent=560 
                final_monthly_rent=((monthly_rent*self.__subscription_period)-discount)/self.__subscription_period
                return final_monthly_rent
            else:
                return -1
        else:
            return -1
            
obj1=BasePackage("Vetri","Platinum",4,)
res=obj1.calculate_monthly_rent()
print(res)
