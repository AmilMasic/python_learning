class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} users"
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# print(user1.first, user1.last)

# print(user2.full_name())
# print(user2.initials())
# print(User.active_users)
# print(User.display_active_users())
tom = User.from_string("Tom,Jones, 69")
print(tom.full_name())
