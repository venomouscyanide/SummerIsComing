
class conqueror_army():

	def __init__(self,name):
		self.__name=name
		self.__ally_list=[]
		self.__king_status=False

	def add_ally(self,ally_name):
		self.__ally_list.append(ally_name)

	def is_ruler(self):
		if(len(self.__ally_list)>=3):
			self.__king_status=True

	def get_details(self):
		return(self.__king_status,self.__ally_list,self.__name)