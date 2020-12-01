# Basic
for i in range(0, 151, 1):
    print (i)

# Multiples of Five

for i in range(5, 5005, 5):
    print (i)

# Counting, the Dojo Way

for i in range(0, 101, 1):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:  # Tried using elif here but since the first if statement was true it didn't check the second condition. Changed it to another if statement.
        print ("Coding ju ju")
    else:
        print (i)

# Whoa that sucker is huge

for i in range(1, 500000, 2):
    sum = 0
    sum = sum + i
    print (sum)

# Countdown by fours

for i in range(2018, 0, -4):
    print (i)

# Flexible Counter

lowNum = 3
highNum = 20
mult = 5

def flexCount(lowNum, highNum, mult):
    for i in range(lowNum, highNum):
        if i % mult == 0:
            print (i)
flexCount(lowNum, highNum, mult)  # call the function like you would in js

