# DO NOT import any Python libraries


def add_times(start: str, duration: str, day = None: str) -> str:
	new_minutes = ""
	times = ""
	days_later = ""
	result = ""
	day_count = 0
	cycle = 0

	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	week = { v.lower(): i for i, v in enumerate(days) }

	# Parse hour, minute, and period
	start_hour, str2 = start.split(":")
	start_minute, period = str2.split()
	add_hour, add_minute = duration.split(":")

	# Initial AM/PM period
	if (period == "PM") : cycle = 1

	# Calculate minutes
	minutes = int(start_minute) + int(add_minute)
	if ( (minutes % 60) < 10 ):
		new_minutes += "0" + str(minutes % 60)
	else:
		new_minutes += str(minutes % 60)

	# Calculate hours
	if (period == "PM"):
		new_hours = ( int(start_hour) + 12 ) + int(add_hour) + (minutes // 60)
	else:
		new_hours = int(start_hour) + int(add_hour) + (minutes // 60)

	# Update AM/PM period
	count = (new_hours + cycle) // 12
	if ( count % 2 == 0) : period = "AM"
	else : period = "PM"

	# Count the number of days later
	day_count = new_hours // 24

	# Convert to 24-hours
	new_hours %= 24

	# Convert back into 12-hour with respective period
	if (new_hours == 12 or new_hours == 0):
		times += "12:" + new_minutes + " " + period
	elif (new_hours > 12):
		new_hours %= 12
		times += str(new_hours) + ":" + new_minutes + " " + period
	else:
		times += str(new_hours) + ":" + new_minutes + " " + period

	# Days later
	if (day_count == 1):
		days_later += "(next day)"
	elif (day_count > 1):
		days_later += "(" + str(day_count) + " days later)"

	# Day of the week
	if ( (day != None) and (day_count == 0) ):
		result += times + ", " + day
	elif (day != None):
		index = ( week[day.lower()] + day_count ) % 7
		result += times + ", " + days[index] + " " + days_later
	elif (day_count > 0):
		result += times + " " + days_later
	else:
		result += times

	return result

