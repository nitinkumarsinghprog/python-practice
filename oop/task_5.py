# Abstraction

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email notification sent: {message}")
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS notification sent: {message}")
class PushNotification(Notification):
    def send(self, message):
        print(f"Push notification sent: {message}")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send("Your order has been shipped")