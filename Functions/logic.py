from Classes.southeros import southeros
from Classes.conqueror import conqueror_army

def decide_to_side(animal_dic,message_dic):
	flag=0

	for key,value in animal_dic.items():
		if(key in message_dic.keys()):
			if(message_dic[key]>=value):
				flag=1
			else:
				flag=0
				break
		else:
			flag=0
			break

	return(flag)

def find_allegiance(southeros_objects,conqueror):
	
	for i in southeros_objects:
		animal_dic,message_dic=i.decide_to_side_helper()
	
		flag=decide_to_side(animal_dic,message_dic)

		if(flag==1):
			i.side_with_conqueror()
			conqueror.add_ally(i.get_details()[0])

	conqueror.is_ruler()



		

