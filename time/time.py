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
# five classes: date (year/month/day)/ time (hour, minute, second, microsecond, tzinfo)/ datetime (year, month, day,
# hour, minute, second, microsecond, and tzinfo.)/ timedelta (diff btw date and time)/ tzinfo (???)

# There are two kinds of date and time objects: “naive” and “aware”. This distinction refers to whether the object
# has any notion of time zone, daylight saving time, or other kind of algorithmic or political time adjustment.
#