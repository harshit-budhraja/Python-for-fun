# Author: Harshit Budhraja
# Greets you according to the time of the day.
import time

name = "YOUR_NAME"
now = time.strftime("%H")
now = int(now)
if now > 0 and now < 12:
	greet = "Good Morning, " + name
elif now > 12 and now < 16:
	greet = "Good Afternoon, " + name
elif now > 16 and now < 20:
	greet = "Good Evening, " + name
elif now > 20 and now < 24:
	greet = "Good Night, " + name

print greet
