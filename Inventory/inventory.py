class Inventory(object):
    invent = []
    capacity = 0
    total_inventory = 0
    available_space = 0
	inventory_value = 0
	
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_space = capacity

    def add_inventory(self, id, price, quantity):
        self.invent.append = product(id, price, quantity)
        self.available_space -= quantity

    def reorder(self, id, how_much):
	"""
	   used to reorder products and for products
	   return by customers.
	"""
	# change this so that it calls the function
	# in product to increment quantity
        for i in invent:
            if i == id:
                i.refill_product(how_much)
