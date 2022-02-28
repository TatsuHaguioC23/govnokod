import schedule
import time
import datetime

def job():
	for x in range(666):
		time.sleep(0.01)
		print("I'm working...")
h = "19:05"
h = datetime.datetime.strptime(h, '%H:%M')
h = (h.strftime("%H:%M"))
print(h)

schedule.every().day.at(h).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)











