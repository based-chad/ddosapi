## API KEY GEN 
c = "UHJvZ3JhbW1lZCBieSBiYXNlZC1jaGFkLiBodHRwczovL2dpdGh1Yi5jb20vYmFzZWQtY2hhZCwgSUcgQFNraWRzLkNyeWluZw=="

import time
import random

Alphabets = "qwertyuiopasdfghjklzxcvbnm"

Upper_Alphabets = Alphabets.upper()

nums = "1234567890"

all = Alphabets+Upper_Alphabets+nums

api_key = random.sample(all,24)
password = "".join(api_key)

print(password)
