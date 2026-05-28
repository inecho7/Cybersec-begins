import secrets
import string
import hashlib
import os

def make_password(length,website,username):
    pool = string.ascii_letters + string.digits + string.punctuation
    #Swapped random.choice with secret.choice for military grade randomness
    result = "".join(secrets.choice(pool) for i in range(length))
    (print("🔒 New Password:", result))

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in result:
        #checks happen here for each letter
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in string.punctuation:
            has_special = True
    score = sum([has_lower,has_upper,has_digit,has_special]) 

    if score == 4:
        print("Strength:EXCELLENT")
    if score == 3:
        print("Strength:GOOD")
    if score == 2:
        print("Strength:WEAK")
    if score == 1:
        print("TRY AGAIN")        

    #The Hashing Engine
    password_bytes = result.encode('utf-8')
    secure_hash = hashlib.sha256(password_bytes).hexdigest()
    print("SHA-256 Hash:",secure_hash)
    file_exists = os.path.isfile("google_passwords.csv")
    with open("google_passwords.csv","a") as file:
        if not file_exists:
            file.write("url,username,password\n")
            file.write(f"{website},{username},{result}\n")

while True:
#1.ask user for input and save it as a variable called 'user_input'
    user_input = input ("Enter desired password length (minimum 8):")
    #Gate 1: Is it a number?
    if user_input.isdigit():
        length = int(user_input)

        #Gate 2: Is it long enough? (Notice this is indented inside Gate 1)
        if length >=8:
            #ask the user for three different pieces of information
            website = input("Enter the website/app name:")
            username = input("Enter the username/email:")

            #3 Pass all three into the function
            make_password(length, website, username)
            break
        else:
            print ("❌️ Too Weak! Passwords must be 8 or more characters")
    else:
            print ("❌️ Error: Those are not valid numbers. Use digits only")   
    #Converts the text "12" into maths number 12



        