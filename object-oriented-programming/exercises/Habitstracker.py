class Habit:
    def __init__(self, name, minutes=0):
        self.name = name
        self.minutes = minutes

    def add_minutes(self, m):
        self.minutes += m


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        new_habit = Habit(name)
        self.habits.append(new_habit)

    def log_time(self, name, minutes):
        for habit in self.habits:
            if habit.name == name:
                habit.add_minutes(minutes)

    def show_report(self):
        for habit in self.habits:
            print(f"{habit.name}: {habit.minutes} minutes")


tracker = HabitTracker()

tracker.add_habit("reading")
tracker.add_habit("exercise")
tracker.add_habit("coding")

tracker.log_time("reading", 30)
tracker.log_time("exercise", 45)
tracker.log_time("coding", 60)
tracker.log_time("reading", 20)

tracker.show_report()
