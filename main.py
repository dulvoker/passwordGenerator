import random

uppercase_letters = str()
for i in range(65, 91) : uppercase_letters += chr(i)
lowercase_letters = uppercase_letters.lower()
digits = str()
for i in range(10): digits += str(i)
symbols = "(){}[]!@#$%^&*\\\'\">?<,."
value_for_password = str()

upper, lower, nums, symbs = True, True, True, False
if upper: value_for_password += uppercase_letters
if lower: value_for_password += lowercase_letters
if nums: value_for_password += digits
if symbs: value_for_password += symbols

length = 15
password_amount = 10

for i in range(password_amount):
    password = "".join(random.sample(value_for_password, length))
    print(password)




