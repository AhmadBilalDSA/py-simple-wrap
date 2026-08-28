import sqlite3

def execute_query(db_path, query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    return res
