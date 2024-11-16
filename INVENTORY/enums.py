from enum import Enum
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4
    RETURNED = 5
    