import random
import string

def make_password(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(pool) for i in range(length))
    (print("🔒 New Password:", result))

(make_password(16))

        