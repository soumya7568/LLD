class Solution:
    def __init__(self, solution_id, user, problem, language, code):
        self.solution_id = solution_id
        self.user = user
        self.problem = problem
        self.language = language  # Python, C++, etc.
        self.code = code
        self.result = None

class Result:
    def __init__(self, status, execution_time, memory_used):
        self.status = status  # Accepted, Wrong Answer, etc.
        self.execution_time = execution_time
        self.memory_used = memory_used
