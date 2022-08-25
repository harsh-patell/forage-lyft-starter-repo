
from car.car import Car

from engine.engine import Engine
from engine.CapuletEngine import CapuletEngine
from engine.StermmanEngine import StemmanEngine
from engine.WilloughbyEngine import WilloughbyEngine

from battery.battery import Battery
from battery.SpinderBattery import SplinderBattery
from battery.NubbinBattery import NubbinBattery


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = StemmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorscharch(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)