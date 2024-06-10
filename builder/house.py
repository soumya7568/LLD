class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls}, {self.roof}, {self.windows}, and {self.doors}"
