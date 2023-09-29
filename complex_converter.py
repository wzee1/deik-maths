# # # # # # # # # # # # # # # # # # #
#                                   #
#    The following code converts    #
#       complex number's from       #
#    algebraic to trigonometric     #
#         and vice-versa.           #
#                                   #
#    ___---******</>******---___    #
#    dev by: wzee | version: 1.1    #
#    ___---******</>******---___    #
#                                   #
# # # # # # # # # # # # # # # # # # #


from math import atan, cos, sin, pi, radians, degrees

# Convert chooser function
def choose_convertion_type():
   # User making choice whether they want to convert to algebraic or trigonometric form
   choice = input("Choose to convert to algebraic or trigonometric: ").lower()

   # If the input is not the following, then reask the input:
   if choice in ["t", "trigonometric", "a", "algebraic"]:
      return choice
   else:
      print("ERROR: Wrong convertion type! Available inputs: t / trigonometric or a / algebraic!\n")
      return choose_convertion_type()


# Float input function
def input_float(prompt):
   # Return if input is float
   try:
      return float(input(prompt))
   # Reask the input if it's not
   except ValueError:
      print("ERROR: Given input is not a float number!\n")
      return input_float(prompt)


# Initalize complex number

# Where "str" is a string form of the expression,
# "real"/"imaginary" is the real/imaginary part of the expression
def get_algebraic_complex_number(a, b):
   return {
      "str": f"{a} + {b} * i",
      "real": a,
      "imaginary": b
   }
   
# Where "str" is a string form of the expression,
# "absolute_value"/"angle" is the value of |z| / phi angle
def get_trigonometric_complex_number(absolute_value, angle):
   return {
      "str": f"z = {absolute_value} * (cos({angle}) + i * sin({angle}))",
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
      "str": f"z = {absolute_value} * (cos({round(angle/180, 3)}π) + i * sin({round(angle/180, 3)}π))",
      "absolute_value": absolute_value,
      "angle": angle
   }


# Convert trigonometric form to algebraic form
def trigonometric_to_algebraic(trigonometric):
   absolute_value = trigonometric["absolute_value"] 
   angle = radians(trigonometric["angle"])   # Converting degree to radian
   
   # Getting the real part and imaginary part
   real = round(absolute_value * cos(angle), 3)
   imaginary = round(absolute_value * sin(angle), 3)   # This will be multipled by "i"

   # Guard clause in case it's not a complex number:
   if trigonometric["angle"] in [0, 180]:
      return {
         "str": f"z = {real}",
         "real": real,
         "imaginary": 0
      }

   # Guard clause in case it doesn't have real part:
   if real == 0:
      return {
         "str": f"z = {imaginary} * i",
         "real": 0,
         "imaginary": imaginary
      }

   return {
      "str": f"z = {real} + {imaginary} * i",
      "real": real,
      "imaginary": imaginary
   }


# Main program
def main():
   # Printing meta info
   print(f"""
╭────────────────────────────────╮
│                                │
│    Complex Number Converter    │
│          dev by wzee           │
│                                │
╰────────────────────────────────╯
<     This program converts    />
<     complex numbers from     />
<  algebraic to trigonometric  />
<       and vice-versa.        />
   """)


   # User chooses convertion type
   convertion_type = choose_convertion_type()

   # Running convertion based on user's input
   match convertion_type:
      case "t" | "trigonometric":
         # Getting input
         real_part = input_float("Input the real part of the complex number (a): ")
         imaginary_part = input_float("Input the imaginary part of the complex number (b): ")

         # Getting starting complex number in algebraic form based on the given inputs
         algebraic_value = get_algebraic_complex_number(real_part, imaginary_part)
         # Converting from algebraic form to trigonometric
         trigonometric_value = algebraic_to_trigonometric(algebraic_value)
         print(f'\n{trigonometric_value["str"]}')
      
      case "a" | "algebraic":
         # Getting input
         absolute_value = input_float("Input the absolute value of the complex number (|z|): ")
         angle = input_float("Input the degrees value of phi angle (φ): ")

         # Getting starting complex number in trigonometric form based on given inputs
         trigonometric_value = get_trigonometric_complex_number(absolute_value, angle)
         # Converting from trigonometric to algebraic
         algebraic_value = trigonometric_to_algebraic(trigonometric_value)
         print(f'\n{algebraic_value["str"]}')
      
      case _:
         return


if __name__ == "__main__":
   main()
