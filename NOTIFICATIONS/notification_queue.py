from  collections import deque
class NotificationQueue:
    def __init__(self):
        self.queue = deque()

    def add_notification(self, notification):
        self.queue.append(notification)

    def get_notification(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0
