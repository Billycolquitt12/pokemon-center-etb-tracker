from dao import items_dao, productsets_dao


class ItemsBL:
    def get_all_items(self):
        return items_dao.get_all_items()

    def get_item_by_id(self, item_id: int):
        if item_id <= 0:
            raise ValueError("item_id must be > 0")
        return items_dao.get_item_by_id(item_id)

    def create_item(self, user_id: int, set_id: int, item_name: str, sealed: bool = True):
        if user_id <= 0:
            raise ValueError("user_id must be > 0")

        if set_id <= 0:
            raise ValueError("set_id must be > 0")

        if not item_name or not item_name.strip():
            raise ValueError("item_name required")

        existing_set = productsets_dao.get_set_by_id(set_id)
        if existing_set is None:
            raise ValueError(f"Set ID {set_id} does not exist. Create the product set first.")

        return items_dao.create_item(user_id, set_id, item_name.strip(), sealed)

    def update_item(self, item_id: int, user_id: int, set_id: int, item_name: str, sealed: bool):
        if item_id <= 0:
            raise ValueError("item_id must be > 0")

        if user_id <= 0:
            raise ValueError("user_id must be > 0")

        if set_id <= 0:
            raise ValueError("set_id must be > 0")

        if not item_name or not item_name.strip():
            raise ValueError("item_name required")

        existing_set = productsets_dao.get_set_by_id(set_id)
        if existing_set is None:
            raise ValueError(f"Set ID {set_id} does not exist. Choose a valid product set.")

        return items_dao.update_item(item_id, user_id, set_id, item_name.strip(), sealed)

    def delete_item(self, item_id: int):
        if item_id <= 0:
            raise ValueError("item_id must be > 0")
        return items_dao.delete_item(item_id)