import secrets
import string
import hashlib
import os

def make_password(length,website,username):
    #make the list of characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation
    #strict compliance to guarantee one letter of each type
    #Swapped random.choice with secret.choice for military grade randomness
    guaranteed_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digit),
        secrets.choice(special)
    ]
    #fill the remaining length with random chars
    all_pool = lower+upper+digit+special
    remaining_length = length - 4 
    remaining_chars = [secrets.choice(all_pool) for _ in range(remaining_length)]
    #combine and shuffle to make sure the four guaranteed letters don't come first always
    password_list = guaranteed_chars + remaining_chars
    secrets.SystemRandom().shuffle(password_list)
    result = "".join(password_list)
    #new rating system (based on length)
    if length <10:
        score = 1
        rating = "Weak (Too Short)"
    elif 10<= length <13:
        score = 2
        rating = "Good"
    elif 13<= length <16:
        score = 3
        rating = "Strong"
    else:
        score = 4
        rating = "Excellent (Matrix Level Security)"
    #printing stuff below
    print(f"Generated Password:{result}") 
    print(f"Strength Score: {rating}({score}/4)")   

    #The Hashing Engine
    password_bytes = result.encode('utf-8')
    secure_hash = hashlib.sha256(password_bytes).hexdigest()
    print("SHA-256 Hash:",secure_hash)
    file_exists = os.path.isfile("google_passwords.csv")
    with open("google_passwords.csv","a") as file:
        if not file_exists:
            file.write("url,username,password\n")
            file.write(f"{website},{username},{result}\n")
            print("DEBUG: Data written to CSV successfully!")
        # If you don't see this, this part of code isn't running

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



        