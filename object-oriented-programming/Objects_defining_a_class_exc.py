# This defines the School class.
# A class is a blueprint/template for creating school objects.
class School:
    # This is a class attribute.
    # It belongs to the class and is shared by all School objects.
    school_type = "secondary"

    # This is the __init__ method.
    # It runs automatically when a new School object is created.
    # It sets up the starting data for each object.
    def __init__(self, address, name, head_teacher, rating):
        # These are instance attributes.
        # Each School object gets its own address, name, head teacher and rating.
        self.address = address
        self.name = name
        self.head_teacher = head_teacher
        self.rating = rating

    # This is an instance method.
    # It belongs to the class and can use the object's attributes through self.
    # It prints a description of the school.
    def description(self):
        print(
            f"{self.name} is located at {self.address} "
            f"and the head teacher is {self.head_teacher}. "
            f"This is a {self.school_type} school. "
            f"This school has a {self.rating} rating."
        )


# These lines create School objects.
# school1 and school2 are objects/instances of the School class.
school1 = School("123 Main Street", "Greenwood High", "Mr. Smith", "Outstanding")
school2 = School("456 Elm Street", "Oakwood Primary", "Ms. Johnson", "Good")

# These lines call the description() method for each object.
# Python uses self to know which object's data to print.
school1.description()
school2.description()

# These lines print individual instance attributes.
# Attributes are data, so they do not use brackets.
print(school1.name)
print(school1.rating)
print(school2.name)
print(school2.rating)
