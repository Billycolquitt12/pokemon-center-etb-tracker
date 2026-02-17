from database import get_connection

def get_all_users():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_user_by_id(user_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Users WHERE user_id=%s", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row


def create_user(username: str, email: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Users (username, email) VALUES (%s,%s)",
        (username, email)
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def update_user(user_id: int, username: str, email: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Users SET username=%s, email=%s WHERE user_id=%s",
        (username, email, user_id)
    )
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows


def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Users WHERE user_id=%s", (user_id,))
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows