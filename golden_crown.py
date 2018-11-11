from Functions.logic import find_allegiance
from Functions.initialize import initialize
from Functions.input_helper import take_query_input
from Functions.input_helper import take_message_input

from Classes.southeros import southeros
from Classes.conqueror import conqueror_army

if __name__ == '__main__':

	southeros_objects=[]
	southeros_objects,conqueror=initialize()

	ally_list=[]
	conqueror_decider,ally_list,conqueror_name=conqueror.get_details()

	for i in range(2):
		query_type=take_query_input(conqueror_decider,ally_list,conqueror_name)
	
	take_message_input(southeros_objects)

	find_allegiance(southeros_objects,conqueror)

	conqueror_decider,ally_list,conqueror_name=conqueror.get_details()

	for i in range(2):
		query_type=take_query_input(conqueror_decider,ally_list,conqueror_name)
	




	