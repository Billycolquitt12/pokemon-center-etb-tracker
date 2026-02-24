# dao/productsets_dao.py
from database import get_connection


def get_all_sets():
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT set_id, set_name, release_year
        FROM ProductSets
        ORDER BY set_id
    """)
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows


def get_set_by_id(set_id: int):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT set_id, set_name, release_year
        FROM ProductSets
        WHERE set_id = %s
    """, (set_id,))
    row = cur.fetchone()
    cur.close()
    cnx.close()
    return row


def get_sets_by_year(year: int):
    """Subset endpoint example: get all sets by release year."""
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)
    cur.execute("""
        SELECT set_id, set_name, release_year
        FROM ProductSets
        WHERE release_year = %s
        ORDER BY set_id
    """, (year,))
    rows = cur.fetchall()
    cur.close()
    cnx.close()
    return rows