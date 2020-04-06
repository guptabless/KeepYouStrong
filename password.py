import random
import string

print("-----------------------------------------------")
print("Password Generator")
print("Code By : NG")
print("Usage: python password.py and then follow the instructions")
print("-----------------------------------------------")

print("Please enter the length of password")
length = int(input("length of password"))

print("You want to include special char in your password, please select at-least one option ")
print("what option you want to perform\n"  " 1.'Y' Yes\n","2.'N' NO\n")

sel = input("select at least one operation\n")
if sel == '1':
    letter = '!@#$%&*'
    letters = set("!@#$%&*")

    count = {}.fromkeys(letters,0)
    res = ''.join(
        random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k=length))
    special_char1 = ''.join(random.choices(letter))
    special_char2 = ''.join(random.choices(letter))
    generate_password = str(special_char2) + str(res)+str(special_char1)
    print("The generated password is : " + str(generate_password))

if sel == '2':
    res = ''.join(
    random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k=length))
    print("The generated password is : " + str(res))
