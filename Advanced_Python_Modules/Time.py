import time
import timeit
import math

def func_one(num):
    lst = []
    for i in range(num):
        lst.append(str(math.sqrt(i)))
    return lst
def func_two(num):
    lst = list(map(int,range(num)))
    lst1 = []
    for n in lst:
        lst1.append(str(n*n))
    return lst1

# First version
start_time = time.time()
result = func_one(1000000) # 1 million
end_time1 = time.time() - start_time
print(f'Time Complexity of Func_one is: {end_time1}')

start_time - time.time()
result = func_two(1000000) # the same 1 million
end_time2 = time.time() - start_time
print(f'Time Complexity of Func_two is: {end_time2}')

if end_time1 < end_time2:
    print("The Func_one is Faster !")
else:
    print("The Func_two is Faster !")


# Second version

def func_three(lst):
    new_lst = []
    for i in lst:
        new_lst.append(str(i*i*i))
    return new_lst

def func_four(lst):
    new_lst = [i*i*i for i in lst]
    return new_lst


# Testing
my_list = [1,10,100,1000,1000,10000,100000,1000000]
start_time = time.time()
result = func_three(my_list)
end_time3 = time.time() - start_time
print(f"Time Complexity of Func_three is: {end_time3}")

start_time = time.time()
result = func_four(my_list)
end_time4 = time.time() - start_time
print(f"Time Complexity of Func_four is: {end_time4}")

if end_time3 < end_time4:
    print("The Func_three is Faster !")
else:
    print("The Func_four is Faster !")
