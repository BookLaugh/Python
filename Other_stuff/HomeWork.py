# ------------- PROBLEM 1 ---------------------

def gen_squares(N=10):
    for i in range(N):
        yield i**2
for num in gen_squares():
    print(num)
   
# ------------- PROBLEM 2 ----------------------

import random

def rand_int(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for num in rand_int(1,10,5):   # Will take random N numbers between low and high numbers
    print(num)
 
# --------------- PROBLEM 3 ------------------------
name = 'Aktan'
make_iter = iter(name)
print(next(make_iter)) # A
print(next(make_iter)) # k
print(next(make_iter)) # t
print(next(make_iter)) # a
print(next(make_iter)) # n

# --------------- PROBLEM 4 -------------------------
str = []
def gen_cube(n):
  for i in range(n):
    str.append(i*3)
   print(str)
gen_cube(5) 

# INSTEAD USE --- yield()                         [0,1,8,27,64] Two methods has the same answers but second is more efficient and useful 
def gen_cube(n):
  for i in range(n):
    yield i*3
print(list(gen_cube(5)))
  
# --------------- EXTRA CREDIT ! ---------------------
my_list = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43]

gen_comp = (item for item in my_list if item > 23) # If item in my_list is above 23 then u take item to the generator called --- gen_comp--- otherwise just continue

for item in gen_comp:
  print(item)
    
