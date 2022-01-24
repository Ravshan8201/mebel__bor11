import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Menyu(
TOVAR_UZ STRING,
TOVAR_RU STRING,
DIRECTORY STRING,
PHOTO_1 STRING,
PRICE INTEGER 
)""")
first_insert3 = """
INSERT INTO Menyu VALUES ("{}","{}","{}","{}","{}")
"""
dct_upd = """
UPDATE Menyu
SET DIRECTORY = "{}"
WHERE TOVAR = "{}"
"""
dct_select = """
SELECT DIRECTORY
FROM Menyu
WHERE {} = "{}"

"""

tovar_upd = """
UPDATE Menyu
SET {} = "{}"
WHERE TOVAR_RU = "{}" and DIRECTORY = "{}"
"""
tovar_select = """
SELECT {}
FROM korzina
WHERE {} = "{}" and DIRECTORY = "{}"
"""



price_upd = """
UPDATE Menyu
SET PRICE = "{}"
WHERE TOVAR = "{}"
"""
price_select = """
SELECT PRICE
FROM Menyu
WHERE {} = "{}"
"""

