import random
import string
_alfabet = string.ascii_uppercase  + string.digits
def random_alfnum(n: int) -> str:
    return ''.join(random.choice(_alfabet) for _ in range(n))