from Classes.southeros import southeros
from Classes.conqueror import conqueror_army

def query_input_helper(query_type,conqueror_decider,ally_list,conqueror_name):

	if(query_type==1):

		if conqueror_decider:
			print(conqueror_name)
		else:
			print("None")

	elif(query_type==2):

		if(len(ally_list)==0):
			print (None)
		else:
			print(', '.join(ally_list))

def take_query_input(conqueror_decider,ally_list,conqueror_name):

	query=input().split()

	if("ruler" in query):
		query_type=1
	elif("Allies" in query):
		query_type=2

	query_input_helper(query_type,conqueror_decider,ally_list,conqueror_name)

def take_message_input(southeros_objects):

	number_conqueror_messages=int(input())
	messages=[]

	kingdom_names=[]

	for i in southeros_objects:
		kingdom_names.append(i.get_details()[0])

	for i in range(number_conqueror_messages):
		messages=input().split()
		
		current_kingdom_name=messages[0][0:len(messages[0])-1].rstrip()

		if(current_kingdom_name in kingdom_names):
			index=kingdom_names.index(current_kingdom_name)
			secret_message=' '.join(messages[1:])
			southeros_objects[index].add_message(secret_message.strip('"'))

