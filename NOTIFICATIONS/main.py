from model import *
from notification_queue import *
from processsor import *


if __name__ == "__main__":
    # Create user preferences
    preferences = UserPreferences(email_allowed=True, sms_allowed=False, push_allowed=True)
    
    # Create users
    user1 = User("user1@example.com", "1234567890", "device_token_1", preferences)
    
    # Create a notification template
    template_email = NotificationTemplate("This is an email notification.", "email")
    template_push = NotificationTemplate("This is a push notification.", "push")
    
    # Create notifications
    notification1 = Notification(user1, "email", template_email)
    notification2 = Notification(user1, "push", template_push)
    
    # Add notifications to the queue
    queue = NotificationQueue()
    queue.add_notification(notification1)
    queue.add_notification(notification2)
    
    # Process the notifications
    processor = NotificationProcessor(queue)
    processor.process_notifications()
