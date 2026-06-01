# Class
# Defines the School class / blueprint
class School:
    school_type = "secondary"  # This is a class attribute. It is shared by all objects of the class.

    # This sets up the starting attributes of each object.
    def __init__(self, address, name, head_teacher, school_type, rating):
        # These are attributes.
        self.address = address
        self.name = name
        self.head_teacher = head_teacher
        self.rating = rating

    # This is a method. It describes the school.
    def description(self):
        print(
            f"{self.name} is located at {self.address} and the head teacher is {self.head_teacher}. This is {self.school_type} school. This schhol is {self.rating} rating.")


# This creates a School object.
school1 = School("123 Main Street", "Greenwood High", "Mr. Smith", "secondary", rating="Outstanding")
school2 = School("456 Elm Street", "Oakwood Primary", "Ms. Johnson", "secondary", rating="Good")
# This calls the description() method.
school1.description()
school2.description()
school1.rating = "Outstanding"
school2.rating = "Good"

print(school1.name)
print(school1.rating)
print(school2.name)
print(school2.rating)
