# business/itemvalues_bl.py
from dao import itemvalues_dao


class ItemValuesBL:
    def get_all(self):
        return itemvalues_dao.get_all_values()

    def get_one(self, value_id: int):
        return itemvalues_dao.get_value_by_id(value_id)

    def get_subset_by_item(self, item_id: int):
        return itemvalues_dao.get_values_by_item_id(item_id)