import uuid
from datetime import datetime

class Notification:
    def __init__(self, user, notification_type, template):
        self.id = str(uuid.uuid4())
        self.user = user
        self.notification_type = notification_type  # 'email', 'sms', 'push'
        self.template = template
        self.status = 'pending'  # 'pending', 'sent', 'failed'
        self.sent_at = None

    def __str__(self):
        return f"Notification(ID={self.id}, User={self.user.email}, Type={self.notification_type}, Status={self.status})"


class User:
    def __init__(self, email, phone_number, device_token, preferences):
        self.email = email
        self.phone_number = phone_number
        self.device_token = device_token
        self.preferences = preferences


class UserPreferences:
    def __init__(self, email_allowed=True, sms_allowed=True, push_allowed=True, notification_frequency='instant'):
        self.email_allowed = email_allowed
        self.sms_allowed = sms_allowed
        self.push_allowed = push_allowed
        self.notification_frequency = notification_frequency  # 'instant', 'daily', 'weekly'


class NotificationTemplate:
    def __init__(self, content, template_type):
        self.content = content
        self.template_type = template_type  # 'email', 'sms', 'push'
