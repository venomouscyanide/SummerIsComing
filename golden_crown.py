from Functions.logic import find_allegiance
from Functions.initialize import initialize
from Functions.input_helper import take_query_input
from Functions.input_helper import take_message_input

from Classes.southeros import southeros
from Classes.conqueror import conqueror_army

if __name__ == '__main__':
	'''
	The driver function
	'''

	'''
	initialize with all values as per problem
	'''
	southeros_objects=[]
	southeros_objects,conqueror=initialize()

	ally_list=[]
	conqueror_decider,ally_list,conqueror_name=conqueror.get_details()

	for i in range(2):
		'''
		take query input and give asnwer as per the question/query
		'''
		query_type=take_query_input(conqueror_decider,ally_list,conqueror_name)
	
	#Take the message input depending on how many for each kingdom
	take_message_input(southeros_objects)

	#find allegiance for conqueror to rule
	find_allegiance(southeros_objects,conqueror)

	#get details of allegiance after processing the messages
	conqueror_decider,ally_list,conqueror_name=conqueror.get_details()

	for i in range(2):
		'''
		take query input and give asnwer as per the question/query
		'''
		query_type=take_query_input(conqueror_decider,ally_list,conqueror_name)
	




	