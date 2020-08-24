# A function calling itself, breaking down the function to its smallest possible and then solving it
# Amazing read to understand recursion : https://codeburst.io/learn-and-understand-recursion-in-javascript-b588218e87ea
#Exercise 1
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 2:
        return 1

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6

#Exercise 2
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  result = number//base

  # Recursive case: keep dividing number by base.
  return is_power_of(result, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# Exercise 3
# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     if is_group(member):
#       count += count_users(member)
#     else:
#       count += 1
#   return count

# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18
