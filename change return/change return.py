costOfItem = float(raw_input("Enter cost of the item: " ))
moneyGiven = float(raw_input("Enter given: "))

quarter = 0
dime = 0
nickel = 0
penny = 0

change = float(moneyGiven - costOfItem)
print "Your change is ", change
while True:
    if change > 1:
       change -= 1
    elif change > .25 and change < 1.00:
        change -= .25
        quarter += 1
    elif change > .10 and change < .25:
        change -= .10
        dime +=  1
    elif change > .05 and change < .10:
        change -= .05
        nickel += 1
    elif  change < .05:
        print change
        penny = penny + int(change * 100)
        change -= .01
        penny += 1
        break
print "quarters: %s \ndimes: %s \nnickels: %s \npennies: %s \n " % (quarter, dime, nickel, penny)