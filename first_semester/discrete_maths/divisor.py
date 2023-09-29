# # # # # # # # # # # # # # # # # # #
#                                   #
#     The following code returns    #
#        an integer's divisor       #
#     count, their divisors and     #
#  the relative primes related to   #
#          a specific number.       #
#                                   #
#    ___---******</>******---___    #
#    dev by: wzee | version: 1.0    #
#    ___---******</>******---___    #
#                                   #
# # # # # # # # # # # # # # # # # # #


def input_integer(prompt):
   try:
      return int(input(prompt))
   except ValueError:
      print("ERROR: Given number is not an integer!\n")
      return input_integer(prompt)

# Returns True is number is prime, False if not
def is_prime(number):
    if (number <= 1):
        return False
 
    for i in range(2, int(number**0.5) + 1):
        if (number % i == 0):
            return False
 
    return True


# Generates prime in [start, end[ range
def primes_in_range(start, end):
   primes = []
   for number in range(start, end):
      if is_prime(number):
         primes.append(number)

   return primes


# Returns a given number's divisor count using a mathematical formula
def divisor_count(number):
   # Generate primes for the canonic form in range of 2 and the given number
   primes = primes_in_range(2, number)
   # Initializing canonic form where key is a prime number and the value is the exponent
   canonic_form = {}
   # Looping through the prime numbers
   for prime in primes:
      # If the number is 1, then the canonic form is finished
      if number == 1:
         break

      # Looping until you cannot divide with current iteration's prime number
      while True:
         # Dividing number with the current prim
         quotient = number / prime
         # If this returns true, then it's not divisible by the current prime
         if int(quotient) != quotient:
            break

         # Divide the number
         number /= prime

         # Append it to the canonic form dictionary
         if str(prime) in canonic_form.keys():
            # If the prime already exists as key, then add one
            canonic_form[f"{prime}"] += 1
         else:
            # If not, then initialize it
            canonic_form[f"{prime}"] = 1

   # Getting the exponents in a list, then adding 1 to their value (bc it's needed for the mathematical formula)
   exponents = list(canonic_form.values())
   exponents_plus_one = list(map(lambda x: x + 1, exponents))

   # (exponent_plus_one[0] * exponent_plus_one[1] * ... * exponent_plus_one[n])
   divisor_count = 1
   for exponent in exponents_plus_one:
      divisor_count *= exponent

   return divisor_count


# Function to get the gcd of a number using the algorithm of Euclidean
def gcd(number1, number2):
   # Special case
   if number1 == 1 or number2 == 1:
      return 1

   # If the 2nd number is greater then the first, I change their values
   if number1 < number2:
      number1, number2 = number2, number1
   
   # Initalizing remainder and previous remainder
   remainder = number1 % number2
   previous_remainder = remainder

   # A loop that runs until you get the gcd
   while True:
      # Getting new remainder value
      remainder = number1 % number2

      # If the new remainder is 0 the loop ends, and it returns previous remainder (gcd)
      if remainder == 0:
         break

      # Changing variable's values for the next iteration
      number1 = number2
      number2 = remainder
      previous_remainder = remainder

   return previous_remainder


# Returns a list of a given number's divisors
def get_divisors(number):
   divisors = [1, number]
   for i in range(2, int(number / 2)):
      if number % i == 0:
         divisors.append(i)

   return sorted(divisors)


def get_relative_prime_divisors(divisors_of_number, number2):
   relative_primes = []
   for divisor in divisors_of_number:
      if gcd(divisor, number2) == 1:
         relative_primes.append(divisor)
   
   return sorted(relative_primes)


def main():
   # Printing meta info
   print(f"""
╭────────────────────────────────╮
│                                │
│    Getting divisors, their     │
│     count, and whether they    │
│    are relative primes to a    │
│         given number.          │
│                                │
│          dev by wzee           │
│                                │
╰────────────────────────────────╯
<      This program returns     />
<  the greatest common divisor  />
<      of two given numbers     />
   """)


   number = input_integer("Input the integer: ")
   divisor_count_of_number = divisor_count(number)
   divisors_of_number = get_divisors(number)
 
   print(f"\nThe count of divisors of {number} is {divisor_count_of_number}.")
   print(f"The divisors of {number} are: ")
   print(*divisors_of_number, sep=", ", end=".\n\n")

   number2 = input_integer("Enter another number: ")
   relative_primes = get_relative_prime_divisors(divisors_of_number, number2)

   if len(relative_primes) > 1:
      print(f"Divisors of {number} that are relative primes to {number2} are:")
      print(*relative_primes, sep=", ", end=".\n")
   elif len(relative_primes) == 1:
      print(f"Divisor of {number} that is relative prime to {number2} is: {relative_primes[0]}.\n")
   else:
      print(f"There are no divisor of {number} that are relative primes to {number2}.\n")


if __name__ == "__main__":
   main()
