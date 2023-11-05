

def addition(base:int, number:list,number_two:list):
  length_of_number = len(number)
  remaining = 0
  sum_list = []
  for i in range(length_of_number):
    if i >= len(number_two):
      sum_list.append(number[i::])
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
  print(sum_list)
  print(final_number)

def subtraction(base:int, number:list, number_two:list):
  print("")

def multiplication(base:int, number:list,number_two:list):
  print("")

def division(base:int, number:list,number_division:int):
  print("")

def rapid_conversion(base:int, number:list, base_two:int):
  print("")

def option_proceed(option:int):
  if option == 6:
    quit()
  rapid_conversions = [2,4,8,16]
  base = input("Type base for number: ").strip()
  if base.isnumeric():
    base = int(base)
  else:
    print("Invalid Base! Yo need to write a number\n")
    return 0
  number = input("Type the number: ").strip()
  if not number.isnumeric():
    print("Invalid number! Type only a number!")
    return 0
  number_list,number_is_ok = transform_number(int(number), base)
  if not number_is_ok:
    print("You wrote a wrong number. Every digit need to be smaller than base.")
    return 0
  if option >=1 and option <=3:
    number_two = input("Type the number two: ").strip()
    if not number_two.isnumeric():
      print("Invalid number! Type only a number!")
      return 0
    number_list_two,number_two_is_ok = transform_number(int(number_two), base)
    if not number_two_is_ok:
      print("You wrote a wrong number. Every digit need to be smaller than base.")
      return 0
  if option == 1:
    addition(base, number_list,number_list_two)
  elif option == 2:
    subtraction(base, number_list,number_list_two)
  elif option == 3:
    multiplication(base,number_list,number_list_two)
  elif option == 4:
    number_division = input("Type a digit: ").strip()
    if number_division.isalpha():
      number_division = int(number_division)
    else:
      print("Invalid number! Yo need to write a digit\n")
      return 0
    division(base,number_list,number_division)
  elif option == 5:
    base_two = input("Type the base two: ").strip()
    if not base_two.isnumeric():
      print("Invalid base! Type only a number!")
      return 0
    base_two = int(base_two)
    if base in rapid_conversions and base_two in rapid_conversions:
      rapid_conversion(base, number_list, base_two)

def transform_number(number:int,base:int):
  list_of_number = []
  number_ok = 1
  while number > 0:
    list_of_number.append(number%10)
    if number%10 >= base:
      number_ok = 0
      break
    number //= 10
  print(list_of_number)
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
  if option.isnumeric():
    option = int(option)
    option_proceed(option)
  else:
    print("Invalid option! Choose between (1-6) \n")
    return 0

while True:
  menu()