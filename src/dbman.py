import mysql.connector as dbman

db_conf={
    'host':"localhost",
    'port':33060,
    'user':"root",
    'password':"secret",
    'db':'BDAP'
}

db = dbman.connect(**db_conf)
cur = db.cursor()
cur.execute('SELECT * FROM CLIENTE')

for i in cur.fetchall():
    print(i)