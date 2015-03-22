# checking if the letter entered is unique or not
"""  python based solution
	
	len(set(input_string)) == len(input_string)
	we could check the length of the string. If the string is ASCII and the length is greater than 128, then the string will not be unique

 """

class UniqueCharacters(object):
	record_keeper = {}
	int_record_keeper = 0
	def __init__(self, input_string):
		self.stored_string = input_string


	def unique_character_checker(self, check_type = 1):
		if check_type == 1:
			for char in self.stored_string:
				if char in self.record_keeper:
					return False
				else:
					self.record_keeper[char] = True
		elif check_type == 2:
			for char in self.stored_string:
				if (self.int_record_keeper & (1<<ord(char))) > 0:
					return False
				else:
					self.int_record_keeper |= 1<< ord(char)
		else:
			return len(set(self.stored_string)) == len(self.stored_string)
		return True		


tester = UniqueCharacters(str(raw_input("enter the thing to be tested ")))
print tester.unique_character_checker(int(raw_input("enter 1 for hashTable checker and 2 for boolean checker ")))

