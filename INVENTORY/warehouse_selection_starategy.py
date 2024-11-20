from abc import ABC,abstractmethod

class WareHouseSelectionStrategy(ABC):
    @abstractmethod
    def select_warehouse(self, warehouses):
        pass
    
class NearestWarehouseStrategy(WareHouseSelectionStrategy):
    def select_warehouse(self, warehouses):
        return warehouses.get('10001')
    
class CheapestWarehouseStrategy(WareHouseSelectionStrategy):
    def select_warehouse(self, warehouses):
        return min(warehouses, key=lambda warehouse: warehouse.inventory.product_id_quantity_map)