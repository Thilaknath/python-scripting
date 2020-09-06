import random
import datetime

print (random.randint(1,10))
print (datetime.datetime.now().year)

now = datetime.datetime.now()
print (now + datetime.timedelta(days=10))