from database import get_connection

def get_values_for_item(item_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT * FROM ItemValues
        WHERE item_id=%s
        ORDER BY recorded_date
    """, (item_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def add_value(item_id: int, market_value: float, recorded_date: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ItemValues (item_id, market_value, recorded_date)
        VALUES (%s,%s,%s)
    """, (item_id, market_value, recorded_date))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def update_value(value_id: int, market_value: float, recorded_date: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE ItemValues
        SET market_value=%s, recorded_date=%s
        WHERE value_id=%s
    """, (market_value, recorded_date, value_id))
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows


def delete_value(value_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM ItemValues WHERE value_id=%s", (value_id,))
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows