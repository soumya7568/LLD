class Location:
    def __init__(self, pincode: int, city: str, state: str, country: str, address: str = None):
        self.address = address
        self.pincode = pincode
        self.city = city
        self.state = state
        self.country = country