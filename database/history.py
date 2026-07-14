from database.database import conn, cursor

def save_history(feature, filename, result):

    cursor.execute(
        """
        INSERT INTO history(feature, filename, result)
        VALUES(?,?,?)
        """,
        (feature, filename, result)
    )

    conn.commit()


def get_history():

    cursor.execute("SELECT * FROM history ORDER BY id DESC")

    return cursor.fetchall()