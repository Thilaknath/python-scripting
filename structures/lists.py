# in keyword equivalent to contains in javascript

# Example 1
# def get_word(sentence, n):
# 	# Only proceed if n is positive 
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words 
# 		if n <= len(words):
# 			return(words[n - 1])
# 	return("")

# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

# List methods append(), insert() -> adds element to a particular location in a list, remove(), pop()
# Example 2
def skip_elements(elements):
    new_list = []
    i = 0

    for element in elements:
        if elements.index(element) % 2 == 0:
            new_list.append(element)
            i += 1
            # print(element)
    return new_list

        

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []








