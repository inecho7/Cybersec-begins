import secrets
import string

def make_password(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    #Swapped random.choice with secret.choice for military grade randomness
    result = "".join(secrets.choice(pool) for i in range(length))
    (print("🔒 New Password:", result))

while True:
#1.ask user for input and save it as a variable called 'user_input'
    user_input = input ("Enter desired password length (minimum 8):")
    #Gate 1: Is it a number?
    if user_input.isdigit():
        length = int(user_input)

        #Gate 2: Is it long enough? (Notice this is indented inside Gate 1)
        if length >=8:
            #1 call your function here: make_password (le#2 Put your break here to exit!
            make_password(length)
            break
        else:
            print ("❌️ Too Weak! Passwords must be 8 or more characters")
    else:
            print ("❌️ Error: Those are not valid numbers. Use digits only")   
    #Converts the text "12" into maths number 12



        