class WarehouseController:
    def __init__(self,warehouse_selection_strategy):
        self.warehouses = dict()
        self.warehouse_selection_strategy = warehouse_selection_strategy
        
    def add_warehouse(self, warehouse):
        self.warehouses[warehouse.address.zip_code] = warehouse
        
    def remove_warehouse(self, warehouse):
        del self.warehouses[warehouse.address.zip_code]
        
    def select_warehouse(self):
        return self.warehouse_selection_strategy.select_warehouse(self.warehouses)