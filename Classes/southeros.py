
class southeros():

	def __init__(self,name=None,animal=None,withConqueror=False,message=None):
		self.__name=name
		self.__message=message
		self.__withConqueror=withConqueror
		self.__animal=animal
		pass

	def get_details(self):
		'''
		returns necessary details
		'''
		return(self.__name,self.__message,self.__withConqueror,self.__animal)

	def add_message(self,message):
		'''
		add message meant for the kingdom
		'''
		self.__message=message

	def side_with_conqueror(self):
		'''
		to take allegiance or not
		'''
		self.__withConqueror=True

	def decide_to_side_helper(self):
		'''
		make two dictionaries with letter occurances
		in the animal and the message to be sent to the 
		find_allegiance() to decide if the kingdom takes
		side with conqueror
		'''
		animal_dic={}
		message_dic={}

		animal=self.__animal.lower()
		
		for i in animal:
			try:
				if(animal_dic[i]):
					animal_dic[i]+=1
			except:
				animal_dic[i]=1

		if(self.__message):
			message=self.__message.lower()
			for i in message:
				try:
					if(message_dic[i]):
						message_dic[i]+=1
				except:
					message_dic[i]=1

		return(animal_dic,message_dic)