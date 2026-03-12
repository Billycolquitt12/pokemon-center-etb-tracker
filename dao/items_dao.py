from database import get_connection


def get_all_items():
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT item_id, user_id, set_id, item_name, sealed
        FROM PokemonItems
        ORDER BY item_id
    """)
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows


def get_item_by_id(item_id: int):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT item_id, user_id, set_id, item_name, sealed
        FROM PokemonItems
        WHERE item_id = %s
    """, (item_id,))
    row = cur.fetchone()
    cur.close()
    cnx.close()
    return row


def create_item(user_id: int, set_id: int, item_name: str, sealed: bool = True):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO PokemonItems (user_id, set_id, item_name, sealed)
            VALUES (%s, %s, %s, %s)
        """, (user_id, set_id, item_name, sealed))
        conn.commit()
        new_id = cur.lastrowid
        return new_id
    finally:
        cur.close()
        conn.close()


def update_item(item_id: int, user_id: int, set_id: int, item_name: str, sealed: bool):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE PokemonItems
            SET user_id = %s, set_id = %s, item_name = %s, sealed = %s
            WHERE item_id = %s
        """, (user_id, set_id, item_name, sealed, item_id))
        conn.commit()
        rows = cur.rowcount
        return rows
    finally:
        cur.close()
        conn.close()


def delete_item(item_id: int):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM PokemonItems WHERE item_id = %s", (item_id,))
        conn.commit()
        rows = cur.rowcount
        return rows
    finally:
        cur.close()
        conn.close()