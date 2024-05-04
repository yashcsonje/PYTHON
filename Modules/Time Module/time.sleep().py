#Day 84
'''
The time.sleep() function suspends the execution of the current thread for a specified number of seconds.
This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.
'''

import time

print("Start:", time.time())
time.sleep(2)
print("End:", time.time())

'''
Output:
Start: 1714840195.2110398
End: 1714840197.212879
'''