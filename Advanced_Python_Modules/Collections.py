from collections import Counter
# -------------------------------------- COUNTER ----------------------------------------------------

my_list = [2,2,2,2,2,6,6,6,6,6,7,7,7,7,7,8,8,8,8]
print(Counter(my_list))  # ------- Counter({2: 5, 6: 5, 7: 5, 8: 4})

my_list2 = ['a','a','a','b','b','b','c','c','c']
print(Counter(my_list2))  # -------- Counter({'a': 3, 'b': 3, 'c': 3})

my_list3 = 'awdwadwdqfqwdq'
print(Counter(my_list3.lower()))  # -------- Counter({'w': 4, 'd': 4, 'q': 3, 'a': 2, 'f': 1})

Str = "How old am I ?"
print(Counter(Str.split())) # ------ Counter({'How': 1, 'old': 1, 'am': 1, 'I': 1, '?': 1})

letters = 'kkkkkkkkkkksssssssssssssssnnnnnnnnnnnn'
C = Counter(letters)
print(C)    # ---------------------- Counter({'s': 15, 'n': 12, 'k': 11})
print(C.most_common(2))  # ----------  [('s', 15), ('n', 12)]
print(list(C)) # ------------------- ['k', 's', 'n'] all unique elements

# -------------------------------------------- DEFAULTDICT -------------------------------------------------

from collections import defaultdict
d = {'Ulan':19}
print(d['Ulan'])
d = defaultdict(lambda:0)
print(d['Umida']) # Default value is 0 for new keys in dict

# ------------------------------------------ NAMEDTUPLE ------------------------------------------------

from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
bobik = Dog(age=9,breed='Huskie',name='bob')
print(type(bobik))
print(bobik.age) # The same as bobik[0]
print(bobik.breed) # The same as bobik[1]
print(bobik.name)  # The same as bobik[2]

