#Day 84
'''
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.
This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.

The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized).
The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time.
'''
import time  # Import the time module

# Define a function using a while loop to iterate from 0 to 49
def usingWhile():
    i = 0
    while i < 50:
        i += 1  # Increment i
        print(i)  # Print the current value of i

# Define a function using a for loop to iterate from 0 to 49
def usingFor():
    for i in range(50):
        print(i)  # Print the current value of i

# Record the initial time
init = time.time()

# Call the function using a for loop
usingFor()

# Calculate the time taken for using a for loop
t1 = time.time() - init

# Record the initial time again
init = time.time()

# Call the function using a while loop
usingWhile()

# Calculate the time taken for using a while loop
print(time.time() - init)  # Print the time taken for using a while loop
print(t1)  # Print the time taken for using a for loop
print(time.time())  # Print the current time in seconds since the epoch

'''
Output:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
0.008760690689086914
0.006891965866088867
1714841163.2124472
'''
