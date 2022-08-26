
from car.car import Car

from engine.CapuletEngine import CapuletEngine
from engine.StermmanEngine import StemmanEngine
from engine.WilloughbyEngine import WilloughbyEngine

from battery.SpinderBattery import SplinderBattery
from battery.NubbinBattery import NubbinBattery

from tire.Carrigan import CarriganTire
from tire.Octoprime import OctoprimeTire

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)
    
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        engine = StemmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)
    
    def create_rorscharch(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)