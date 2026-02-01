from database import get_connection

def get_all_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.item_id, p.item_name, s.set_name
        FROM PokemonItems p
        JOIN ProductSets s ON p.set_id = s.set_id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_item(user_id, set_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO PokemonItems (user_id, set_id, item_name)
        VALUES (%s, %s, %s)
    """, (user_id, set_id, name))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PokemonItems WHERE item_id = %s", (item_id,))
    conn.commit()
    conn.close()
