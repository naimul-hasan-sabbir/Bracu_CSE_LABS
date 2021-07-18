import re

test_case = int(input("Enter test cases: "))

for i in range(0,test_case):

    regular_expression_input = input("Enter regular expression :")

    regex = re.compile(regular_expression_input)

    string_numbers = int(input("Enter String numbers to check:"))

    for j in range(0,string_numbers):

       string_from_user = input()

       if regex.findall(string_from_user):

          print("YES "+str(i))
       else:

          print("NO "+str(i))