#Print from an Array List

friends = ['bae', 'amreen', 'vas', 'siva']
for friend in friends:
    print("Hi " + friend)

#Print from an Loop
for i in range(10):
    print("Hello World")

#Data Types
#int, string, float
print(8 + 7.5) #Implicit conversion int to float
print("The area of a triangle is " + str(7.5)) #Explicit conversion

#Functions
def area(base, height):
    area = (base * height)/2
    return area

area_a = area(7,3)
area_b = area(5,4)
print("Area of two plots equals " + str(area_a + area_b))

#Comparing Operators and Logical Operators If Statements

def is_positive(number):
    if(number > 0):
        return True

print (is_positive(13))
