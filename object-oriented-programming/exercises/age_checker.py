def check_age(age):
    if age < 18:
        raise ValueError("User must be 18 or over")

    return True


age = 15
