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

def create_set(set_name: str, release_year: int):
    cnx = get_connection()
    cur = cnx.cursor()
    cur.execute("""
        INSERT INTO ProductSets (set_name, release_year)
        VALUES (%s, %s)
    """, (set_name, release_year))
    cnx.commit()
    new_id = cur.lastrowid
    cur.close()
    cnx.close()
    return new_id