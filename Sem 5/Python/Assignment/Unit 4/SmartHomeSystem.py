# . Write a Python application that simulates a smart home system. Create classes for different devices 
# such as Light, Fan, and Thermostat. Implement inheritance to handle device types and raise exceptions
# for invalid operations (e.g., setting negative temperature).

# ------------------ Base Class ------------------
class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"{self.name} is currently {state}.")


# ------------------ Derived Class: Light ------------------
class Light(Device):
    def __init__(self, name, brightness=0):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.brightness = value
        print(f"{self.name} brightness set to {self.brightness}%.")


# ------------------ Derived Class: Fan ------------------
class Fan(Device):
    def __init__(self, name, speed=0):
        super().__init__(name)
        self.speed = speed

    def set_speed(self, value):
        if not 0 <= value <= 5:
            raise ValueError("Fan speed must be between 0 and 5.")
        self.speed = value
        print(f"{self.name} speed set to {self.speed}.")


# ------------------ Derived Class: Thermostat ------------------
class Thermostat(Device):
    def __init__(self, name, temperature=25):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, temp):
        if temp < 0:
            raise ValueError("Temperature cannot be negative!")
        self.temperature = temp
        print(f"{self.name} temperature set to {self.temperature}°C.")


# ------------------ Main Program ------------------
def main():
    print("===== Smart Home System =====")
    light = Light("Living Room Light")
    fan = Fan("Ceiling Fan")
    thermostat = Thermostat("Home Thermostat")

    while True:
        print("\n1. Turn On Light")
        print("2. Turn Off Light")
        print("3. Set Light Brightness")
        print("4. Turn On Fan")
        print("5. Turn Off Fan")
        print("6. Set Fan Speed")
        print("7. Turn On Thermostat")
        print("8. Turn Off Thermostat")
        print("9. Set Thermostat Temperature")
        print("10. Show Device Status")
        print("11. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                light.turn_on()
            elif choice == '2':
                light.turn_off()
            elif choice == '3':
                value = int(input("Enter brightness (0-100): "))
                light.set_brightness(value)
            elif choice == '4':
                fan.turn_on()
            elif choice == '5':
                fan.turn_off()
            elif choice == '6':
                value = int(input("Enter fan speed (0-5): "))
                fan.set_speed(value)
            elif choice == '7':
                thermostat.turn_on()
            elif choice == '8':
                thermostat.turn_off()
            elif choice == '9':
                temp = float(input("Enter temperature (°C): "))
                thermostat.set_temperature(temp)
            elif choice == '10':
                print()
                light.status()
                fan.status()
                thermostat.status()
            elif choice == '11':
                print("👋 Exiting Smart Home System...")
                break
            else:
                print("❌ Invalid choice! Try again.")

        except ValueError as e:
            print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()
