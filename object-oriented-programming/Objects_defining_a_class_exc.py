import gc


# This defines the School class.
# A class is a blueprint/template for creating school objects.
class School:
    # This is a class attribute.
    # It belongs to the class and is shared by all School objects.
    school_type = "secondary"

    # This is the __init__ method.
    # It runs automatically when a new School object is created.
    # __init__ is the constructor. It sets up the object with initial data.
    def __init__(self, address, name, head_teacher, rating):
        # These are instance attributes.
        # Each School object gets its own address, name, head teacher and rating.
        self.address = address
        self.name = name
        self.head_teacher = head_teacher
        self.rating = rating

    # This is the destructor.
    # It may run when the object is destroyed.
    def __del__(self):
        print(f"{self.name} has been destroyed")

    # This is an instance method.
    # It belongs to the class and can use the object's attributes through self.
    def description(self):
        print(
            f"{self.name} is located at {self.address} "
            f"and the head teacher is {self.head_teacher}. "
            f"This is a {self.school_type} school. "
            f"This school has a {self.rating} rating."
        )


# These lines create School objects.
school1 = School("123 Main Street", "Greenwood High", "Mr. Smith", "Outstanding")
school2 = School("456 Elm Street", "Oakwood Primary", "Ms. Johnson", "Good")

# These lines call the description() method for each object.
school1.description()
school2.description()

# These lines print individual instance attributes.
print(school1.name)
print(school1.rating)
print(school2.name)
print(school2.rating)

# This deletes the reference to school1.
# If no other references point to that object, Python may destroy it.
del school1

# This asks Python to run garbage collection.
gc.collect()
