# Class to represent an Item
class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def reduce_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            raise ValueError(f"Insufficient stock for item {self.name}")


# Class to manage Inventory of items
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise ValueError(f"Item with ID {item_id} not found in inventory")

    def check_stock(self, item_id):
        if item_id in self.items:
            return self.items[item_id].quantity
        else:
            raise ValueError(f"Item with ID {item_id} not found in inventory")
    
    def update_stock(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id].update_quantity(quantity)
        else:
            raise ValueError(f"Item with ID {item_id} not found in inventory")


# Class to represent a Customer Order
class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.items = {}  # {item_id: quantity}
        self.status = "Pending"
    
    def add_item_to_order(self, item, quantity):
        if item.item_id in self.items:
            self.items[item.item_id] += quantity
        else:
            self.items[item.item_id] = quantity
    
    def remove_item_from_order(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise ValueError(f"Item with ID {item_id} not found in order")
    
    def checkout(self, inventory):
        # Check if all items are in stock
        for item_id, quantity in self.items.items():
            if inventory.check_stock(item_id) < quantity:
                raise ValueError(f"Insufficient stock for item ID {item_id}")
        
        # If everything is in stock, reduce the inventory
        for item_id, quantity in self.items.items():
            inventory.items[item_id].reduce_quantity(quantity)
        
        self.status = "Completed"


# Class to represent a User
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.orders = []
    
    def create_order(self, order_id):
        new_order = Order(order_id, self)
        self.orders.append(new_order)
        return new_order


# Class to represent the Warehouse which manages the Inventory
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
    
    def restock_item(self, item, quantity, supplier):
        self.inventory.update_stock(item.item_id, quantity)
        print(f"{quantity} units of {item.name} restocked by {supplier.name}")

    def check_inventory(self):
        return self.inventory.items

    def is_stock_low(self, item_id, threshold=5):
        stock = self.inventory.check_stock(item_id)
        return stock < threshold


# Class to represent a Supplier who supplies items to the Warehouse
class Supplier:
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id
        self.name = name

    def supply_item(self, warehouse, item, quantity):
        warehouse.restock_item(item, quantity, self)


# Driver Code (Main Execution)
if __name__ == "__main__":
    # Create items
    item1 = Item(1, "Laptop", 1000, 10)
    item2 = Item(2, "Phone", 500, 5)
    
    # Create a supplier
    supplier = Supplier(101, "Best Supplier")
    
    # Create a warehouse and add items to inventory
    warehouse = Warehouse("Main Warehouse")
    warehouse.inventory.add_item(item1)
    warehouse.inventory.add_item(item2)
    
    # Create a user
    user = User(1, "Alice")
    
    # Create an order
    order = user.create_order(201)
    order.add_item_to_order(item1, 2)
    order.add_item_to_order(item2, 1)
    
    # Checkout the order
    try:
        order.checkout(warehouse.inventory)
        print(f"Order {order.order_id} completed for user {user.name}")
    except ValueError as e:
        print(e)

    # Check if any item is running low
    if warehouse.is_stock_low(item2.item_id):
        print(f"Stock for item {item2.name} is low. Restocking...")
        supplier.supply_item(warehouse, item2, 10)
    
    # Display the current inventory
    for item_id, item in warehouse.check_inventory().items():
        print(f"{item.name}: {item.quantity} units")
