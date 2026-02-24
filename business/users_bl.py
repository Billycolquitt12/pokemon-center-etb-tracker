# business/users_bl.py
from dao import users_dao


class UsersBL:
    def get_all(self):
        return users_dao.get_all_users()

    def get_one(self, user_id: int):
        return users_dao.get_user_by_id(user_id)

    def get_subset_by_username(self, username: str):
        return users_dao.get_users_by_username(username.strip())