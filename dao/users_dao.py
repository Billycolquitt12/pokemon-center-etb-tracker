# dao/users_dao.py
from database import get_connection


def get_all_users():
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT user_id, username, email
        FROM Users
        ORDER BY user_id
    """)
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows


def get_user_by_id(user_id: int):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT user_id, username, email
        FROM Users
        WHERE user_id = %s
    """, (user_id,))
    row = cur.fetchone()
    cur.close()
    cnx.close()
    return row


def get_users_by_username(username: str):
    """Subset endpoint example: find users whose username contains a string."""
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT user_id, username, email
        FROM Users
        WHERE username LIKE %s
        ORDER BY user_id
    """, (f"%{username}%",))
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows