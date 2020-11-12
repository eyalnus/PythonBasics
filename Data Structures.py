#!/usr/bin/env python
# coding: utf-8

# # Lists

# **Lists** are one of the basic data structures in Python. Python does not have an "Array" type as other languages, so **lists** are usually used for this purpose. **Lists** are considered a Sequence Type and support sequence related functions such as *len()*, indexing and slicing, and support iteration. A **list** object can either be created using the *list()* constructor or using square brackets enclosing the list content: **[element1, element2, ..., elementn]**. **Lists** are ordered collections and are mutable, meaning their content can be modified.

# In[ ]:


l1 = list()
l2 = []
l3 = [1,2,3]
print("l1:", l1)
print("l2:", l2)
print("l3:", l3)


# **Lists can be nested, meaning can contain lists. There can be any number of nesting levels, and the lists can be of any size.**

# In[ ]:


nestedList = [l1,l2,l3]
print(nestedList)


# In[ ]:


nestedNestedList = [nestedList, l1, [l2,l3]]
print(nestedNestedList)


# **Elements of a list do not need to be of the same type.**

# In[ ]:


mixedList = ["John", "Doe", "m", 34, 1.82, ["Alice", "Bob"]]
print(mixedList)


# **Indexing and slicing are performed in the same manner as previously shown for strings. Accessing an element by index returns a single element, slicing returns a list.**

# In[ ]:


print(mixedList[0])
print(mixedList[3:5])
print(mixedList[3:4])
print(mixedList[3])


# In[ ]:


print(mixedList[-2:-1])
print(mixedList[3:])


# In[ ]:


print(mixedList[-1][0])


# In[ ]:


print(mixedList[-1:])
print(mixedList[-1:][0])


# **As opposed to strings, lists are mutable and therefore an element at a given index can be changed**

# In[ ]:


mutable = ["one", 2, 3.0]
print(mutable)
mutable[0] = "ONE"
print(mutable)


# In[ ]:


mutable2 = mutable
print("mutable2:",mutable2)
mutable2[1] = "two"
print("mutable:",mutable)
print("mutable2:",mutable2)


# *Note: lists are created once and then passed by reference. Modifying a list does not create a new instance in memory, and changes it for all references.

# **Other sequence type functionalities**

# In[ ]:


print("mixedList length:",len(mixedList))
print("34 in mixedList:", 34 in mixedList)
print("'m' not in mixedList:", "m" not in mixedList)
print("index of 'Doe' in mixedList:", mixedList.index("Doe"))


# In[ ]:


print('"Alice" in mixedList:', 'Alice' in mixedList)


# In[ ]:


print('["Alice","Bob"] in mixedList:', ["Alice","Bob"] in mixedList)
print('["Bob","Alice"] in mixedList:', ["Bob","Alice"] in mixedList) 


# **The list constructor can take other Sequence types as input and convert them element by element into a list**

# In[ ]:


stringList = list("Python")
print(stringList)


# In[ ]:


stringList2 = list(stringList)
print(stringList2)
stringList2[0]="0"
print(stringList)
print(stringList2)


# **Lists can also be created from strings using the *split(sep)* function of a string object. The *sep* parmater is an optional separator string around which the string will be split into elements.**

# In[ ]:


ipList = "192.168.1.1".split(".")
print(ipList)
split = "192.168.1.1".split(".1")
print(split)


# In[ ]:


data="Scientific Programming with Python!"
dataSplit = data.split()
print(dataSplit)


# In[ ]:


print("\n".join(dataSplit)) #join list elements into a string using a connector string


# ## List manipulation

# Once a list is created, its elements can be modified. <br>
# **Adding Elements**
# 
# * `append(x)` - adds the element `x` at the end of the list
# * `insert(i, x)` insert the element `x` at the i-th place
# * `extend(iter)` - concatenate the elements of `iter` to the list
# 

# In[ ]:


list1 = ["Alice", "Bob"]
print(list1)


# In[ ]:


list1.append("Dave")
print(list1)


# In[ ]:


list1.insert(2,"Charlie")
print(list1)


# In[ ]:


list1.extend(["Eve","Faith"])
print(list1)


# In[ ]:


list1.append(["Grace","Heidi"])
print(list1)


# In[ ]:


list1.extend("Ivan")
print(list1)


# In[ ]:


judy = ["Judy"]
concat = list1 + judy
print("concat:",concat)


# In[ ]:


print("list1:",list1)
##print("list1 + judy[0]:",list1 + judy[0]) #error - cannot implicitly concatenate string to list


# 
# **Removing Elements**
# * `pop(i)` - Remove the item at index `i` (and return it). If `i`is not defined, pops last element.
# * `remove(x)` - Remove item `x` (first instance found)
# 

# In[ ]:


list2 = [1,3,5,7,9]
print(list2)


# In[ ]:


list2 = list2 * 4
print(list2)


# In[ ]:


elem = list2.pop()
elem3 = list2.pop(3)
print("Element at end of list:", elem)
print("Element at index 3:",elem3)
print("New element at index 3:", list2[3])


# In[ ]:


print(list2)
list2.remove(7)
print(list2)


# **Another useful function for lists is the *count()* function which returns the number of appearances of an element in the list**

# In[ ]:


list2.count(9)


# **The *count()* function can be used on strings as well**

# In[ ]:


"The quick brown fox jumped over the lazy gray dog".count(" ")


# ## Sorting

# **List**s can be sorted using the built-in *sort()* function. By default, sorting is done in ascending order. Only **list**s containing comparable elements can be sorted. Sorting is done in place - altering the existing list.

# In[ ]:


numericalList = [1,65,12.44,78,123.09,2.2,7.11,234,534,3.2,9,12]
numericalList.sort()
print(numericalList)


# In[ ]:


charList = list("asdkfjeisdklfjdXYZkshfjksdhfeuvzpxcvjeiouczpoifj")
print("unsorted:",charList)
charList.sort()
print("sorted:",charList)


# In[ ]:


mixList = [17,"5"]
##mixList.sort() #error - cannot compare string and int


# **The sort function has optional parameters - *sort(reverse,key)*. Reverse is False by default, and setting it to True will cause the sorting to be in descending order. The *key* parameter accepts a function to be called on the elements by which the comparison will be made, instead of the default comparator function for each type**

# In[ ]:


codes = ["delta", "alpha", "foxtrot","beta","charlie"]
codes.sort(reverse=True)
print(codes)


# In[ ]:


codes.sort(key=len)
print(codes)


# *Note: this is a special case where the parameters sent to the function are **named**, and not just sent in order of the function signature. In fact, we cannot send parameters to the sort() function without naming them. We will learn more about this in the future.*

# In[ ]:


##codes.sort(True,len) #error - cannot send parameters to sort function without keywords


# # Tuples

# **Tuples** are an immutable version of **lists**. **Tuples** are considered a Sequence Type and support sequence related functions such as *len()*, indexing and slicing, and support iteration. A **tuple** object can either be created using the *tuple()* constructor or using round brackets enclosing the list content: **(element1, element2, ..., elementn)**. **Tuples** are ordered collections and are immutable, meaning their content <font color=red>*cannot*</font> be modified.

# In[ ]:


t1 = tuple()
t2 = ()
t3 = (1,2,3)
print("t1:", t1)
print("t2:", t2)
print("t3:", t3)


# In[ ]:


mixedTuple = (17, 13.37, 'tuple', 543265e-3,
          True, ('\n',0,False), [t1,t2,t3], None)
print(mixedTuple)
print("mixedTuple length:",len(mixedTuple))
print("True in mixedTuple :",True in mixedTuple)
print("False not in mixedTuple:",False not in mixedTuple)
print("Index of 'tuple' in mixedTuple:",mixedTuple.index('tuple'))


# In[ ]:


print(mixedTuple[0])
##mixedTuple[0] = 18 #error - cannot modify element of tuple


# In[ ]:


stringTuple = tuple("This also works")
print(stringTuple)


# In[ ]:


tupleList = list(stringTuple)
print(type(tupleList),tupleList)


# In[ ]:


listTuple = tuple(tupleList)
print(type(listTuple),listTuple)


# In[ ]:


print("".join(listTuple))


# **Tuples can be implicitly created and unpacked.**

# In[ ]:


courseDetails = 'Scientific Programming in Python', 3, 3, ["3502826","3502811"]
print(courseDetails)
print(type(courseDetails))


# In[ ]:


name, credits, hours, prerequisites = courseDetails
print("name:",name)
print("credits:",credits)
print("hours:",hours)
print("prerequisites:",prerequisites)


# In[ ]:


##name, credits = courseDetails #error - cannot implicitly unpack partial tuple


# **This can also be done for other sequences.**

# In[ ]:


a,b,c = [1,2,3]
d,e,f = "def"
print(a,b,c,d,e,f)


# # Sequence Iteration

# We can iterate over a sequence type object, such as a **list**, **string** or **tuple** using the <font color="blue">**for**</font> statement. Python treats <font color="blue">**for**</font> loops differently than most languages you are probably familiar with, as it does not conform to the (initialize; condition; increment) format. In Python, the <font color="blue">**for**</font> statement is declared as follows:<br>
# for \< iterator \> in \< iterable \>:<br>
# &emsp;\< perform_action \><br>
# else:<br>
# &emsp;\< perform_end_iteration_action \><br>
# <br>
# *Note: the else clause is optional. It is called when the iteration is complete, and won't be performed if the loop ended due to a **break** call.*
# 
# 

# In[ ]:


fruits = ["apples", "oranges", "bananas", "lemons"]
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits.")


# In[ ]:


num = 0
for char in "171337984230423":
    num += int(char)
print(num)    


# **Sometimes we wish to know the index of elements while we iterate. For this we use the *enumerate()* function**

# In[ ]:


num = 0
for i,char in enumerate("171337984230423"):
    print(i,char)
    num += int(char) if i%3 == 0 else 0
print("sum of i mod 3 == 0:",num)    


# In[ ]:


mix = []
for fruit in fruits:
    for char in fruit:
        mix.append(char if fruit.index(char)%2 == 0 else char.upper())
mix = "".join(mix)
print(mix)


# **What if we still wish to loop through a set of code a specified number of times, and not just loop through a sequence? We can use the *range()* function.**

# In[ ]:


for i in range(5): #loops through values 0 to 4
    print(i)


# In[ ]:


for i in range(2,5): #start at i=2
    print(i)


# In[ ]:


for i in range(0,10,2): #start at i=0, increment by 2, stop at step before 10
    print(i)


# In[ ]:


veggies = ["cucumber","lettuce","celery","eggplant","pepper","squash"]
for i in range(len(veggies)):
    if i > 4:
        break
    print(veggies[i])
else:
    print("No more veggies.")


# In[ ]:


for i in range(len(veggies)):
    veggies[i] = veggies[i].upper()
    print(veggies[i])


# ## List Comprehension

# The Python <font color="blue">for</font> statement has a secondary syntax used for **list** comprehension - creating lists from sequences and other iterables. Following are a few examples.

# In[ ]:


numbers = [12,14,99,100,32,6,11,5,16,89]
squares = []
for num in numbers:
    squares.append(num**2)
print(squares)


# In[ ]:


squaresComp = [num**2 for num in numbers]
print(squaresComp)


# In[ ]:


evenSquares = []
for num in numbers:
    if num % 2 == 0:
        evenSquares.append(num**2)
    else:
        evenSquares.append(num)
print(evenSquares)


# In[ ]:


evenSquaresComp = [(num**2 if num % 2 == 0 else num) for num in numbers]
print(evenSquaresComp)


# In[ ]:


string1 = "aAbReSDGTesrfewWEf34sd fsdf wefSDFGr w234rWE SWDFw234 fasdf F"
caps = [s for s in string1 if s.isupper()]
print(caps)


# # Sets

# A **set** is a collection with no order and no repititions. Each element can exist in a set at most once. A **set** is created using the *set()* constructor which can receive no input or a sequence as its input parameter. 

# In[ ]:


set1 = set()
print("empty set:",set1)
set2 = set((1,2,3,"asd"))
print("set from tuple:",set2)


# *Note: An empty set is printed as "set()" and a non-empty set is printed in curled brackets. We will explain shortly.*

# In[ ]:


set3 = set([100, 300, 300, 700])
print("set from list:", set3)


# *Why did the order change between the list and the set?*

# In[ ]:


set4 = set("hello world")
print("set from string:", set4)


# **Sequence Type functionality and iterating over a set**

# In[ ]:


print("set4 length:",len(set4))
print("l in set4:", 'l' in set4)
print("' ' not in set4:", " " not in set4)
##print("index of 'd' in set4:", set4.index("d")) #error - no index defined for sets
##print("set4[0]:", set4[0]) #error - no index defined for sets


# In[ ]:


print([s for s in set4])


# ### **Set** manipulation

# The `add(item)` function adds an *item* to a *set* if it does not already exist. The `update(iter)` function merges an *iterable* object into the *set*, excluding cuplicate items.

# In[ ]:


set5 = set("There is no cow level")
print(set5)
set5.add("diablo")
print(set5)


# In[ ]:


set5.add("diablo")
print(set5)


# In[ ]:


set5.update(range(10))
print(set5)


# **The `union(iter)` function acts like the `update(iter)` function, but returns a new set instead of modifying the existing one.**

# In[ ]:


set6 = set5.union(range(100,200,10))
print("original set:", set5)
print("union set:",set6)


# In[ ]:


##set7 = set6.add([1,2,3,4,5]) # - error, cannot add list to set


# *Why can't you add a list to a set?*

# In[ ]:


set8 = set([1,3,5,7,9])
set9 = set8
print("set8",set8)
print("set9",set9)


# In[ ]:


set8.discard(9)
print("set8",set8)


# In[ ]:


print("set8.pop()",set8.pop())
print("set9",set9)


# In[ ]:


set9.clear()
print("set9",set9)
print("set8",set8)


# In[ ]:


set8.discard(7)
print("set8",set8)
##print("set8.pop()",set8.pop()) #error - cannot pop() from an empty set.
##set8.remove(7) # error - the key 7 is not foudn in the set


# *Note: `remove` raises an error if item to remove is not found, `discard` does not. The `pop()` function removes and returns the "first" element in the set, as defined by its internal hashing order, and will also return an error if the set is empty.

# **The `intersection(iter)` function returns a new set with the intersection of the original set and the given iteratable**

# In[ ]:


print(set5.intersection(range(3)))
print(set5.intersection(set6))
print(set5.intersection(["hello"]))


# # Dictionaries

# **Dictionaries** (**dict** for short) are containers which contain `key:value` pairs of objects. A `key` is a hashable object and must be unique to each **dict**. The `key` maps to an object, which is defined as its `value` in the **dict**. <br>
# **Dictionaries** are defined using curled brackets containind comma-separated elements (e.g {element1, element2, ..., elementN}, each element being a colon-separated `key:value` pairs (e.g "color":"blue"). <br>
# For example: {"brand":"Ford", "model":"Focus","color":"blue"}.<br>
# Alternatively, we can use the `dict()` constructor function which accepts named parameters as input:<br>
# `dict(brand="Ford", model="Focus",color="blue")`

# In[ ]:


ascii_codes = {"a":97, "b":98,"c":99,"d":100,"A":65, "B":66,"C":67,"D":68}
print(ascii_codes)
more_ascii_codes = dict(e=101,f=102,E=69,F=71)
print(more_ascii_codes)


# *Note: the displayed container (curled brackets) of a **dict** is the same as that of a **set**. This is why empty **set**s are displayed as `set()` and not `{}`. Empty curled brackets in Python are by definition a **dict** and not a **set**. However, we can create a **set** using curled brackets.

# In[ ]:


confusing_set = {"a",97, "b",98,"c",99,"d",100,"A",65, "B",66,"C",67,"D",68}
print(confusing_set)


# **We can use integers and floats as *dict* keys.**

# In[ ]:


reverse_ascii = {97:"a", 98:"b",99:"c",100:"d",65:"A", 66:"B",67:"C",68:"D"}
print(reverse_ascii)
stations = {91.8:"galgalatz", 96.6:"galatz", 89.7:"reshet gimmel", 95.0:"reshset bet"}
print(stations)


# In[ ]:


food = {'Fruits': ['Apple', 'Banana', 'Orange'],
         'Vegetables': ['Lettuce', 'Cucumber', 'Eggplant'],
         'Other': ['Meat', 'Bread', 'Rice']}
print(food)


# ### Using non-unique keys

# In[ ]:


numbers = {10:"ten", 100:"one hundred",1500:"one thousand five hundred", 2000:"two thousand", 1500:"fifteen hundred"}
print(numbers)


# ## Using non-hashable keys

# In[ ]:


reverse_food = {['Apple', 'Banana', 'Orange']:'Fruits',
         ['Lettuce', 'Cucumber', 'Eggplant']:'Vegetables' ,
         ['Meat', 'Bread', 'Rice']:'Other' }


# ## Getting and Setting Values

# We access **dict** values similarly to accessing **string** and **list** elements, using the `[]` operator. However, instead of indices, we access using `keys`. 

# In[ ]:


print("B ascii:",ascii_codes["B"])
print("ascii 67:",reverse_ascii[67])


# In[ ]:


print("The third fruit:",food["Fruits"][2])


# In[ ]:


##print("B ascii:",ascii_codes["G"]) # error - no key "G" in ascii_codes
##print("The first cake:",food["Cakes"][0]) # error - no key "Cakes" in food


# *Note: attempting to return a value for a non-existent key raises an error*

# In[ ]:


print("station 91.8:",stations.get(91.8))
print("station 100.1:",stations.get(100.1))


# **Using the dictionary's `get(key)` will not raise an error for a non-existent key.**

# **Dictionaries are mutable, you can modify the value of a key**

# In[ ]:


print("more ascii codes:" ,more_ascii_codes)
more_ascii_codes["F"] = 70
print("fixed more ascii codes:" ,more_ascii_codes)


# In[ ]:





# In[ ]:


stations_copy = dict(stations)
stations_copy[104.8] = 'reshet aleph'
print("copy:",stations_copy)


# In[ ]:


print("original:",stations)


# In[ ]:


food_copy = dict(food)
food_copy["Other"][0] = "Pasta"
print("copy:",food_copy["Other"])
print("original:",food["Other"])


# In[ ]:


print(stations_copy.pop(91.8))
print(stations_copy)


# **The `pop(key)` function removes the item corresponding to `key` from the dictionary and returns its value**

# In[ ]:


##print(stations_copy.pop(91.8)) # error - no key 91.8 in dict


# In[ ]:


print(stations_copy.popitem()) # removes and returns last item insterted
print(stations_copy)


# ## Iterating over Dictionaries

# In[ ]:


print([item for item in ascii_codes])


# *Note: iterating over a **dict** iterates over its keys*

# In[ ]:


print (type(reverse_ascii.keys()))
print (type(reverse_ascii.values()))
print (type(reverse_ascii.items()))


# **Each one of the above is an iterable class derived from the dict container.**<br>
# 

# In[ ]:


print (reverse_ascii.keys())
print (reverse_ascii.values())
print (reverse_ascii.items())


# In[ ]:


for k in reverse_ascii.keys():
    print(ascii_codes[reverse_ascii[k]])


# In[ ]:


for k,v in reverse_ascii.items():
    print("ascii code:", k, ", ascii character:",v)

