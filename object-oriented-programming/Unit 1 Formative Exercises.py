class Membership:
    def __init__(self, first_name, last_name, membership_type, is_active):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_type = membership_type
        self.is_active = is_active

        if is_active == True:
            print(f"{self.first_name} {self.last_name} is an active member with a {self.membership_type} membership.")
        else:
            print(
                f"{self.first_name} {self.last_name} is not an active member, but they have a {self.membership_type} membership.")

    def show_details(self):
        print(
            f"{self.first_name} {self.last_name} membership type is {self.membership_type}, and their active status is {self.is_active}.")


class Member_one(Membership):
    def __init__(self, first_name, last_name, membership_type, is_active):
        super().__init__(first_name, last_name, membership_type, is_active)


class Member_two(Membership):
    def __init__(self, first_name, last_name, membership_type, is_active):
        super().__init__(first_name, last_name, membership_type, is_active)


class Member_three(Membership):
    def __init__(self, first_name, last_name, membership_type, is_active):
        super().__init__(first_name, last_name, membership_type, is_active)


member_one = Member_one("John", "Sawyer", "Gold", True)
member_two = Member_two("Anna", "Buczak", "Silver", False)
member_three = Member_three("Lou", "Costa", "Platinum", True)
