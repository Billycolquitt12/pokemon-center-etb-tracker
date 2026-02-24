# service/routers/users_api.py
from fastapi import APIRouter, HTTPException
from business.users_bl import UsersBL

router = APIRouter(prefix="/users", tags=["users"])
bl = UsersBL()


@router.get("/")
def get_all_users():
    return bl.get_all()


@router.get("/{user_id}")
def get_user(user_id: int):
    row = bl.get_one(user_id)
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return row


# SUBSET example (required by Project 3):
@router.get("/search/{username}")
def search_users(username: str):
    return bl.get_subset_by_username(username)