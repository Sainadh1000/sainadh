# Create a base class Notification

# Method:

# send(message) → prints "Sending notification..."

# Subclasses (override send(message)):

# EmailNotification

# Print: "Sending Email: <message>"

# SMSNotification

# Print: "Sending SMS: <message>"

# PushNotification

# Print: "Sending Push Notification: <message>"
# Function:

# send_notification(notification_obj, message)

# Calls notification_obj.send(message)

# Requirement:

# Create a list of different notification objects

# Loop through them and send different messages

class notification:
    def send(self,message):
        print(f"sending notifications")
class emailnotification(notification):
    def send(self,message):
        print(f"Sending Email: {message}")
class smsnotification(notification):
    def send(self,message):
        print(f"Sending sms: {message}")
class pushnotification(notification):
    def send(self,message):
        print(f"Sending push notification: {message}")

notifications = [
    emailnotification(),
    smsnotification(),
    notification()
]

def send_notification(notification_obj, message):
    notification_obj.send(message)
for n in notifications:
    send_notification(n, "Hello User!")
