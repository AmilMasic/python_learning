class User:
    active_users = 0

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

print(user1.first, user1.last)

print(user2.full_name())
print(user2.initials())
print(User.active_users)
print(user2.logout())
print(User.active_users)
