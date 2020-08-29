# Example 1
animal = "Hippopotamus"
print(animal[-5])

# Example 2
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower():
      if letter.isalpha():
          if letter in result:
              result[letter] += 1
          else:
              result[letter] = 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# Example 3
def combine_guests(guests1, guests2):
    guests2.update(guests1)
    return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Example 4
def car_listing(car_prices):
  result = ""
  for make, price in car_prices.items():
    result += "{} costs {} dollars".format(make, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Example 5
def squares(start, end):
	return [ x * x for x in range(start, end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 6
def combine_lists(list1, list2):
    list1.reverse()
    
    return list2 + list1
  
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# Example 7
def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# Example 8 [ WRONG IMPLEMENTATION FIX IT]
def format_address(address_string):
    houseNo = address_string[0:address_string.find(" ")]
    streetName = address_string[address_string.find(" "):]
    
    return "house number {} on street named {}".format(houseNo, streetName)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

