
# from pars import create_event_obj


# path = 'B2.15-data-3000-with-fav.json/data_3000.json'




# item_prices = []
# with open(path, 'r') as jsonf:
# 	for inx, line in enumerate(jsonf):
# 		if inx == 20:
# 			break
# 		event_obj = create_event_obj(line)
# 		item_prices.append(event_obj.item_price)


# total_sum = 0
# for item in item_prices:
# 	total_sum += int(item)
	
# print(total_sum)


from pars import create_event_obj_namedtuple


path = 'B2.15-data-3000-with-fav.json/data_3000.json'


item_prices = []
with open(path, 'r') as jsonf:
	for inx, line in enumerate(jsonf):
		if inx == 20:
			break
		event_obj = create_event_obj_namedtuple(line)
		item_prices.append(event_obj.item_price)


total_sum = 0
for item in item_prices:
	total_sum += int(item)
	
print(total_sum)