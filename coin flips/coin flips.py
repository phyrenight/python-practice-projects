import random

timesToFlip = int(raw_input("How many times do you want to flip the coin: "))

heads = 0
tails = 0
coinFlips = []
i = 0
while i < timesToFlip:
    random.seed()
    flip = random.randint(1,2)
    if flip == 1:
        heads += 1
        coinFlips.append("heads")
        i += 1
    else:
        tails += 1
        coinFlips.append("tails")
        i += 1
for n in coinFlips:
    print n,
	
print "heads: ", heads
print "tails: ", tails