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