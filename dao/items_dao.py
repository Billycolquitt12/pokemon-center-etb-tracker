from database import get_connection

def get_all_items():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT p.item_id, p.item_name, p.sealed,
               u.username,
               s.set_name, s.release_year
        FROM PokemonItems p
        JOIN Users u ON p.user_id = u.user_id
        JOIN ProductSets s ON p.set_id = s.set_id
        ORDER BY p.item_id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_item_by_id(item_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT item_id, user_id, set_id, item_name,
               (sealed = 1) AS sealed
        FROM PokemonItems
        WHERE item_id = %s
    """, (item_id,))

    row = cur.fetchone()
    conn.close()
    return row

def create_item(user_id: int, set_id: int, item_name: str, sealed: bool=True):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO PokemonItems (user_id, set_id, item_name, sealed)
        VALUES (%s,%s,%s,%s)
    """, (user_id, set_id, item_name, sealed))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def update_item(item_id: int, user_id: int, set_id: int, item_name: str, sealed: bool):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE PokemonItems
        SET user_id=%s, set_id=%s, item_name=%s, sealed=%s
        WHERE item_id=%s
    """, (user_id, set_id, item_name, sealed, item_id))
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows


def delete_item(item_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM PokemonItems WHERE item_id=%s", (item_id,))
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows