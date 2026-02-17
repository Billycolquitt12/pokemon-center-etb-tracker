from database import get_connection

def get_all_sets():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM ProductSets")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_set_by_id(set_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM ProductSets WHERE set_id=%s", (set_id,))
    row = cur.fetchone()
    conn.close()
    return row


def create_set(set_name: str, release_year: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProductSets (set_name, release_year) VALUES (%s,%s)",
        (set_name, release_year)
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def update_set(set_id: int, set_name: str, release_year: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE ProductSets SET set_name=%s, release_year=%s WHERE set_id=%s",
        (set_name, release_year, set_id)
    )
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows


def delete_set(set_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM ProductSets WHERE set_id=%s", (set_id,))
    conn.commit()
    rows = cur.rowcount
    conn.close()
    return rows