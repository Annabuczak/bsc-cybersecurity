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
