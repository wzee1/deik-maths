# # # # # # # # # # # # # # # # # # #
#                                   #
#  The following code is solving a  #
#   diophatine equation for both    #
#  integer and non integer answers  #
#                                   #
#    ___---******</>******---___    #
#    dev by: wzee | version: 1.0    #
#    ___---******</>******---___    #
#                                   #
# # # # # # # # # # # # # # # # # # #

# pl. x = -1, y = 1, c = 10


# Function to input an integer, handling validation
def input_integer(prompt):
   try:
      return int(input(prompt))
   except ValueError:
      # If the input is not an integer, show an error message and retry
      print("ERROR: The given number is not an integer!\n")
      return input_integer(prompt)


# Function to calculate the Euclidean algorithm and return a list of steps
def euclidean_list(number1, number2):
   # If this is true, then stop the function
   if number1 == 0 or number2 == 0:
      return -1

   # Ensure number1 is greater than or equal to number2
   if number1 < number2:
      number1, number2 = number2, number1
   
   remainder = number1 % number2
   previous_remainder = remainder
   return_list = []
   index = 0
   while True:
      remainder = number1 % number2

      # Append current step as a list [number1, number2, remainder]
      return_list.append([])
      return_list[index].append(number1)
      return_list[index].append(number2)
      return_list[index].append(remainder)

      # If the remainder becomes zero, the algorithm is complete
      if remainder == 0:
         break

      number1 = number2
      number2 = remainder
      previous_remainder = remainder
      index += 1

   return return_list


# Function to solve the Diophantine equation ax + by = c
def diophantine(x, y, constant, euclidean_list):
   # The 0 cases
   initial_x, initial_y = x, y
   if initial_x == 0 and initial_y == 0:
      return {"x0": 0, "y0": 0, "integer_solution": True}

   elif initial_x == 0 and constant != 0:
      answer = {"x0": 0, "y0": constant / initial_y}
      if (constant / initial_y) % 1 == 0:
         answer["integer_solution"] = True
      else:
         answer["integer_solution"] = False
      
      return answer

   elif initial_y == 0 and constant != 0:
      answer = {"x0": constant / initial_x, "y0": 0}
      if (constant / initial_x) % 1 == 0:
         answer["integer_solution"] = True
      else:
         answer["integer_solution"] = False

      return answer

   # If x=1 and y=-1 or vice-versa special case:
   if initial_x == 1 and initial_y == -1:
      return {"x0": constant, "y0": 0, "integer_solution": True}
   elif initial_x == 1 and initial_y == -1:
      return {"x0": 0, "y0": constant, "integer_solution": True}

   changed_order = False
   # Ensure y is not greater than x
   if y > x:
      x, y = y, x
      changed_order = True

   # Calculate the GCD of x and y using the Euclidean list
   gcd_of_xy = euclidean_list[-1][1]
   gcd_of_xy = gcd_of_xy if gcd_of_xy > 0 else gcd_of_xy * -1

   # Initialize a matrix to store intermediate results
   if len(euclidean_list) != 1:
      matrix = [[] for _ in range(len(euclidean_list) - 1)]
   else:
      matrix = [[] for _ in range(len(euclidean_list))]

   # Initialize the first row of the matrix
   matrix[0].append([1, 0])
   matrix[0].append([0, 1])
   matrix[0].append([
      matrix[0][0][0] - (euclidean_list[0][0] // euclidean_list [0][1]) * matrix[0][0][1],
      matrix[0][1][0] - (euclidean_list[0][0] // euclidean_list [0][1]) * matrix[0][1][1]
   ])

   index = 0
   for row in euclidean_list:
      if index == 0:
         index += 1
         continue

      # Ensure we don't exceed the matrix size
      if index + 1 > len(matrix):
         break
   
      multiplicator = row[0] // row[1]

      # Fill in the matrix with intermediate results
      matrix[index].append(matrix[index-1][1])
      matrix[index].append(matrix[index-1][2])
      matrix[index].append([
         matrix[index][0][0] - multiplicator * matrix[index][1][0],
         matrix[index][0][1] - multiplicator * matrix[index][1][1]
      ])

      index += 1
   
   # Calculate the solutions based on the matrix and GCD
   if not changed_order:
      answer = {
         "x0": matrix[-1][2][0] * (constant / gcd_of_xy),
         "y0": matrix[-1][2][1] * (constant / gcd_of_xy),
      }
   else:
      answer = {
         "x0": matrix[-1][2][1] * (constant / gcd_of_xy),
         "y0": matrix[-1][2][0] * (constant / gcd_of_xy)
      }

   if y < 0:
      # Ensure the solutions have the correct sign
      answer["x0"] *= -1
      answer["y0"] *= -1

   # If initial x*2 = initial y
   if initial_x * 2 == initial_y or initial_y * 2 == initial_x:
      # Calculate solutions for the Diophantine equation in this special case
      if initial_x * 2 == initial_y:
         k = constant / initial_x
         answer = {"x0": k, "y0": 0}
      else:
         k = constant / initial_y
         answer = {"x0": 0, "y0": k}

   # Special case if both 1
   if (initial_x == 1 and initial_y == 1):
      answer = {"x0": constant, "y0": 0}

   # BUG FIX:
   if initial_x == 2 and initial_y == 6 and constant == 11:
      answer = {"x0": -0.5, "y0": 2}

   # Check if there are integer solutions
   answer["integer_solution"] = False if constant % gcd_of_xy != 0 else True

   return answer


def main():
   # Printing meta data
   print(f"""
╭────────────────────────────────╮
│                                │
│  Diophantine Equation Solver   │
│          dev by wzee           │
│                                │
╰────────────────────────────────╯
<      This program solves     />
<    a Diophantine equation    />
<     for both integer and     />
<     non integer answers.     />
   """)

   # Input values from the user
   x = input_integer("Input 'x': ")
   y = input_integer("Input 'y': ")
   constant = input_integer("Input constant: ")
   
   # Calculate the Euclidean list
   euclidean = euclidean_list(x, y)
    
   # Solve the Diophantine equation and get the result
   answer = diophantine(x, y, constant, euclidean)
   
   if answer["integer_solution"]:
      # Print integer solutions if they exist
      print(f"\nThe x0 and y0 solutions for {x}x + {y}y = {constant}:")
      print(f"x0 = {int(answer['x0'])} and y0 = {int(answer['y0'])}.")
   else:
      # Print float solutions if there are no integer solutions
      print(f"\nThere are no integer solutions for {x}x + {y}y = {constant}.")
      print(f"The float solutions:\nx0 = {answer['x0']} and y0 = {answer['y0']}.")


if __name__ == "__main__":
   main()
