import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Phone_Num INTEGER,
DILLER STRING ,
DOLJNOST STRING ,
DOM STRING,
DATATIME STRING,
BILL STRING,
ZAKAZ STRING,
Lang INTEGER ,
Stage INTEGER,
Lang_sql STRING
)
""")
first_insert = """
INSERT INTO Users VALUES ("{}", " ", " ", " ", " ", " ", " ", " ", " ", " ", "{}",  " ")
"""

upd_DATATIME = """
UPDATE Users 
SET DATATIME = "{}" 
WHERE TG_ID = "{}"
"""
select_DATATIME = """
SELECT DATATIME
From Users
WHERE TG_ID = "{}"
"""


upd_BILL = """
UPDATE Users 
SET BILL = "{}" 
WHERE TG_ID = "{}"
"""
select_BILL = """
SELECT BILL
From Users
WHERE TG_ID = "{}"
"""

upd_DOM = """
UPDATE Users 
SET DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""


upd_DOLJNOST = """
UPDATE Users 
SET DOLJNOST = "{}" 
WHERE TG_ID = "{}"
"""
select_DOLJNOST = """
SELECT DOLJNOST
From Users
WHERE TG_ID = "{}"
"""


get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""
upd_name = """
UPDATE Users 
SET F_Name = "{}" 
WHERE TG_ID = "{}"
"""
select_name = """
SELECT F_Name
From Users
WHERE TG_ID = "{}"
"""

update_phone_num = """
UPDATE Users 
SET Phone_Num = "{}"
WHERE TG_ID = "{}"
"""
select_num = """
SELECT Phone_Num 
FROM Users
WHERE TG_ID = "{}"
"""
upd_DILLER = """
UPDATE Users 
SET DILLER = "{}" 
WHERE TG_ID = "{}"
"""
select_DILLER = """
SELECT DILLER
FROM Users
WHERE TG_ID = "{}"
"""
select_age = """
SELECT Age_Id
FROM Users
WHERE TG_ID = "{}"
"""
get_ageid = """
UPDATE Users 
SET Age_Id = "{}"
WHERE TG_ID = "{}"
"""
lang = """
UPDATE Users
SET lang = "{}"
WHERE TG_ID = "{}"
"""
lang_select = """
SELECT Lang
FROM Users
WHERE TG_ID = "{}"
"""

stagee = """
UPDATE Users
SET Stage = "{}"
WHERE TG_ID = "{}"
"""
stage = """
SELECT Stage
FROM Users
WHERE TG_ID = "{}"
"""

upd_ZAKAZ = """
UPDATE Users
SET ZAKAZ = "{}"
WHERE TG_ID = "{}"
"""
select_ZAKAZ = """
SELECT ZAKAZ
FROM Users
WHERE TG_ID = "{}"
"""
conn.commit()