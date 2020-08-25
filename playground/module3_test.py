# Exercise 1
number = 1
while number < 7:
	print(number, end=" ")
	number += 1

# Exercise 2
def show_letters(word):
	for x in word:
		print(x, end="\n")

show_letters("Hello")
# Should print one line per letter

# Exercise 3
def digits(n):
	count = 0
	if n == 0:
		return 1
	while (n % 10):
		count += 1
		n = n % 10
		break
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

# Exercise 4
def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 4)
# Should print the multiplication table shown above

# Exercise 5
def counter(start, stop):
	x = start
	if ___:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# Exercise 6
for x in range(10):
    for y in range(x):
        print(y)

# Exercise 7
for x in range(1, 10, 3):
    print(x)

# Exercise 8
def even_numbers(maximum):
	return_string = ""
	for x in ___:
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed