import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users_list(
TG_ID INTEGER 
)
""")
first_insert222 = """
INSERT INTO Users_list VALUES ("{}")
"""

get__id = """
SELECT TG_ID 
FROM Users_list
Where TG_ID = "{}"
"""