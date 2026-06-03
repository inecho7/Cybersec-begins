import secrets
import string
import hashlib
import os
def estimate_crack_time(input_data,is_passphrase=False):
    if is_passphrase:
        word_count = input_data
        pool_size = 7776
        total_combinations = pool_size ** word_count
    else:
        length = len(input_data)
        pool_size = 94
        total_combinations = pool_size ** length

    guesses_per_second = 100_000_000_000
    seconds = total_combinations // guesses_per_second

    if seconds < 1:
        return "Instantaneously"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes"
    elif seconds < 8400:
        return f"{int(seconds // 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds // 86400)} days"
    else:
        years = seconds // 31536000              
        if years > 1_000_000:
            return"Millions of Years"
        return  f"{int(years):,} years"

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
    print(f"Estimated time to crack: {estimate_crack_time(password)}")

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

def make_passphrase(word_count, website, username):
    word_vault = []#empty list waiting to hold words
    with open("words.txt","r") as file:
        for line in file.readlines():
            #it grabs one line at a time
            parts = line.split()
            word_vault.append(parts[1])
    chosen_words = [secrets.choice(word_vault) for _ in range(word_count)]
    result = "-".join(chosen_words)
    print(f"Generated Passphrase: {result}")
    print(f"Estimated time to crack: {estimate_crack_time(word_count, is_passphrase=True)}")

    file_exists = os.path.isfile("google_passwords.csv")
    with open("google_passwords.csv","a") as file:
        if not file_exists:
            file.write("url,username,password\n")
        file.write(f"{website},{username},{result}\n")
        print("DEBUG: Data written to CSV successfully!")
    
while True:
    try:
        choice = input("Choose 1 for random password, 2 for passphrase or 3 to exit: ")
#1.ask user for input and save it as a variable called 'user_input'
        if choice == "1":
            user_input = input ("Enter desired password length (minimum 8): ")
            #Gate 1: Is input a number?
            if user_input.isdigit():
                length = int(user_input)

             #Gate 2: Is it long enough? (Notice this is indented inside Gate 1)
                if length >=8:
            #ask the user for three different pieces of information
                    website = input("Enter the website/app name: ")
                    username = input("Enter the username/email: ")
        #3 Pass all three into the function
                    make_password(length, website, username)
                    break
                else:
                    print ("❌️ Too Weak! Passwords must be 8 or more characters")
            else:
                print ("❌️ Error: Those are not valid numbers. Use digits only")   
    #Converts the text "12" into maths number 12
           
        if choice == "2":
            user_input = input ("Enter the desired word count(4-6 recommended): ")
            if user_input.isdigit():
                word_count = int(user_input)

                if word_count >= 3:
                    website = input("Enter website/app name: ")
                    username = input("Enter username/email: ")
                    make_passphrase(word_count, website, username)

                    import time
                    time.sleep(0.5)
                    break
                else:
                    print("Passphrase must be at least 3 words")
            else:
                print("Please enter a valid number")
        elif choice == "3":
            print("Exitting Password Generator, Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2")
    except ValueError:
        print("An error occured. Please try again")




        