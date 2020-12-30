import json
from collections import namedtuple


Event = namedtuple('Event', ['timestamp', 'event_type', 'item_id', 'item_price'])

def create_event_obj_namedtuple(json_string):
	event_dict = json.loads(json_string)
	event_obj = Event(
		timestamp = event_dict["timestamp"],
		event_type = event_dict["eventType"],
		item_id = event_dict["item_id"],
		item_price = event_dict['item_price']
		)
	return event_obj


# class Event:
# 	pass

# def create_event_obj(json_string):
# 	event_dict = json.loads(json_string)
# 	event_obj = Event()
# 	for key, value in event_dict.items():
# 		setattr(event_obj, key, value)
# 	return event_obj

