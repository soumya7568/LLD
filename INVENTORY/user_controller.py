from user import User

class UserController:
    def __init__(self):
        self.users = dict()
        
    def add_user(self, user:User):
        self.users[user.name] = user
        
    def remove_user(self, user:User):
        del self.users[user.name]