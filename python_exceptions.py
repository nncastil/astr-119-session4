#when we get unexpected results

try:								#to attempt to run something
	print(a)
except:								#even though a is not defined
	print("a is not defined!")

try:
	print(a)
except NameError:					#when error message shows up
	print("a is still not defined")
except:
	print("Something else went wrong.")
	
print(a)							#this will break the program since a is not defined