avg_tile_size = 1 # are in feet
cost_per_tile = float(raw_input("What is the cost per tile: "))
width_of_floor = int(raw_input("What is the floor's width(in feet): "))
height_of_floor = int(raw_input("what is the floor's height(in feet): "))

amountOfTiles = float((width_of_floor * height_of_floor)/avg_tile_size)
print "Total amount of tiles needed: %s " % amountOfTiles

total_price = float(amountOfTiles * cost_per_tile)
print "The total cost for the tiles is: %s" % total_price