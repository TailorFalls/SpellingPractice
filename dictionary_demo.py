my_dict = {}
my_dict["sulk"] = "To be angry or upset about something and to refuse to discuss it with other people"
my_dict["excitement"] = "A feeling of eager enthusiasm and interest : the state of being excited"
my_dict["character"] = "foo"
my_dict["dilemma"] = "bar"
print("Hello! I've loaded my dictionary.")
print("Let's look at the keys for it.")
print(my_dict.keys())
print("How many keys are there? Let's get the length of the dictionary.")
print(len(my_dict))
print("Let's see what the first key is.")
print(list(my_dict.keys())[0])
print("Whew! That was hard.")
print("Let's just see what all of the keys are.")

for thing in my_dict.keys():
  print(thing)

print("Great. Now let's do something with each of the keys.")
for cat in my_dict.keys():
  print("When I look in key: " + cat + " I find: " + my_dict[cat])
