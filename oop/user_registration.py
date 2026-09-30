class User:
    def __init__(self, name, email, password):
        self.name = name 
        self.email = email
        self.password = password

    def display_user(self):
        print(self.name)
        print(self.email)
        print("*********")

    def change_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

user1 = User("Nitin", "nitin@gmail.com", "12345")
user1.display_user()
user1.change_password("abc123")
print(user1.check_password("abc123"))