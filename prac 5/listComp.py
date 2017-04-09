products = [["phoen", 340, False], ["PC", 1420.95, True], ["palnt", 23, True]]
onSale = [product for product in products if True in product]
print(onSale)