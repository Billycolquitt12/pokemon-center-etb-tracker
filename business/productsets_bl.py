from dao import productsets_dao

class ProductSetsBL:
    def get_all_sets(self):
        return productsets_dao.get_all_sets()

    def get_set_by_id(self, set_id: int):
        if set_id <= 0:
            raise ValueError("set_id must be > 0")
        return productsets_dao.get_set_by_id(set_id)

    def get_sets_by_year(self, year: int):
        if year <= 0:
            raise ValueError("year must be > 0")
        return productsets_dao.get_sets_by_year(year)

    def create_set(self, set_name: str, release_year: int):
        if not set_name or not set_name.strip():
            raise ValueError("set_name required")
        if release_year <= 0:
            raise ValueError("release_year must be > 0")
        return productsets_dao.create_set(set_name.strip(), release_year)