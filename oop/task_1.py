class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_user(self):
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(f"Phone : {self.phone}")

    @staticmethod
    def is_valid_email(email):
        if "@" in email and "." in email:
            return True
        return False

    @staticmethod
    def is_valid_phone(phone):
        if len(phone) == 10 and phone.isdigit():
            return True
        return False

use1 = User("Nitin", "nitin@gmail.com", "9988776655")
use1.display_user()
print(User.is_valid_email("nitin@gmail.com"))
print(User.is_valid_phone("9876543210"))

