import random
import string

length = int(input('Enter the length of password:'))
char = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(char) for _ in range(length))
print(password)

