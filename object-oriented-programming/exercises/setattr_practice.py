class Vegetables:
    pass


veggie1 = Vegetables()

veggie1_details = {
    "name": "Beans",
    "colour": "Green",
    "vitamins": ["B", "C", "K"],
    "calories": 50
}

for key, value in veggie1_details.items():
    setattr(veggie1, key, value)

print(veggie1.name)
print(veggie1.colour)
print(veggie1.vitamins)
print(veggie1.calories)
