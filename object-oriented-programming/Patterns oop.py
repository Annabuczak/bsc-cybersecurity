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
