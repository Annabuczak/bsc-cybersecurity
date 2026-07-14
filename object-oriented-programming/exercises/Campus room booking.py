class Room:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity

    def __str__(self):
        return f"Room {self.room_id} (capacity {self.capacity})"


class Booking:
    def __init__(self, room, user_name, time_slot):
        self.room = room
        self.user_name = user_name
        self.time_slot = time_slot

    def __str__(self):
        return f"{self.room} booked by {self.user_name} at {self.time_slot}"


class BookingSystem:
    def __init__(self):
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room_id, user_name, time_slot):
        selected_room = None

        for room in self.rooms:
            if room.room_id == room_id:
                selected_room = room

        if selected_room is None:
            print("Room does not exist")
            return

        for booking in self.bookings:
            if booking.room.room_id == room_id and booking.time_slot == time_slot:
                print("Room is already booked at this time")
                return

        new_booking = Booking(selected_room, user_name, time_slot)
        self.bookings.append(new_booking)
        print("Booking successful")

    def show_bookings(self):
        for booking in self.bookings:
            print(booking)


system = BookingSystem()

room_1 = Room("A101", 30)
room_2 = Room("A102", 45)
room_3 = Room("A103", 55)

system.add_room(room_1)
system.add_room(room_2)
system.add_room(room_3)

system.book_room("A101", "Anna", "10:00")
system.book_room("A102", "Tom", "11:00")
system.book_room("A101", "Ben", "10:00")  # already booked

system.show_bookings()
