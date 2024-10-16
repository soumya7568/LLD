from solution_submission import Result
class CodeExecutionEngine:
    def execute_code(self, code, language, test_cases):
        # Simulate running code in a sandbox
        results = []
        for test_case in test_cases:
            result = self.run_test_case(code, language, test_case)
            results.append(result)
        return results
    
    def run_test_case(self, code, language, test_case):
        # Mock function: Runs the code with input and checks output
        execution_time = 0.5  # Example
        memory_used = 64  # Example in MB
        status = 'Accepted'  # Simulate checking output
        if test_case.expected_output != "some output":
            status = 'Wrong Answer'
        return Result(status, execution_time, memory_used)
