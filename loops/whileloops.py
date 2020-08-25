#Exercise 1
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

#Exercise 2
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      factor+= 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

#Exercise 3
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while ((n!= 0) & (n % 2 == 0)):
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

#Exercise 4
def sum_divisors(n):
  x = 1
  sum = 0
  if n == 0:
    sum += n
  else:
    while n > x:
      while n % x == 0 and n != x:
        sum += x
        x += 1
      x += 1
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
114