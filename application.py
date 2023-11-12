import colorama 
from colorama import Fore, Style

def addition(base:int, number:list,number_two:list):
  """_summary_

  Args:
      base (int): _description_
      number (list): _description_
      number_two (list): _description_
  """
  length_of_number = len(number)
  remaining = 0
  sum_list = []
  for i in range(length_of_number):
    if i >= len(number_two):
      for j in range(i,length_of_number):
        sum_of_digit = number[j]+remaining
        if sum_of_digit >= base:
          remaining = 1
          sum_of_digit -= base
          number[j] = sum_of_digit
        else:
          remaining = 0
          number[j] = sum_of_digit
        sum_list.append(number[j])
      break
    sum_of_digit = number[i]+number_two[i]+remaining
    if sum_of_digit >= base:
      remaining = 1
      sum_of_digit -= base
      sum_list.append(sum_of_digit)
    else:
      remaining = 0
      sum_list.append(sum_of_digit)
  if remaining > 0:
    sum_list.append(remaining)
  final_number = 0
  for i in range(len(sum_list)-1, -1, -1):
    final_number = final_number * 10 + sum_list[i]
  print(final_number)

def subtraction(base:int, number:list, number_two:list):
  """_summary_

  Args:
      base (int): _description_
      number (list): _description_
      number_two (list): _description_
  """
  #Doesen't work for number < number_two
  length_of_number = len(number)
  subtraction_list = [] 
  need_number = 0
  for i in range(length_of_number):
    if i >=len(number_two):
      for j in range(i,length_of_number):
        if need_number == 1 and number[j] == 0:
          number[j] = base-1
        elif need_number == 1:
          number[j] -= 1
          need_number = 0
        subtraction_list.append(number[j])
      break
    if need_number == 1 and number[i] == 0:
      number[i] = base-1
    elif need_number == 1:
      number[i] -= 1
      need_number = 0
    if number[i] < number_two[i]:
      need_number = 1
    difference = number[i] + need_number*(base) - number_two[i]
    subtraction_list.append(difference)
  final_number = 0
  for i in range(len(subtraction_list)-1, -1, -1):
    final_number = final_number * 10 + subtraction_list[i]
  print(final_number)

def multiplication(base:int, number:list,number_two:int):
  """_summary_

  Args:
      base (int): _description_
      number (list): _description_
      number_two (int): _description_
  """
  length_of_number = len(number)
  carry = 0
  multiplication_list = []
  for i in range(length_of_number):
    multiplication = number[i]*number_two + carry # in base 10
    carry = multiplication // base
    multiplication_list.append(multiplication%base)
  if carry > 0:
    multiplication_list.append(carry)
  final_number = 0
  for i in range(len(multiplication_list)-1, -1, -1):
    final_number = final_number * 10 + multiplication_list[i]
  print(final_number)

def division(base:int, number:list,number_division:int):
  """_summary_

  Args:
      base (int): _description_
      number (list): _description_
      number_division (int): _description_
  """
  print("")

def proceed_conversion(base:int, number:list, base_two:int):
  """_summary_

  Args:
      base (int): _description_
      number (list): _description_
      base_two (int): _description_
  """
  print("")

def option_proceed(option:int):
  if option == 6:
    quit()
  rapid_conversions = [2,4,8,16]
  base = input("Type base for number: ").strip()
  if base.isnumeric():
    base = int(base)
  else:
    raise ValueError("Invalid Base! Yo need to write a number")
  number = input("Type the number: ").strip()
  if not number.isnumeric():
    raise ValueError("Invalid number! Type only a number!")
  number_list,number_is_ok = transform_number(int(number), base)
  if not number_is_ok:
    raise ValueError("You wrote a wrong number. Every digit need to be smaller than base.")
  if option >=1 and option <=2:
    number_two = input("Type the number two: ").strip()
    if not number_two.isnumeric():
      raise ValueError("Invalid number! Type only a number!")
    number_list_two,number_two_is_ok = transform_number(int(number_two), base)
    if not number_two_is_ok:
      raise ValueError("You wrote a wrong number. Every digit needs to be smaller than base.")
  if option == 1:
    addition(base, number_list,number_list_two)
  elif option == 2:
    subtraction(base, number_list,number_list_two)
  elif option == 3:
    number_multiplication = input("Type a digit: ").strip()
    if number_multiplication.isdigit():
      number_multiplication = int(number_multiplication)
    else:
      raise ValueError("Invalid number! Yo need to write a digit\n")
    multiplication(base,number_list,number_multiplication)
  elif option == 4:
    number_division = input("Type a digit: ").strip()
    if number_division.isdigit():
      number_division = int(number_division)
    else:
      raise ValueError("Invalid number! Yo need to write a digit\n")
    division(base,number_list,number_division)
  elif option == 5:
    base_two = input("Type the base two: ").strip()
    if not base_two.isnumeric():
      raise ValueError("Invalid base! Type only a number!")
    base_two = int(base_two)
    proceed_conversion(base, number_list, base_two)

def transform_number(number:int,base:int):
  list_of_number = []
  number_ok = 1
  while number > 0:
    list_of_number.append(number%10)
    if number%10 >= base:
      number_ok = 0
      break
    number //= 10
  return list_of_number,number_ok

def menu():
  print("[Algorithms & Conversions for base number]")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Conversion(From base1 to base2)")
  print("6. Close")
  option = input("Choose option: ").strip()
  if option.isnumeric() and int(option) in [1,2,3,4,5,6]:
    option = int(option)
    try:
      option_proceed(option)
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)
  else:
    raise ValueError("Invalid option! Choose between (1-6) \n")

if __name__ == "__main__":
  while True:
    try:
      menu()
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)