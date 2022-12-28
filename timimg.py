def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))


def func_two(n):
    return list(map(str,range(10)))

print(func_two(10))

import time
#Current time
start_time=time.time()
#Run Code
result=func_one(1000000)
#End Time
end_time=time.time()
#Elapsed Time
elapsed_time=end_time-start_time
print(elapsed_time)

#Current time
start_time=time.time()
#Run Code
result=func_two(1000000)
#End Time
end_time=time.time()
#Elapsed Time
elapsed_time=end_time-start_time
print(elapsed_time)







