lastFoundPrime = 1 # starting point for each search
while True:
    choice = raw_input("Would you like to find a prime number?((y)es or (n)o")
    if choice == 'y':
        testNum = lastFoundPrime + 1
        while True:
            count =  0
            i = 2
            while i < testNum:
                if (testNum % i) == 0:
                    count += 1
                    testNum += 1
                    break
                else:
                    i += 1
            if count == 0:
                    print " %s is a prime  number" % testNum
                    lastFoundPrime = testNum
                    break
    else:
        break
