# Class
# Defines the School class / blueprint
class School:

    # This sets up the starting attributes of each object.
    def __init__(self, address, name, head_teacher):
        # These are attributes.
        self.address = address
        self.name = name
        self.head_teacher = head_teacher

    # This is a method. It describes the school.
    def description(self):
        print(f"{self.name} is located at {self.address} and the head teacher is {self.head_teacher}.")


# This creates a School object.
school1 = School("123 Main Street", "Greenwood High", "Mr. Smith")

# This calls the description() method.
school1.description()
