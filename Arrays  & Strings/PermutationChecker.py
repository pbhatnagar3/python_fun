# word permutation checker
""" 
one of the ways of doing this would be sort and check
	sorted(first_word) == sorted(second_word)
but we can also hash in all the letters and check
"""
first_word = str(raw_input("Enter the first word that you want to check "))
second_word = str(raw_input("Enter the second word "))
print sorted(first_word) == sorted(second_word) 
# the above is a O(nlogn) solution

record_keeper_dict = {}
for c in first_word:
	if c in record_keeper_dict:
		record_keeper_dict[c] += 1
	else:
		record_keeper_dict[c] = 1

flag = True
for c in second_word:
	if c not in record_keeper_dict:
		flag = False
	else:
		if record_keeper_dict[c] > 0:
			record_keeper_dict[c] -= 1
		else:
			del record_keeper_dict[c]

print flag

