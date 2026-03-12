# dao/itemvalues_dao.py
from database import get_connection


def get_all_values():
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT
            iv.value_id,
            iv.item_id,
            pi.item_name,
            ps.set_name,
            iv.market_value,
            iv.recorded_date
        FROM ItemValues iv
        JOIN PokemonItems pi ON iv.item_id = pi.item_id
        JOIN ProductSets ps ON pi.set_id = ps.set_id
        ORDER BY iv.value_id
    """)
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows


def get_value_by_id(value_id: int):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT
            iv.value_id,
            iv.item_id,
            pi.item_name,
            ps.set_name,
            iv.market_value,
            iv.recorded_date
        FROM ItemValues iv
        JOIN PokemonItems pi ON iv.item_id = pi.item_id
        JOIN ProductSets ps ON pi.set_id = ps.set_id
        WHERE iv.value_id = %s
    """, (value_id,))
    row = cur.fetchone()
    cur.close()
    cnx.close()
    return row


def get_values_by_item_id(item_id: int):
    """Price history for one item, now including item name and set name."""
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT
            iv.value_id,
            iv.item_id,
            pi.item_name,
            ps.set_name,
            iv.market_value,
            iv.recorded_date
        FROM ItemValues iv
        JOIN PokemonItems pi ON iv.item_id = pi.item_id
        JOIN ProductSets ps ON pi.set_id = ps.set_id
        WHERE iv.item_id = %s
        ORDER BY iv.recorded_date
    """, (item_id,))
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows