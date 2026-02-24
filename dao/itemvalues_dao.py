# dao/itemvalues_dao.py
from database import get_connection


def get_all_values():
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT value_id, item_id, market_value, recorded_date
        FROM ItemValues
        ORDER BY value_id
    """)
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows


def get_value_by_id(value_id: int):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT value_id, item_id, market_value, recorded_date
        FROM ItemValues
        WHERE value_id = %s
    """, (value_id,))
    row = cur.fetchone()
    cur.close()
    cnx.close()
    return row


def get_values_by_item_id(item_id: int):
    """Subset endpoint example: price history for one item."""
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT value_id, item_id, market_value, recorded_date
        FROM ItemValues
        WHERE item_id = %s
        ORDER BY recorded_date
    """, (item_id,))
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows