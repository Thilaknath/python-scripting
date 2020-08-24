#Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. 
#A for loop works well when you want to iterate over a sequence of elements.

# To quickly recap the range() function when passing one, two, or three parameters:

# One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
# Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
# Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, 
# but this time increasing each step by the third parameter.

# result = 1

# for x in range(1, 5):
#     print("loop executed" + str(x))
#     result = result * x

# print(result)

for x in range(100):
    if(x%7 == 0):
        print(x)