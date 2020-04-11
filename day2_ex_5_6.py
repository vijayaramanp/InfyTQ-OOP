#OOPR-Exer-6
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.mileage=None
        self.fuel_left=None

    def identify_distance_travelled(self,initial_fuel):
        distance_travelled=(initial_fuel-self.fuel_left)*self.mileage
        return distance_travelled
        
    def identify_distance_that_can_be_travelled(self):
        initial_fuel=20
        distance_travelled=self.identify_distance_travelled(initial_fuel)
        if self.fuel_left > 5:
            return (initial_fuel-5)*self.mileage - distance_travelled
            
        else:
            return 0
        
v1=Vehicle()
v1.mileage=10
v1.fuel_left=10
print(v1.identify_distance_that_can_be_travelled())
