class Car:
    def __init__(self, brand, model, year):
        # Initialize attributes
        self.brand = brand
        self.model = model
        self.year = year
        self._meter_reading = 0

    def display_info(self):
        """Displays car details."""
        print(f"{self.year} {self.brand} {self.model}")

    def accelerate(self):
        """Increases the car's speed."""
        self.speed += 5
        print(f"Accelerating... Current speed: {self.speed} mph")


class ElectricCar(Car):
    def __init__(self,brand,model,year,battery,seats,range_per_charge):
        super().__init__(brand, model, year)
        self.battery = 100
        self.seats = seats
        self.range_charge = range_per_charge

    def battery_charging(self):
        
        if self.battery <=100:
            print("battery is 100% charged ")
        else: 
            self.battery += 10
            print(f"battery charging is {self.battery}")

    def battery_discharge(self):
        if self.battery > 10:
            self.battery -= 10
            print(f"car battery is {self.battery}%")
        else:
            print(f"battery is very low {self.battery}")
        