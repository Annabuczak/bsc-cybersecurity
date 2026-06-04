class Employee:
    company = "THM"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} earns {self.salary} per year.")


class Driver(Employee):
    def __init__(self, name, salary, vehicle_type):
        super().__init__(name, salary)
        self.vehicle_type = vehicle_type

    def show_details(self):
        print(f"{self.name} earns {self.salary} per year and drives a {self.vehicle_type}.")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        print(f"{self.name} earns {self.salary} per year and codes in {self.programming_language}.")


driver = Driver("Anna", 14500, "car")
driver.show_details()

developer = Developer("Lou", 25000, "Python")
developer.show_details()

print(driver.company)
print(developer.company)
