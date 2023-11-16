# component.py
class Component:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.available = quantity

    def checkout(self):
        if self.available > 0:
            self.available -= 1
            return True
        else:
            print(f"No available {self.name} to check out.")
            return False

    def return_component(self):
        if self.available < self.quantity:
            self.available += 1
            return True
        else:
            print(f"All {self.name} are already available.")
            return False
# sensor.py
from component import Component

class Sensor(Component):
    def __init__(self, name, quantity, sensor_type):
        super().__init__(name, quantity)
        self.sensor_type = sensor_type
# main.py
from component import Component
from sensor import Sensor

# Creating instances
temperature_sensor = Sensor("Temperature Sensor", 5, "Analog")
# cli.py
from component import Component
from sensor import Sensor

def main():
    temperature_sensor = Sensor("Temperature Sensor", 5, "Analog")

    # Example: Checking out a component
    if temperature_sensor.checkout():
        print(f"{temperature_sensor.name} checked out successfully.")
    else:
        print("Checkout failed.")

    # Example: Returning a component
    if temperature_sensor.return_component():
        print(f"{temperature_sensor.name} returned successfully.")
    else:
        print("Return failed.")

if __name__ == "__main__":
    main()
