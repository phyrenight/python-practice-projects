item_cost = float(raw_input("Enter the cost of the item: "))
tax = float(raw_input("Enter the tax on the item: "))

percent_to_decimal = tax / 100
tax_on_item = item_cost * percent_to_decimal
final_cost = item_cost + tax_on_item

print "The tax on the item is: ", tax_on_item
print "The item price plus tax is: ", final_cost