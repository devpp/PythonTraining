import secrets
import random
import string

secretcodes = secrets.SystemRandom()

for i in range(1, 10):
    otp = secretcodes.randrange(1000, 9999)
    print(otp)


def myRanStr(strlen):
    charact = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(charact) for a in range(strlen))


print("Random string is :-", myRanStr(8))
