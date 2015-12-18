userNumber = int(raw_input("Please choose a number: "))
original = userNumber
steps = 0
while userNumber != 1:
    if(userNumber % 2) == 0:
        userNumber = userNumber /2
        steps += 1
    else:
        userNumber = (userNumber * 3) + 1
        steps += 1
print " To get %s to 1 it took %s steps " % (original, steps)