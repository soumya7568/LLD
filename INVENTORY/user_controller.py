class UserController:
    def __init__(self):
        self.users = dict()
        
    def add_user(self, user):
        self.users[user.name] = user
        
    def remove_user(self, user):
        del self.users[user.name]