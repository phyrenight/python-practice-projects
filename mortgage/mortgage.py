principal = int(raw_input("Enter the prinpal amount: "))
interest = float(raw_input("Enter the interest percent: "))
total_payments = int(raw_input("Enter the number of payments: "))

part1 =  float(principal *(interest *(1 + interest)**total_payments))
print part1
part2 =  float((1 + interest)**total_payments -1)
monthly_payments = part1 / part2

print "Monthly payments are: %s " % monthly_payments