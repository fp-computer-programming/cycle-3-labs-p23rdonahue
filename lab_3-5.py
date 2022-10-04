#author:RED 10/4/22

import math 
import time
print(math.pow(2,2))
x= time.process_time ()
print(x)
print(2**2)
z= time.process_time ()
print(z)
#takes little longer for z to process

print(math.pow(2,2))
x= time.perf_counter ()
print(x)
print(2**2)
z= time.perf_counter ()
print(z)

#