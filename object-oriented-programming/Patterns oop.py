# Singleton

class Config:
    _instance = None

    def __new__(cls, db_url, debug):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_url = db_url
            cls._instance.debug = debug
        return cls._instance


config1 = Config("postgresql://localhost:5432/mydb", True)
config2 = Config("mysql://localhost:3306/otherdb", False)

print(config1.db_url)
print(config1.debug)

print(config2.db_url)
print(config2.debug)

print(config1 is config2)


class Config:
    _instance = None

    def __new__(cls, db_url, debug):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_url, debug):
        self.db_url = db_url
        self.debug = debug


config1 = Config("postgresql://localhost:5432/mydb", True)
config2 = Config("mysql://localhost:3306/otherdb", False)

print(config1.db_url)
print(config1.debug)

print(config2.db_url)
print(config2.debug)

print(config1 is config2)
print(id(config1))
print(id(config2))


class WaitingRoomDisplay:
    _instance = None

    def __new__(cls, display, queue):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, display, queue):
        if hasattr(self, "_initialized"):
            return

        self.display = display
        self.queue = queue
        self._initialized = True

    def next_patient(self):
        print(self.display)
        print(f"Queue number: {self.queue[0]}")


display1 = WaitingRoomDisplay("Buddy is next in the queue", [1])
display2 = WaitingRoomDisplay("Cruella is next in the queue", [2])

display1.next_patient()

print(display1 is display2)
print(display1.display)
print(display2.display)
print(display1.queue)
print(display2.queue)


class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls.singleton = super(OneOnly, cls).__new__(cls)
        return cls._singleton


a1 = OneOnly()
a2 = OneOnly()
print(a1 is a2)


# Factory
class DogToy:
    def __init__(self, name):
        self.name = name


class DogToyFactory:
    def create_toy(self, toy_name):
        if toy_name == "ball":
            return DogToy("Green Ball")
        elif toy_name == "licky mat":
            return DogToy("Blue Licky Mat")
        elif toy_name == "rope":
            return DogToy("Cotton Rope")
        else:
            return None


factory = DogToyFactory()

toy = factory.create_toy("ball")

toy1 = factory.create_toy("ball")
toy2 = factory.create_toy("licky mat")
toy3 = factory.create_toy("rope")

print(toy1.name)
print(toy2.name)
print(toy3.name)


# Factory

class Notification:
    def send(self, message):
        raise NotImplementedError("Subclasses must implement send()")


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")


class NotificationFactory:
    @classmethod
    def create_notification(cls, type_name):
        if type_name == "email":
            return EmailNotification()
        elif type_name == "sms":
            return SMSNotification()
        else:
            raise ValueError("Invalid notification type")


email_notification = NotificationFactory.create_notification("email")
sms_notification = NotificationFactory.create_notification("sms")

email_notification.send("Hello, this is an email notification!")
sms_notification.send("Hello, this is an SMS notification!")


# adapter
class CiscoFirewall:
    def transmit(self, packet):
        print(f"Transmitting packet: {packet}")


class FirewallAdapter:
    def __init__(self, firewall):
        self.firewall = firewall

    def send_data(self, packet):
        self.firewall.transmit(packet)


firewall = CiscoFirewall()
adapter = FirewallAdapter(firewall)
adapter.send_data("Packet")


class SmartLight:
    def turn_on(self, ):
        print("Light is now ON")


class SmartSpeaker:
    def power_up(self):
        print("Speaker is now ON")


class SmartSpeakerAdapter:
    def __init__(self, speaker):
        self.speaker = speaker

    def turn_on(self):
        self.speaker.power_up()


speaker = SmartSpeaker()
adapter = SmartSpeakerAdapter(speaker)
adapter.turn_on()


class OldPrinter:
    def output(self, document):
        print(f"Printing: {document}")


class PrinterAdapter:

    def __init__(self, printer):
        self.printer = printer

    def print_document(self, document):
        self.printer.output(document)


printer = OldPrinter()
adapter = PrinterAdapter(printer)
adapter.print_document("Hello")

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class ThirdPartyPayment:
    def make_transaction(self, value):
        print(f"Third-party processing payment of {value}")


class ThirdPartyPaymentAdapter(PaymentProcessor):
    def __init__(self, third_party):
        self.third_party_payment = third_party

    def process_payment(self, amount):
        self.third_party_payment.make_transaction(amount)


third_party_payment = ThirdPartyPayment()
adapter = ThirdPartyPaymentAdapter(third_party_payment)

adapter.process_payment(100)


# Decorator
class Pizza:
    def get_cost(self):
        return 10.0


class PizzaDecorator(Pizza):

    def __init__(self, pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()


class CheeseDecorator(PizzaDecorator):
    def __init__(self, cheese):
        super().__init__(pizza)

    def get_cost(self):
        return self.pizza.get_cost() + 2.0


class OliveDecorator(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_cost(self):
        return self.pizza.get_cost() + 1.0


pizza = Pizza()
pizza = CheeseDecorator(pizza)
pizza = OliveDecorator(pizza)
print(f"Pizza is {pizza.get_cost()}")


class IceCream:
    def get_cost(self):
        return 5.0


class IceCreamDecorator(IceCream):
    def __init__(self, ice_cream):
        self.ice_cream = ice_cream

    def get_cost(self):
        return self.ice_cream.get_cost()


class SprinklesDecorator(IceCreamDecorator):
    def __init__(self, ice_cream):
        super().__init__(ice_cream)

    def get_cost(self):
        return self.ice_cream.get_cost() + 1.0


class ChocolateSauceDecorator(IceCreamDecorator):
    def __init__(self, ice_cream):
        super().__init__(ice_cream)

    def get_cost(self):
        return self.ice_cream.get_cost() + 1.5


ice_cream = IceCream()
ice_cream = ChocolateSauceDecorator(ice_cream)
ice_cream = ChocolateSauceDecorator(ice_cream)
print(f"Ice Cream is {ice_cream.get_cost()}")


class DataService:
    def get_data(self):
        return "Important data"


class LoggingDataServiceDecorator:
    def __init__(self, data_service):
        self.data_service = data_service

    def get_data(self):
        print("LOG: about to fetch data")
        return self.data_service.get_data()


data_service = DataService()
logged_service = LoggingDataServiceDecorator(data_service)

print(logged_service.get_data())
