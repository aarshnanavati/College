# Design a SmartDevice class that inherits from both Phone and Camera. Handle method name clashes using method resolution order.

class Phone:
    def power_on(self):
        print("Phone is Powering on..")

    def feature(self):
        print("Can make calls")

class Camera:
    def power_on(self):
        print("Camera is Powering on..")
    def feature(self):
        print("Can take pictures")

class SmartDevice(Phone,Camera):
    def power_on(self):
        print("Smartdevice is Powering on..")
        super().power_on()

    def show_features(self):
        super().feature()
        Camera.feature(self)

if __name__ == "__main__":
    device = SmartDevice()
    device.power_on()
    device.show_features()

    print("\n MRO: ",SmartDevice.__mro__) 