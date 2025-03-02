import datetime

### Accepts a string (HH:MM:SS) and returns number of seconds
### Handles SS, MM:SS, HH:MM:SS, and discards any additional parts
def timeToSeconds(timeString):
    parts = timeString.count(':')
    if parts == 0:
        timeString = '00:00:' + timeString
    elif parts == 1:
        timeString = '00:' + timeString
    elif parts > 2:
        splits = parts - 2
        timeString = timeString.split(':', splits)[-1]

    # print(timeString)
    h, m, s = timeString.rsplit(':', 2)
    seconds = 3600 * int(h) + 60 * int(m) + int(s)
    return seconds
    
### Accepts a number in seconds and returns the time formatted as HH:MM:SS
### If time is greater than 24 hours, it will include X days. Maybe edit this later.
def secondsToTime(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

### Returns a list of all times, with an optional minimum and maximum hour
### The list is in hh:mm:ss format
def getAllTimes(min=2, max=8):
    timeValues = []
    for h in range(min, max):
        for m in range(0,60):
            for s in range(0,60):
                if h == 0:
                    t = f"{m:02}:{s:02}"
                else:
                    t = f"{h:02}:{m:02}:{s:02}"

                timeValues.append(t)
    return timeValues

### Accepts age as an int and returns the 5-year age group (i.e. 20-24)
def getAgeGroup(age):
    if age < 20:
        return "Under 20"
    elif age > 79:
        return "80 and Over"
    else:
        base = int(age / 5) * 5
        return f'{base}-{base + 4}'