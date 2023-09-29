# # # # # # # # # # # # # # # # # # #
#                                   #
#   The following code solves the   #
#      algorithm of Euclidean       #
#                                   #
#    ___---******</>******---___    #
#    dev by: wzee | version: 1.1    #
#    ___---******</>******---___    #
#                                   #
# # # # # # # # # # # # # # # # # # #


# Gets an integer input from the user
def input_integer(text):
   # If it's convertable to an integer it returns it
   try:
      return int(input(text))
   # If not, then returns an error message and reasks the user
   except ValueError:
      print("ERROR: Given input is not integer!\n")
      return input_integer(text)


# Function to get the gcd of a number using the algorithm of Euclidean
def euclidean(number1, number2):
   # Special case
   if number1 == 0 or number2 == 0:
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


def main():
   # Printing meta info
   print(f"""
╭────────────────────────────────╮
│                                │
│   Euclidean Algorithm Solver   │
│          dev by wzee           │
│                                │
╰────────────────────────────────╯
<      This program returns     />
<  the greatest common divisor  />
<      of two given numbers     />
   """)

   # Gets the 2 numbers, then returns answer
   number1 = input_integer("Input 1st integer: ")
   number2 = input_integer("Input 2nd integer: ")
   print(f"The GCD of {number1} and {number2} is {euclidean(number1, number2)}.")


if __name__ == "__main__":
   main()
   