
from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        for value in self.tire_wear:
            if value >= 0.9:
                return True
        return False