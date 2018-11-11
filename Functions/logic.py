from Classes.southeros import southeros
from Classes.conqueror import conqueror_army

def decide_to_side(animal_dic,message_dic):
	'''
	we have the dictionaries of occurances of the letters
	in the message and the animal
	see if there are atleast enough letter occurances of the 
	animal is in the message.
	if yes, we have the kingdom siding with the conqueror
	else, kingdom does not side with the conqueror
	'''
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
	'''
	Find if the kingdom decided to side with conqueror
	based on the message containing the kingdom animal
	
	side_with_conqueror() returns two dictionaries.
	One with number of occurances of letters in message
	and another with number of occurances of letters in animal 
	'''
	for i in southeros_objects:
		animal_dic,message_dic=i.decide_to_side_helper()
	
		flag=decide_to_side(animal_dic,message_dic)

		if(flag==1):
			i.side_with_conqueror()
			conqueror.add_ally(i.get_details()[0])

	'''
	Finally calculate if there are enough allies
	to become the ruler for the conqueror
	'''
	conqueror.is_ruler()



		

