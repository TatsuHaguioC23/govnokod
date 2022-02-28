import sqlite3
import schedule
import time
import requests
openweather_token = "http://api.openweathermap.org/data/2.5/weather?appid=1840343a10e12bec9837aca471c28ced&q="

con = sqlite3.connect('db.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
	id INTEGER,
	name TEXT,
	lang TEXT,
	balance REAL DEFAULT(0)
	)''')
con.commit()
con = sqlite3.connect('db.db')
cur = con.cursor()
cur.execute('SELECT * FROM users')
row = cur.fetchall()
print(row)
#for x in row:
#	print(x[0])
cur.execute('''INSERT INTO users(lang, id) VALUES("23:30", "ru")''')
con.commit()
city = 'Саратов'
#param=(requests.get(openweather_token+city+"&units=metric").json())
#mainwth = (param["weather"][0]["id"])
#print(mainwth)
con = sqlite3.connect('db.db')
cur = con.cursor()
cur.execute('SELECT lang FROM users WHERE id="ru"')
row = cur.fetchone()
def job():
	thistuple = ("помидор",  "огурец",  "лук")
	for x in thistuple:  
	    print(x)
schedule.every().day.at(str(row[0])).do(job)
print(row[0])
cur.execute('SELECT * FROM users')
row = cur.fetchall()
print(row)
con.commit()
time.perf_counter()
while True:
	schedule.run_pending()
	time.sleep(1)