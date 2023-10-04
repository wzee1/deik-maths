# # # # # # # # # # # # # # # # # # #
#                                   #
#    The following code returns     #
#        a complex number's         #
#          nth root index.          #
#                                   #
#    ___---******</>******---___    #
#    dev by: wzee | version: 1.1    #
#    ___---******</>******---___    #
#                                   #
# # # # # # # # # # # # # # # # # # #


from math import atan, cos, sin, pi, radians, degrees


# Float input function
def input_float(prompt):
   # Return if input is float
   try:
      return float(input(prompt))
   # Reask the input if it's not
   except ValueError:
      print("ERROR: Given input is not a float number!\n")
      return input_float(prompt)


# Integer input function
def input_positive_integer(prompt):
   # Return if input is integer
   try:
      number = int(input(prompt))
      if number <= 1:
         print("ERROR: Given input must be greater than 1!\n")
         return input_positive_integer(prompt)

      return number
   # Reask the input if it's not
   except ValueError:
      print("ERROR: Given input is not an integer number!\n")
      return input_positive_integer(prompt)


# "real"/"imaginary" is the real/imaginary part of the expression
def get_algebraic_complex_number(real, imaginary):
   return {
      "real": real,
      "imaginary": imaginary
   }
   

# "absolute_value"/"angle" is the value of |z| / phi angle
def get_trigonometric_complex_number(absolute_value, angle):
   return {
      "absolute_value": absolute_value,
      "angle": angle
   }


# Convert to algebraic form to trigonometric form
def algebraic_to_trigonometric(algebra):
   algebra_real = algebra["real"]
   algebra_imaginary = algebra["imaginary"]
   
   # Calculating abs value using the sqrt(a**2 + b**2) formula
   absolute_value = round(abs(
      (algebra_real**2 + algebra_imaginary**2)**0.5
   ))
   
   # If the real part is 0, then it's 90 degrees, otherwise return atan
   if abs(algebra_real) != 0:
      angle = degrees(atan(abs(algebra_imaginary) / abs(algebra_real)))
   else:
      angle = 90

   # Change angle in case we are not in the top right part
   if algebra_real < 0 and algebra_imaginary > 0:
      angle = 180 - angle
   elif algebra_real < 0 and algebra_imaginary < 0:
      angle = 180 + angle
   elif algebra_real > 0 and algebra_imaginary < 0:
      angle = 360 - angle

   return {
      "absolute_value": absolute_value,
      "angle": angle
   }


# Returns complex number in user's desired form
def get_complex_number():
   # Asking which form to input the complex number
   print("In what form do you want to provide the complex number?")
   complex_form = input("Enter (t / trigonometric or a / algebraic): ").lower()

   # Guard clause: restart the function if the value is not:
   if complex_form not in ["t", "trigonometric", "a", "algebraic"]:
      print('ERROR: Unknown form! You can type in "trigonometric" or "t" and "algebraic" or "a"!\n')
      return get_complex_number()

   # Returning the complex number based on the complex_form
   match complex_form:
      case "a" | "algebraic":
         # Getting the algebraic parts that are needed
         real_part = input_float("Enter the real part of your complex number: ")
         imaginary_part = input_float("Enter the imaginary part of your complex number: ")
         algebra = get_algebraic_complex_number(real_part, imaginary_part)

         return algebraic_to_trigonometric(algebra)
      
      case "t" | "trigonometric":
         # Getting the trigonometric parts that are needed
         absolute_value = input_float("Enter the |z| (absolute value) of your complex number: ")
         angle = input_float("Enter the φ angle (in degrees) of your complex number: ")
         
         return get_trigonometric_complex_number(absolute_value, angle)


def root_of_complex_number(complex_number, root_index):
   # Gets the absolute value
   absolute_value = complex_number["absolute_value"]
   # Gets angle in degrees and converting it to radians straight
   angle = round(complex_number["angle"] / 180, 4)

   # Array of the roots
   roots = []
   # Generating root_index count of roots
   for index in range(root_index):
      # Current dict is calculating the values based on the math formula:
      # k_root:
      # nth_root(absolute_value) * [(cos((angle + 2kπ) / root_index) + i * sin((angle + 2kπ) / root_index)))]
      current = {
         "absolute_value": round(absolute_value**(1 / root_index), 4),
         "angle": round((angle + index * 2) / root_index, 4)
      }

      # Correcting if the angle is greather than 2π
      if current["angle"] > 2:
         current["angle"] %= 2

      # Adding string to print it better
      current["str"] = f'ω{index} = {current["absolute_value"]} * (cos({current["angle"]}π) + i * sin({current["angle"]}π))'

      # Appending current root to the roots list
      roots.append(current)

   return roots   # Returning roots


def main():
   # Printing meta info
   print(f"""
╭────────────────────────────────╮
│                                │
│    Roots in Complex Numbers    │
│          dev by wzee           │
│                                │
╰────────────────────────────────╯
<     This program gets the    />
<       nth root index of      />
<       complex numbers.       />
   """)

   # Getting complex number and the root index
   complex_number = get_complex_number()
   root_index = input_positive_integer("Enter the root index: ")

   # Getting roots
   roots = root_of_complex_number(complex_number, root_index)

   print(f'\nThe roots of z = {complex_number["absolute_value"]} * (cos({round(complex_number["angle"] / 180, 3)}π)+ i * sin({round(complex_number["angle"] / 180, 3)}π)) are:')

   # Printing roots
   for root in roots:
      print(root["str"])


if __name__ == "__main__":
   main()
