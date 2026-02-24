# business/productsets_bl.py
from dao import productsets_dao


class ProductSetsBL:
    def get_all(self):
        return productsets_dao.get_all_sets()

    def get_one(self, set_id: int):
        return productsets_dao.get_set_by_id(set_id)

    def get_subset_by_year(self, year: int):
        return productsets_dao.get_sets_by_year(year)