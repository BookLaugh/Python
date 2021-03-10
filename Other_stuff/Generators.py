# Key function 'yield' takes less memory and efficient to use
def fib_gen(n):
    x = 1
    y = 1

    for i in range(n):
        yield x
        x,y = y,x+y
print(list(fib_gen(10)))
for num in fib_gen(10):
    print(num)

# Simple generator with key function -- next() --

def simple_gen():
    for i in range(4):
        yield i

# for number in simple_gen():
#     print(number)

# assigning to the variable

gen = simple_gen()
print(next(gen))   # --- 0
print(next(gen))   # --- 1
print(next(gen))   # --- 2
print(next(gen))   # --- 3
# print(next(gen))   # --- This will give an StopIterationError


# Next key function that might be useful is --- iter() ---

name = 'Ulan'
for letter in name:
    print(letter)
# print(next(name))  --- It's an error

# To iterate through string we have to do the following

make_iter = iter(name)
print(next(make_iter))
print(next(make_iter))
print(next(make_iter))
print(next(make_iter))
