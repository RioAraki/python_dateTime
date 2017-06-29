# Assume package is allowed for time calculation

import datetime

# let's say we have input like:
# 1. "Sun 13:00-15:00", "Mon 12:00-21:00"
# 2. "1979 Mar 24th 14:22:35", "2015 July 1st 09:33:21", current time
# 3. "03/21/15 18:26:52	", "11/19/17 20:11:22" fmt="%m/%d/%y"

# A study of datetime package

time1str1, time1str2 = "1979 Mar 24th 14:22:35", "2015 July 1st 09:33:21"
time2str1, time2str2 = "03/21/15 18:26:52", "11/19/17 20:11:22"
time3str1, time3str2 = "Sun 13:00-15:00", "Mon 12:00-21:00"

#
# timedate api
# five classes (types): date (year/month/day)/ time (hour, minute, second, microsecond, tzinfo)/ datetime (year, month, day,
# hour, minute, second, microsecond, and tzinfo.)/ timedelta (diff btw date and time)/ tzinfo (???)

# About timezone: There are two kinds of date and time objects: "naive" and "aware". This distinction refers to whether the object
# has any notion of time zone, daylight saving time, or other kind of algorithmic or political time adjustment.

# Timedelta object
print "\n=====time delta====="
# A time interval, difference about different times
d = datetime.timedelta(weeks = 1044, days = 9941, seconds = 1358, microseconds = 1249)

print d
print repr(d)
print d.total_seconds()

# date object
print "\n=====date====="
# year, month, day; value error if date out of range
print datetime.date.today()

print datetime.date.fromtimestamp(1498450656)
# get date from a time stamp
# timestamp (epoch time): how many seconds from jan 01 1970

d=datetime.date(year=2, month=1, day=1)
print "d's ordinal: " + str(d.toordinal())
print "Today's ordinal: " + str(datetime.date.today().toordinal())
print "From ordinal 10000: " + str(datetime.date.fromordinal(10000))
# ordinal: 0001 year 01 month 01 day has initial value of 1, one day => 1 value ordinal
# when compare two dates, transfer to ordinal and compare ordinal value

# date use as dict keys, in boolean -> true
# other methods: replace(year, month, day)/ timetuple()/ weekday()/ isoweekday()/ isoformat()/ ctime()
print datetime.date(year=10,month=1,day=1).timetuple()
print datetime.date(year=10,month=1,day=1).weekday()
print datetime.date(2004, 1, 4).isocalendar() # 2004/01/04
# "== (2004, 1, 7) because its the 7th day of first week in 2004"
# The ISO year consists of 52 or 53 full weeks, and where a week starts on a Monday and ends on a Sunday. The first week
# of an ISO year is the first (Gregorian) calendar week of a year containing a Thursday. This is called week number 1,
# and the ISO year of that Thursday is the same as its Gregorian year.
# For example, 2004 begins on a Thursday, so the first week of ISO year 2004 begins on Monday, 29 Dec 2003 and
# ends on Sunday, 4 Jan 2004
print datetime.date(2002, 12, 4).isoformat() #<- default string format of date
print datetime.date(2002, 12, 4).ctime()

# CALCULATE BIRTHDAY
print "\nBirthday Calculation"
today = datetime.date.today()
print today
birthday = datetime.date(today.year,4,25)
if birthday < today:
    birthday = birthday.replace(year = today.year+1)
    print birthday
diff = birthday - today
print diff.days


# example of working with date
print "\nDate Calculation"
d = datetime.date.fromordinal(731920)
print d.strftime("%d/%m/%y")
print d.strftime("%A %d. %B %Y")
print 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")

#===important===#
# strftime(format)/__format__(format)

# date object
print "\n=====datetime====="
# A single object containing all info from a date to a time object.
# today()/ now([tz])/utcnow()/fromtimestamp()/utcfromtimestamp()/fromordinal()/combine()/strptime()/astimezone()
# utcoffset()/dst()/tzname()/
# strptime() -> Return a datetime corresponding to date_string, parsed according to format.
d = datetime.date(2017, 10, 10)
t = datetime.time(21,30)
dt1 = datetime.datetime.combine(d,t)
print datetime.datetime.combine(d,t)

dt = datetime.datetime.strptime("21/11/06 16:30", "%y/%m/%d %H:%M")
print dt
# format -> how it parse the input string

# tz -> discuss in tzinfo object

# time object
print "\n=====time====="
print "Nothing tricky"
# possible parameters: datetime.time([hour[, minute[, second[, microsecond[, tzinfo]]]]])
# time is limited to a day (< 24hr)

# tzinfo object
print "\n=====tzinfo====="
print "Not important"

print "\n=====strftime() and strptime()====="
