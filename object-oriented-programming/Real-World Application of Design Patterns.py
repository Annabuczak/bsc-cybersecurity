# SmartHome Inc software

class DeviceManager:
    _instance = None

    def __new__(cls, display, manage):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.display = display
            cls._instance.manage = manage
        return cls._instance


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class MobileAlert:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Mobile alert for {self.name}: {message}")


class EmailAlert:
    def __init__(self, email):
        self.email = email

    def update(self, message):
        print(f"Email alert to {self.email}: {message}")


class SmartLight(Subject):
    def __init__(self):
        super().__init__()
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is now ON")
        self.notify("Light is now ON")

    def turn_off(self):
        self.is_on = False
        print("Light is now OFF")
        self.notify("Light is now OFF")


class SmartLightDecorator:
    def __init__(self, smart_light):
        self.smart_light = smart_light

    def turn_on(self):
        print("Smart light log: turning on")
        self.smart_light.turn_on()

    def turn_off(self):
        self.smart_light.turn_off()
        print("Smart light log: turned off")


class RingDoor(Subject):
    def __init__(self):
        super().__init__()
        self.is_recording = False

    def record(self):
        self.is_recording = True
        print("Recording video from Ring Door")
        self.notify("Ring Door started recording")

    def turn_off(self):
        self.is_recording = False
        print("Recording has stopped")
        self.notify("Ring Door stopped recording")


class RingDoorDecorator:
    def __init__(self, ring_door):
        self.ring_door = ring_door

    def record(self):
        print("Security log: Ring Door recording started")
        self.ring_door.record()

    def turn_off(self):
        self.ring_door.turn_off()
        print("Security log: Ring Door recording stopped")


class RingDoorAdapter:
    def __init__(self, door_bell):
        self.door_bell = door_bell

    def turn_on(self):
        self.door_bell.record()


class VacuumRobot(Subject):
    def __init__(self):
        super().__init__()

    def start_cleaning(self):
        print("Starting cleaning")
        self.notify("Vacuum Robot started cleaning")

    def recharge(self):
        print("Recharging vacuum robot")
        self.notify("Vacuum Robot is recharging")


class VacuumRobotDecorator:
    def __init__(self, vacuum_robot):
        self.vacuum_robot = vacuum_robot

    def start_cleaning(self):
        self.vacuum_robot.start_cleaning()
        print("Cleaning in progress...")

    def recharge(self):
        print("Cleaning stopped.")
        self.vacuum_robot.recharge()


class VacuumRobotAdapter:
    def __init__(self, vacuum_robot):
        self.vacuum_robot = vacuum_robot

    def turn_on(self):
        self.vacuum_robot.start_cleaning()


class Thermostat(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 20

    def check_temperature(self):
        print(f"Current temperature is {self.temperature}C")
        self.notify(f"Thermostat temperature is {self.temperature}C")

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature changed to {self.temperature}C")
        self.notify(f"Thermostat temperature changed to {self.temperature}C")

    def eco_mode(self):
        print("Eco mode enabled")
        self.notify("Thermostat eco mode is ON")


class ThermostatDecorator:
    def __init__(self, thermostat):
        self.thermostat = thermostat

    def check_temperature(self):
        self.thermostat.check_temperature()
        print("Temperature checked successfully")

    def set_temperature(self, temperature):
        self.thermostat.set_temperature(temperature)

    def eco_mode(self):
        print("Saving energy...")
        self.thermostat.eco_mode()


class ThermostatAdapter:
    def __init__(self, thermostat):
        self.thermostat = thermostat

    def turn_on(self):
        self.thermostat.check_temperature()


class EnergySavingStrategy:
    def save_energy(self):
        pass


class EcoStrategy(EnergySavingStrategy):
    def save_energy(self):
        print("Eco strategy: lowering thermostat and reducing device power usage")


class NightStrategy(EnergySavingStrategy):
    def save_energy(self):
        print("Night strategy: turning off lights and reducing camera activity")


class AwayFromHomeStrategy(EnergySavingStrategy):
    def save_energy(self):
        print("Away strategy: turning off non-essential devices and enabling security mode")


class EnergyManager:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def manage_energy(self):
        self.strategy.save_energy()


device_manager = DeviceManager("Display Device Manager", "Manage Device Manager")

print(device_manager.display)
print(device_manager.manage)

mobile_alert = MobileAlert("Anna")
email_alert = EmailAlert("anna@email.com")

smart_light = SmartLight()
smart_light.attach(mobile_alert)
smart_light.attach(email_alert)
smart_light = SmartLightDecorator(smart_light)

smart_light.turn_on()
smart_light.turn_off()

ring_door = RingDoor()
ring_door.attach(mobile_alert)
ring_door.attach(email_alert)
ring_door = RingDoorDecorator(ring_door)

ring_door_adapter = RingDoorAdapter(ring_door)
ring_door_adapter.turn_on()
ring_door.turn_off()

vacuum_robot = VacuumRobot()
vacuum_robot.attach(mobile_alert)
vacuum_robot.attach(email_alert)
vacuum_robot = VacuumRobotDecorator(vacuum_robot)

vacuum_robot_adapter = VacuumRobotAdapter(vacuum_robot)
vacuum_robot_adapter.turn_on()
vacuum_robot.recharge()

thermostat = Thermostat()
thermostat.attach(mobile_alert)
thermostat.attach(email_alert)
thermostat = ThermostatDecorator(thermostat)

thermostat_adapter = ThermostatAdapter(thermostat)
thermostat_adapter.turn_on()
thermostat.set_temperature(22)
thermostat.eco_mode()

energy_manager = EnergyManager(EcoStrategy())
energy_manager.manage_energy()

energy_manager.set_strategy(NightStrategy())
energy_manager.manage_energy()

energy_manager.set_strategy(AwayFromHomeStrategy())
energy_manager.manage_energy()
