#Day 84
'''
The time.strftime() function formats a time value as a string, based on a specified format.
This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report.
'''

import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2024-05-04 22:02:48