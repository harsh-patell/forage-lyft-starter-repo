from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        sum = 0
        for value in self.tire_wear:
            sum += value
        return sum >= 3