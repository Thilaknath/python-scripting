# Example 1
# keys inside dictionary are unique
file_counts = {"jpg": 10, "txt": 5, "csv": 9, "php": 29}
print(type(file_counts))
print ("jpg" in file_counts)

# Adding elements to a dictionary
file_counts["py"] = 17
print(file_counts)

# Delete elements using the del() keyword
del file_counts["txt"]
print(file_counts)

# # Example 2
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39
toc["Chapter 3"] = 24
print(toc)
print("Chapter 5" in toc)
# Epilogue starts on page 39
# Chapter 3 now starts on page 24
# What are the current contents of the dictionary?
# Is there a Chapter 5?

# Example 3 _> Dictionary iteerations 
file_counts = {"jpg": 10, "txt": 5, "csv": 9, "php": 29}
# 
for ext, amount in file_counts.items():
    print("Type {} has {} files".format(ext, amount))
# 
for value in file_counts.values():
    print (value)
# 
for keys in file_counts.keys():
    print (keys)

# Example 4
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, feature in cool_beasts.items():
    print("{} have {}".format(animal, feature))

# Example 5
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, color in wardrobe.items():
	for x in color:
		print("{} {}".format(x, item))

