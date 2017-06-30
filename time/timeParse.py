import datetime
import re

# let's say we have input like:
# 1. "Sun 13:00-15:00", "Mon 12:00-21:00"
# 2. "1979 Mar 24th 14:22:35", "2015 July 1st 09:33:21", current time
# 3. "03/21/15 18:26:52	", "11/19/17 20:11:22"

# A study of datetime package

time1str1, time1str2 = "1979 Mar 24th 14:22:35", "2015 July 1st 09:33:21"
time2str1, time2str2 = "03/21/15 18:26:52", "11/19/17 20:11:22"
time3str1, time3str2 = "Sun 13:02-15:50", "Mon 12:13-21:11"
current = datetime.datetime.today()
print current

time1_1 = datetime.datetime.strptime(time1str1, "%Y %b %dth %X")
time1_2 = datetime.datetime.strptime(time1str2, "%Y %B %dst %X")
current1 = current.strftime("%Y %b %d %X")
print "Current time in format 1 is: " + str(current1)
diff1 = time1_2 - time1_1
print str(time1_1) +", "+ str(time1_2) + ", diff is: " + str(diff1)

time2_1 = datetime.datetime.strptime(time2str1, "%x %X")
time2_2 = datetime.datetime.strptime(time2str2, "%x %X")
current2 = current.strftime("%x %X")
print "Current time in format 2 is: " + str(current2)
diff2 = time2_1 - time2_2
print str(time2_1) +", "+ str(time2_2) + ", diff is: " + str(diff2)

#Time interval
#Time interval cannot be represented using normal datetime, use regex to parse.

time3match = re.search(r"(\d+:\d+)-(\d+:\d+)",time3str1)
time1, time2 = time3match.group(1,2)
time1, time2 = datetime.datetime.strptime(time1, "%H:%M"), datetime.datetime.strptime(time2, "%H:%M")
diff3 = time1 - time2
print time1, time2, diff3
# re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in
#  the string (this is what Perl does by default).
