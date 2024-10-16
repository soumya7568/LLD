from sender import NotificationSender
import datetime

class NotificationProcessor:
    def __init__(self, notification_queue):
        self.notification_queue = notification_queue

    def process_notifications(self):
        while self.notification_queue:
            notification = self.notification_queue.get_notification()
            user = notification.user

            # Check user preferences before sending notification
            if notification.notification_type == 'email' and not user.preferences.email_allowed:
                print(f"User {user.email} has disabled email notifications.")
                continue
            elif notification.notification_type == 'sms' and not user.preferences.sms_allowed:
                print(f"User {user.email} has disabled SMS notifications.")
                continue
            elif notification.notification_type == 'push' and not user.preferences.push_allowed:
                print(f"User {user.email} has disabled push notifications.")
                continue

            # Send the notification
            success = NotificationSender.send_notification(notification)
            if success:
                notification.status = 'sent'
                notification.sent_at = datetime.now()
                print(f"Notification {notification.id} sent successfully.")
            else:
                notification.status = 'failed'
                print(f"Notification {notification.id} failed to send.")
