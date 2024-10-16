class Problem:
    def __init__(self, problem_id, title, description, difficulty, test_cases, tags):
        self.problem_id = problem_id
        self.title = title
        self.description = description
        self.difficulty = difficulty  # Easy, Medium, Hard
        self.test_cases = test_cases  # List of input/output pairs
        self.tags = tags  # Array, Dynamic Programming, etc.

class TestCase:
    def __init__(self, input_data, expected_output):
        self.input_data = input_data
        self.expected_output = expected_output
