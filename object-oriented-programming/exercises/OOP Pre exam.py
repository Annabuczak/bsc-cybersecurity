# Scenario: Bike Repair Task Tracker

class Task:
    def __init__(self, name=str, reward_amount=float, is_complete=bool):
        self.name = name
        self.reward_amount = reward_amount,
        self.is_complete = is_complete

    def describe(self):

        if (self.is_complete):
            print(f"Louie has completed: {self.name} and {self.reward_amount}")
        else:
            print(f"Louie has not completed: {self.name} and  did not earn {self.reward_amount}")


task_1 = Task("Take rubbish out", reward_amount=5.0, is_complete=True)
task_2 = Task("Hoover living room", reward_amount=2.0, is_complete=False)
task_3 = Task("Walked Buddy", reward_amount=3.0, is_complete=True)
task_1.describe()
task_2.describe()
task_3.describe()


# Household Reward Tracker — Procedural Version
class HouseholdTask:
    def __init__(self, name, reward_amount=float, is_complete=bool):
        self.name = name
        self.reward_amount = name
        self.is_complete = is_complete


class RewardTracker:

    def __init__(self):

        self.tasks = []

    def add_task(self, HouseholdTask, ):
        self.name.append(HouseholdTask)

    def calculate_reward_amount(self):
        if self.is_complete:
            return self.reward_amount
        else:
            print(f"Louie has not completed: {self.name}")

    def show_tasks(self):
        if (self.is_complete):
            print(f"Louie has completed: {self.name}")
        else:
            print(f"Louie has not completed: {self.name}")
            for householdtasks in self.name:
                print(householdtasks)


house_task1 = HouseholdTask("Put laundry away", reward_amount=1.0, is_complete=True)
house_task2 = HouseholdTask("Put bike away", reward_amount=3.0, is_complete=False)
house_task3 = HouseholdTask("Fed Buddy", reward_amount=2.0, is_complete=True)

reward_amount = [1.0, 3.0, 2.0]
print(reward_amount)

print(house_task1.name)
print(house_task2.name)
print(house_task3.name)

total_earned = sum(reward_amount)
print("Money earned this week " + str(total_earned))

total_owned = 110
print("Money owned for bike repair: " + str(total_owned))

total_earned -= total_owned
print("Remining balance: " + str(total_earned))
total_earned += total_owned

# Weekly Behaviour Points

day_name_point = {
    "Monday": 8,
    "Tuesday": 3,
    "Wednesday": 10,
    "Thursday": 5,
    "Friday": 2,

}
total_points_earned = sum(day_name_point.values())
print(f'Total points earned this week: {total_points_earned}')

average_points_earned = total_points_earned / len(day_name_point)
print(f'Average points earned this week: {average_points_earned}')
good_days = []

for day, points in day_name_point.items():
    if points >= 6:
        good_days.append(day)

print(f"Good days: {good_days}")
