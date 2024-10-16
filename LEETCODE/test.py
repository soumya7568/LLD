# User class for authentication and tracking progress
class User:
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email
        self.solved_problems = []  # List of solved problem IDs

    def submit_solution(self, problem, code):
        submission = Submission(self, problem, code)
        result = submission.evaluate()
        if result == "Accepted":
            self.solved_problems.append(problem.id)
        return result

    def view_profile(self):
        return {
            "username": self.username,
            "email": self.email,
            "solved_problems": len(self.solved_problems)
        }


# Problem class stores problem details and test cases
class Problem:
    def __init__(self, problem_id, title, description, difficulty, test_cases):
        self.id = problem_id
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.test_cases = test_cases  # List of test cases
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)


# Submission class for submitting solutions to problems
class Submission:
    def __init__(self, user, problem, code):
        self.user = user
        self.problem = problem
        self.code = code
        self.status = "Pending"

    def evaluate(self):
        # Simulating code evaluation against test cases
        for test_case in self.problem.test_cases:
            input_data, expected_output = test_case
            result = self.run_code(input_data)
            if result != expected_output:
                self.status = "Wrong Answer"
                return self.status
        
        self.status = "Accepted"
        return self.status

    def run_code(self, input_data):
        # Simulate running user code (here it could be any logic, mock for now)
        # Assume `exec()` or sandbox execution in the actual system
        return input_data  # For simplicity, just return the input as output


# Leaderboard class for ranking users
class Leaderboard:
    def __init__(self):
        self.users = []

    def update(self, user):
        # If user not in the leaderboard, add them
        if user not in self.users:
            self.users.append(user)

    def get_top_users(self, top_n=10):
        # Sort users by the number of problems solved and return top N users
        return sorted(self.users, key=lambda u: len(u.solved_problems), reverse=True)[:top_n]


# Discussion class for problem-specific discussions
class Discussion:
    def __init__(self, problem):
        self.problem = problem
        self.posts = []

    def add_post(self, user, content):
        post = {"user": user.username, "content": content}
        self.posts.append(post)

    def view_posts(self):
        return self.posts


# Example Test Cases and Flow
if __name__ == "__main__":
    # Create some users
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com")

    # Create a problem with some test cases
    problem1 = Problem(101, "Two Sum", "Find indices of two numbers that add up to a target", "easy", [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2])
    ])

    # User1 submits a solution
    code = """def two_sum(nums, target):
                  for i in range(len(nums)):
                      for j in range(i+1, len(nums)):
                          if nums[i] + nums[j] == target:
                              return [i, j]"""
    result = user1.submit_solution(problem1, code)
    print(f"User1 Submission Result: {result}")

    # Create leaderboard and update rankings
    leaderboard = Leaderboard()
    leaderboard.update(user1)
    leaderboard.update(user2)
    print("Top users: ", [user.username for user in leaderboard.get_top_users()])

    # Problem discussion
    discussion = Discussion(problem1)
    discussion.add_post(user1, "Can anyone explain how to optimize this solution?")
    print("Discussion posts:", discussion.view_posts())
