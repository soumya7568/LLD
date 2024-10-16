class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.solved_problems = []
        self.stats = UserStats()

class UserStats:
    def __init__(self):
        self.total_problems_solved = 0
        self.contests_participated = 0
        self.rank = 0
    
    def update_stats(self, problems_solved, contests):
        self.total_problems_solved += problems_solved
        self.contests_participated += contests
