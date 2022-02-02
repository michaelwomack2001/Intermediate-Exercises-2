import time
def fib(num):
    if num <= 1:
        return num
    else:
        return(fib(num-1) + fib(num-2)) #did this last semester in java but so that is where I got the format from just switched to python

start_time = time.time()
fib_num = fib(35)
total_time = time.time() - start_time

print(fib_num)
print(f'fib(35) executed in {total_time} seconds') 
#used the link provided and https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution to learn time function, didn't copy anything