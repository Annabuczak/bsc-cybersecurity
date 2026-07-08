# SmartHome Inc software

class DeviceManager:
    _instance = None

    def __new__(cls, display, manage):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.display = display
            cls._instance.manage = manage

        return cls._instance


class SmartLight:
    def turn_on(self):
        print("Light is now ON")


class RingDoor:
    def record(self):
        print("Recording video from Ring Door")


class RingDoorAdapter:
    def __init__(self, door_bell):
        self.door_bell = door_bell

    def turn_on(self):
        self.door_bell.record()


class VacuumRobot:
    def start_cleaning(self):
        print("Starting cleaning")


class VacuumRobotAdapter:
    def __init__(self, vacuum_robot):
        self.vacuum_robot = vacuum_robot

    def turn_on(self):
        self.vacuum_robot.start_cleaning()


class Thermostat:
    def check_temperature(self):
        print("Check current temperature")


class ThermostatAdapter:
    def __init__(self, thermostat):
        self.thermostat = thermostat

    def turn_on(self):
        self.thermostat.check_temperature()


device_manager = DeviceManager("Display Device Manager", "Manage Device Manager")

print(device_manager.display)
print(device_manager.manage)

smart_light = SmartLight()
smart_light.turn_on()

ring_door = RingDoor()
adapter = RingDoorAdapter(ring_door)
adapter.turn_on()

vacuum_robot = VacuumRobot()
adapter = VacuumRobotAdapter(vacuum_robot)
adapter.turn_on()

thermostat = Thermostat()
thermostat.check_temperature()
adapter.turn_on()


class ActivateDevice:
    active = True

    def __init__(self, device):
        self.device = device
        if device:
            self.active = True
            print(self.device)
        else:
            self.device = None
            self.active = False
