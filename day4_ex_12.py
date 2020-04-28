#OOPR-Exer-12
#Start writing your code here
class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status=trained_status
        self.__experience=experience
        
    def rides_vehicle(self):
        pass
    
class CycleRider(Rider):
    def rides_blindfolded(self):
        print("Rides blind folded")
        
    
class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(trained_status,experience)
        self.__race_license=race_license
    
    def rides_in_dome(self):
        print("Rides in Dome")
        
b1=BikeRider(True,True,4)
