
class conqueror_army():

	def __init__(self,name):
		self.__name=name
		self.__ally_list=[]
		self.__king_status=False

	def add_ally(self,ally_name):
		'''
		add ally kingdom to be displayed when queried
		'''
		self.__ally_list.append(ally_name)

	def is_ruler(self):
		'''
		function to find if conqueror has enough
		allies to become the is_ruler
		'''
		if(len(self.__ally_list)>=3):
			self.__king_status=True

	def get_details(self):
		'''
		return relevant details when called
		'''
		return(self.__king_status,self.__ally_list,self.__name)