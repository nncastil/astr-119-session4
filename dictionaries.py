#to define dictionary data structure

example_dict = {						#key : value for elements
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10
}
print(type(example_dict))				#says "dict"

course = example_dict["class"]			#get a value via key
print(course)

example_dict["awesomeness"] += 1		#increases value

print(example_dict)

for x in example_dict.keys():			#prints dictionary key and elements
	print(x,example_dict[x])