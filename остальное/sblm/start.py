import random
import string
letters = string.ascii_lowercase
prsaw = ''.join(random.choice(letters) for i in range(14))
print(prsaw)