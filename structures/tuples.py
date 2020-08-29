# Example 1
# def file_size(file_info):
# 	file_name, file_type, file_size= file_info
# 	return("{:.2f}".format(file_size / 1024))

# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

# Example 2 (Enumerate Function)
# def skip_elements(elements):
#     new_list = []
#     for index, element in enumerate(elements):
#         if index % 2 == 0:
#             new_list.append("{}".format(element))
            
#     return(new_list)

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# Example 3 Multiple of 7 using For loop and LIST Comprehension
# multiples = []
# for x in range(1,11):
#     multiples.append(x*7)

# print(multiples)

# #List Comprehension
# multiples = [x * 7 for x in range(1,11)]
# print(multiples)

# langugaes = ["Python", "Pearl", "JavScript", "Java", "Go"]
# length = [len(ele) for ele in langugaes]
# print(length)

def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []