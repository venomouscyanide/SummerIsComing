from Classes.southeros import southeros
from Classes.conqueror import conqueror_army

def initialize():

	#kingdoms
	land=southeros("Land","Panda")
	water=southeros("Water","Octopus")
	ice=southeros("Ice","Mammoth")
	air=southeros("Air","Owl")
	fire=southeros("Fire","Dragon")

	southeros_objects=[]
	southeros_objects.extend([land,water,ice,air,fire])

	conqueror=conqueror_army("King Shah")

	return(southeros_objects,conqueror)