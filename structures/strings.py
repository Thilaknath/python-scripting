# Example 1
def first_and_last(message):
    if(message == ""):
        return True
    elif(message[0] == message[len(message) - 1]):
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Example 2
str = "Ada adad"
print(str[len(str) - 1])

# Example 3 [Slice]
fruit = "Pineapple"
print(fruit[1:3])
print(fruit[:3])
print(fruit[4:])

# Example 4 [index]
ada = "Mappillai"
print(ada.index('a'))

# Example 5 [in]
str = "Cats & Dogs are here"
print("Log" in str)

# String methods Strip, To upper(), lower(), lstrip(), rstrip()
# count(), isnumeric(), endswith(), split()

# Example 6
# def initials(phrase):
#     words = phrase.upper()
#     result = ""
    
#     wordArr = words.split()
#     for word in wordArr:
#         result += word[0]
#     return result


# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# Example 7 Format method
# For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. 
# The colon acts as a separator from the field name, if you had specified one. 
# You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} 
# would align the text three spaces to the right, as well as specify a float number with two decimal places.
def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name = name, grade = grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# Example 8
# "base string with {} placeholders".format(variables)
example = "format() method"
formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)
# Output
# this is an example of using the format() method on a string

# Example 9
# "{0} {1}".format(first, second)
first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)
# Outputs:
# apple carrot banana
