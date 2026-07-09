class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def description(self):
        print(f"{self.name} is a cat")


class Dog(Animal):

    def __init__(self, name, age, breed, colour):
        super().__init__(name)
        self.age = age
        self.breed = breed
        self.colour = colour
        self._hunger = 5
        self._cuddles = 10
        self._chew_level = 0
        self._swallow_level = 0
        self._friendly_level = 10
        self.burps = False

    def description(self):
        print(f"{self.name} is {self.age} year old and is a {self.breed}.")
        print(f"{self.name} is {self.colour}.")
        print(f"{self.name}'s friendly level is {self._friendly_level}.")

    def show_colour(self):
        print(f"{self.name} is {self.colour}.")

    def bark(self):
        print(f"{self.name} says woof")

    def hungry(self):
        print(f"{self.name}'s hunger level is {self._hunger}")

        if self._hunger >= 5:
            print(f"{self.name} is hungry")
        elif self._hunger <= 0:
            print(f"{self.name} is full")
        else:
            print(f"{self.name} is okay")

    def ball(self):
        print(f"{self.name} fetches the ball")

    def feed(self):
        self._hunger -= 2

        if self._hunger < 0:
            self._hunger = 0

        print(f"{self.name} has been fed")
        print(f"Hunger level is now {self._hunger}")

    def cuddles(self):
        self._cuddles += 5
        print(f"{self.name} gets cuddles")
        print(f"Cuddles level is now {self._cuddles}")

    def friendly(self):
        print(f"{self.name} is friendly")
        print(f"Friendly level is now {self._friendly_level}")

    def eat(self):
        self._chew_food()
        self._swallow_food()
        self.burps = True
        self._hunger -= 2

        if self._hunger < 0:
            self._hunger = 0

        print(f"{self.name} has eaten")
        print(f"Burps: {self.burps}")
        print(f"Hunger level is now {self._hunger}")

    def _chew_food(self):
        self._chew_level += 2
        print(f"{self.name} chews food")
        print(f"Chew level is now {self._chew_level}")

    def _swallow_food(self):
        self._swallow_level += 2
        print(f"{self.name} swallows food")
        print(f"Swallow level is now {self._swallow_level}")


whiskers = Cat("Whiskers")
buddy = Dog("Buddy", 1, "Cavalier King Charles Spaniel", "chestnut and white")

buddy.description()
buddy.show_colour()
buddy.bark()
buddy.hungry()
buddy.ball()
buddy.feed()
buddy.cuddles()
buddy.eat()
buddy.hungry()
buddy.friendly()

whiskers.description()
whiskers.eat()

animals = [
    Dog("Buddy", 1, "Cavalier King Charles Spaniel", "chestnut and white"),
    Cat("Whiskers")
]

for animal in animals:
    animal.description()
    animal.eat()
    print(animal.name)
