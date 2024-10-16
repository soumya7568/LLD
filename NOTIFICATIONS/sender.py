class NotificationSender:
    @staticmethod
    def send_notification(notification):
        if notification.notification_type == 'email':
            return NotificationSender.send_email(notification.user.email, notification.template.content)
        elif notification.notification_type == 'sms':
            return NotificationSender.send_sms(notification.user.phone_number, notification.template.content)
        elif notification.notification_type == 'push':
            return NotificationSender.send_push(notification.user.device_token, notification.template.content)

    @staticmethod
    def send_email(to_email, content):
        # Simulating sending an email
        print(f"Sending email to {to_email} with content: {content}")
        return True  # Simulate success

    @staticmethod
    def send_sms(to_phone, content):
        # Simulating sending an SMS
        print(f"Sending SMS to {to_phone} with content: {content}")
        return True  # Simulate success

    @staticmethod
    def send_push(device_token, content):
        # Simulating sending a push notification
        print(f"Sending push notification to device {device_token} with content: {content}")
        return True  # Simulate success
