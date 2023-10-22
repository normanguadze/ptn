import random
import string

def generate_unique_string(length=16):
    characters = string.ascii_letters + string.digits  # Uppercase letters, lowercase letters, and numbers
    return ''.join(random.sample(characters, length))

# Generate and print 50 unique strings
for _ in range(50):
    unique_string = generate_unique_string()
    print(unique_string)
