# Animal Rescue Centre

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


animal_1 = Animal("Buddy", 1)
animal_1.show_info()
animal_2 = Animal("PussyCat", 2)
animal_2.show_info()


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_info(self):
        print(self.name, self.age, self.breed)


class Cat(Animal):
    def __init__(self, name, age, breed, indoor=True):
        super().__init__(name, age)
        self.breed = breed
        self.ido = indoor

    def show_info(self):
        print(self.name, self.age, self.breed)


Dog_1 = Dog("Buddy", 1, "KCS")
Cat_1 = Cat("Pussycat", 2, "Main")
Dog_1.show_info()
Cat_1.show_info()

print(f'My dog name is {Dog_1.name}, he is {Dog_1.age} years old and he is a  {Dog_1.breed}')
print(
    f'My neighbours cat name is {Cat_1.name} he is {Cat_1.age} years old and he is a  {Cat_1.breed} he is indoor only cat{Cat_1.ido}')


# Home Appliance Energy Cost Tracker

class Appliance:
    def __init__(self, cost_per_hour):
        self.cost_per_hour = cost_per_hour

    def calculate_cost(self):
        return self.cost_per_hour


class Lamp(Appliance):
    def calculate_cost(self):
        return super().calculate_cost()


class WashingMachine(Appliance):
    def __init__(self, cost_per_hour, fixed_charge):
        super().__init__(cost_per_hour)
        self.fixed_charge = fixed_charge

    def calculate_cost(self):
        return self.fixed_charge + super().calculate_cost()


cost_per_hour = 12
fixed_charge = 2

app = Appliance(cost_per_hour)
app_1 = WashingMachine(12.0, 2)
app_2 = Lamp(1)

print(f"Standard cost of running appliance is {app.calculate_cost()}")
print(f"Cost of running washing machine is {app_1.calculate_cost()}")
print(f"Cost of running lamp is {app_2.calculate_cost()}")

# Smart Home Alerts
