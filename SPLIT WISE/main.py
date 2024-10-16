class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.balances = {}  # Holds balances for each user
        
    def add_balance(self, user_id: str, amount: float) -> None:
        """Add a balance for a specific user."""
        if user_id in self.balances:
            self.balances[user_id] += amount
        else:
            self.balances[user_id] = amount

    def get_balance(self) -> dict:
        """Return all balances."""
        return self.balances

    def settle_up(self, user_id: str, amount: float) -> None:
        """Settle up with another user by paying them an amount."""
        if user_id in self.balances:
            self.balances[user_id] -= amount
        else:
            raise ValueError("User not found in balances")


class Group:
    def __init__(self, group_id: str, name: str, members: list):
        self.group_id = group_id
        self.name = name
        self.members = members  # List of user IDs

    def add_member(self, user_id: str) -> None:
        """Add a user to the group."""
        if user_id not in self.members:
            self.members.append(user_id)

    def remove_member(self, user_id: str) -> None:
        """Remove a user from the group."""
        if user_id in self.members:
            self.members.remove(user_id)


class Expense:
    def __init__(self, expense_id: str, amount: float, paid_by: str, participants: list, group_id: str):
        self.expense_id = expense_id
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants  # List of user IDs
        self.group_id = group_id  # Group associated with the expense

    def split_equally(self) -> dict:
        """Return the amount owed by each participant."""
        amount_per_person = self.amount / len(self.participants)
        return {participant: amount_per_person for participant in self.participants}


class Splitwise:
    def __init__(self):
        self.users = {}  # User ID -> User object
        self.expenses = []  # List to track all expenses
        self.groups = {}  # Group ID -> Group object

    def add_user(self, user: User) -> None:
        """Add a user to the system."""
        self.users[user.user_id] = user

    def create_group(self, name: str, user_ids: list) -> Group:
        """Create a new group and add users."""
        group_id = str(len(self.groups) + 1)  # Simple ID generation
        new_group = Group(group_id, name, user_ids)
        self.groups[group_id] = new_group
        return new_group

    def add_expense(self, expense: Expense) -> None:
        """Add an expense and update user balances."""
        self.expenses.append(expense)
        splits = expense.split_equally()

        for participant in expense.participants:
            if participant != expense.paid_by:  # Only update balances for those who didn't pay
                self.users[participant].add_balance(expense.paid_by, splits[participant])

        # Update the payer's balance for each participant
        self.users[expense.paid_by].add_balance(expense.paid_by, -sum(splits.values()))

    def get_user_balances(self, user_id: str) -> dict:
        """Get the balance details of a user."""
        if user_id in self.users:
            return self.users[user_id].get_balance()
        else:
            raise ValueError("User not found")

    def get_expense_history(self, user_id: str) -> list:
        """Get the history of expenses associated with a user."""
        return [expense for expense in self.expenses if user_id in expense.participants]


# Example Usage
if __name__ == "__main__":
    splitwise = Splitwise()

    user1 = User("1", "Alice")
    user2 = User("2", "Bob")
    user3 = User("3", "Charlie")

    splitwise.add_user(user1)
    splitwise.add_user(user2)
    splitwise.add_user(user3)

    # Create a group with Alice, Bob, and Charlie
    group = splitwise.create_group("Dinner Group", ["1", "2", "3"])

    # Alice pays $60 for a dinner shared by the group
    expense1 = Expense("1", 60, "1", group.members, group.group_id)
    splitwise.add_expense(expense1)

    # Bob pays $30 for drinks shared by the group
    expense2 = Expense("2", 30, "2", group.members, group.group_id)
    splitwise.add_expense(expense2)

    print("Alice's Balances:", splitwise.get_user_balances("1"))  # Alice's balances
    print("Bob's Balances:", splitwise.get_user_balances("2"))  # Bob's balances
    print("Charlie's Balances:", splitwise.get_user_balances("3"))  # Charlie's balances

    print("Expense History for Bob:", splitwise.get_expense_history("2"))
