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
    def __init__(self, address, name, head_teacher, rating, students):
        # These are instance attributes.
        # Each School object gets its own address, name, head teacher, rating and students.
        self.address = address
        self.name = name
        self.head_teacher = head_teacher
        self.rating = rating
        self.students = students

    # This is the destructor.
    # It may run when the object is destroyed.
    def __del__(self):
        print(f"{self.name} has been destroyed")

    # This is the __len__ built-in method.
    # It lets us use len(school1).
    # It returns the number of students in this school object.
    def __len__(self):
        return len(self.students)

    # This is the __eq__ built-in method.
    # It lets us compare two School objects using ==.
    # The word other means the second object we are comparing with.
    def __eq__(self, other):
        return self.name == other.name

    # This is the __str__ built-in method.
    # It controls what appears when we print the whole object.
    def __str__(self):
        return (
            f"{self.name} is located at {self.address}. "
            f"The head teacher is {self.head_teacher}. "
            f"This is a {self.school_type} school. "
            f"This school has a {self.rating} rating."
        )

    # This is the __repr__ built-in method.
    # It gives a more technical/developer-style version of the object.
    def __repr__(self):
        return (
            f"School(name='{self.name}', address='{self.address}', "
            f"head_teacher='{self.head_teacher}', rating='{self.rating}')"
        )

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
# school1 and school2 are objects/instances of the School class.
school1 = School(
    "123 Main Street",
    "Greenwood High",
    "Mr. Smith",
    "Outstanding",
    ["Anna", "Louie", "John"]
)

school2 = School(
    "456 Elm Street",
    "Oakwood Primary",
    "Ms. Johnson",
    "Good",
    ["Alan", "Beth"]
)

school3 = School(
    "789 River Road",
    "Greenwood High",
    "Mrs. Wilson",
    "Good",
    ["Tom", "Mia"]
)

# These lines call the description() method for each object.
school1.description()
school2.description()

# These lines print individual instance attributes.
print(school1.name)
print(school1.rating)
print(school2.name)
print(school2.rating)

# These lines use the __len__ built-in method.
print(len(school1))
print(len(school2))

# These lines use the __str__ and __repr__ built-in methods.
print(school1)
print(repr(school1))

# These lines use the __eq__ built-in method.
# Python automatically calls school1.__eq__(school2).
print(school1 == school2)
print(school1 == school3)

# This deletes the reference to school1.
del school1

# This asks Python to run garbage collection.
gc.collect()
print(school2.__dict__)
print(School.__dict__)
print(School.__doc__)
print(school2.__class__)
print(school2.__class__.__name__)
print(School.__module__)
