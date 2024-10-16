class Contest:
    def __init__(self, contest_id, title, start_time, end_time, problems):
        self.contest_id = contest_id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.problems = problems
        self.leaderboard = Leaderboard()

class Leaderboard:
    def __init__(self):
        self.rankings = []

    def update_rankings(self, user, score):
        self.rankings.append((user, score))
        self.rankings.sort(key=lambda x: x[1], reverse=True)  # Sort by score
