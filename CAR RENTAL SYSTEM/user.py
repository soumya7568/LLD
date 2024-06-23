class User:
    def __init__(self, user_id: int = None, user_name: str = None, driving_license: int = None):
        self.user_id = user_id
        self.user_name = user_name
        self.driving_license = driving_license

    # Getters and setters
    def get_user_id(self) -> int:
        return self.user_id

    def set_user_id(self, user_id: int):
        self.user_id = user_id

    def get_user_name(self) -> int:
        return self.user_name

    def set_user_name(self, user_name: int):
        self.user_name = user_name

    def get_driving_license(self) -> int:
        return self.driving_license

    def set_driving_license(self, driving_license: int):
        self.driving_license = driving_license

