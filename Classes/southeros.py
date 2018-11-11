
class southeros():

	def __init__(self,name=None,animal=None,withShah=False,message=None):
		self.__name=name
		self.__message=message
		self.__withShah=withShah
		self.__animal=animal
		pass

	def get_details(self):
		return(self.__name,self.__message,self.__withShah,self.__animal)

	def add_message(self,message):
		self.__message=message

	def side_with_conqueror(self):
		self.__withShah=True

	def decide_to_side_helper(self):
		#check if __message contains the __animal
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