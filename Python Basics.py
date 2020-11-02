#!/usr/bin/env python
# coding: utf-8

# # Interpreted Language

# Immediate mode allows running code one the fly. Variables remain for entire session.

# In[ ]:


2+2


# In[ ]:


a=2+2


# In[ ]:


a


# In[ ]:


b=a**2
b


# In[ ]:


b++


# In[ ]:


b+=1
print(b)


# # Variables

# Python variabes are dynamically typed, which means they are checked at runtime.<br>
# Additionally, the variable type can change throughout the lifetime of the program.<br>
# Variable names must start with an underscode or letter; can contain underscores, letters and numbers; are case sensitive.

# In[ ]:


myVar = 33
print(myVar)
print(type(myVar))
myVar = 1.1
print(myVar)
print(type(myVar))


# In[ ]:


(42).bit_length()


# In[ ]:


fminutes = 415.
print(type(fminutes))
nminutes = 415
print(type(nminutes))


# In[ ]:


fhours=fminutes/60
nhours=nminutes/60
print(fhours, type(fhours))
print(nhours, type(nhours))


# In[ ]:


fhours=fminutes//60
nhours=nminutes//60
print(fhours, type(fhours))
print(nhours, type(nhours))


# In[ ]:


print(fminutes % 60)
print(nminutes % 60)


# In[ ]:


int(fhours)


# In[ ]:


float(nhours)


# In[ ]:


fhours == nhours


# In[ ]:


type(fminutes) == type(nminutes)


# In[ ]:


print(0,bool(0))
print(1, bool(1))
print(-1, bool(-1))
print(0e11, bool(0e11))
print("", bool(""))
print(" ", bool(" "))
print("False", bool("False"))


# # Strings

# Python does not use "character" varaible types, only strings. Strings are declared between single or double quotes. The following are all valid:<br>
# 'Hello World'<br>
# "Hello World"<br>
# """Hello <br>
# World"""<br>
# '''Hello<br>
# World'''<br>
# <br>
# Single quotes can be placed inside double quoted strings, and double quotes inside single quoted strings.<br>
# "This 'String' is valid"<br>
# 'This "String" is also valid'<br>
# <br>
# Triple quotes take raw text input and transform it into a string literal.

# In[ ]:


s1="""Inside this string,
we will find 'single' quotes.\nWhich means the string will be surrounded with
double quotes."""
print(s1)
s1


# In[ ]:


s2="""However, using "double" quotes will cause the string to be surrounded by single quotes."""
print(s2)
s2


# In[ ]:


q="""What will using both 'single' and "double" quotes cause?"""
print(q)
q


# **String objects are also Sequence Types, and support a variety of sequence related functions.**

# In[ ]:


data="Scientific Programming with Python!"


# In[ ]:


print(""""data" length: """, len(data))
print("P in data:", "P" in data)
print("S not in data:", 'S' not in data)
print("Index of P in data: ", data.index('P'))
print("Index of Py in data: ", data.index('Py'))
##print("Index of Java in data: ", data.index('Java')) #error - substring not found


# **String objects are immutable, meaning once created they cannot be modified. Any modification actually creates a new string.**

# In[ ]:


str1 = "It was the worst of times."
print(str1.replace('worst','best'), str1)


# **Indexing and Slicing**

# In[ ]:


print("data[17]:", data[17])
print("data[-1]:", data[-1])

##data[-1] = "?" #error - cannot modify string
##print("data[1000]:", data[1000]) #error - index out of bounds

print("data[17:21]:", data[17:21])
print("data[17:-3]:", data[17:-3])
print("data[17:1000]:", data[17:1000]) 

print("data[0:-1:4]:", data[0:-1:4])


# <font color="blue">Slicing</font> behaves differently than <font color="red">indexing</font>. <font color="red">Indexing</font> returns an element at this specified location of the sequence (in this case, a string). <font color="blue">Slicing</font> is defined as follows: \< Sequence \>[s:e] $\Rightarrow$ return a sequence of all elements whose index is at least *s* and smaller than *e*.<br>
# This can be an empty sequence if no elements match the query, and up to the entire sequence if all elements match the query.
# 

# **Concatenation**

# In[ ]:


moreData = data + "!!"
print(moreData)
evenMoreData = data*5
print(evenMoreData)


# In[ ]:


fl = 44.12
##numberString = "55" + fl #error - can't add float to string implicitly
numberString = "55" + str(fl) # explicit conversion to string
print(numberString)


# **String Formatting**<br>
# Strings use '{}' as placeholders which can be filled with variables and formatted.

# In[ ]:


"{} and {} and {}, Oh my!".format('lions', 'tigers', 'bears')


# In[ ]:


"{1} and {2} and {0}, Oh my!".format('lions', 'tigers', 'bears')


# In[ ]:


"{1} and {1} and {1}, Oh my!".format('lions', 'tigers', 'bears')


# In[ ]:


import string
"{0[7]}{1[4]}{1[11]}{1[11]}{1[14]} {0[22]}{1[14]}{1[17]}{1[11]}{1[3]}.".format(string.ascii_uppercase, string.ascii_lowercase)


# In[ ]:


print("It's always {weather} in {city}.".format(weather="sunny", city="philadelphia"))


# In[ ]:


print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(1337))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(1337))
print("exp: {0:e}, rounded: {0:.3f}".format(12345.6789))


# # Flow Control

# **Blocks** in Python are determined by indentation. A single *tab* indentation is used When starting a new **block**, and all code in that **block** will use the some indentation. A nested **block** will require an additional *tab* indentation and so on...<br>
# Conditional statements in Python are written in **if/elif/else** blocks:<br>
# if \< condition_1 \>:<br>
# &emsp;\< action_1 \><br>
# elif \< condition_2 \>:<br>
# &emsp;\< action_2 \>:<br>
# ...<br>
# elif \< condition_k \>:<br>
# &emsp;\< action_k \>:<br>
# else:<br>
# &emsp;\< fallback_action \>
# <br><br>
# *Note: only the **if** block is manditory, the rest are optional*

# In[ ]:


from random import random
num = random()
print(num)
if num > 0.5:
    if num < 0.75:
        print("good")
    else:
        print("great")
elif num > 0.25:
    print("poor")
else:
    print("awful")


# **Conditional loops using "while"**<br>
# while \< condition \>:<br>
# &emsp;\< loop_action \><br>
# else:<br>
# &emsp;\< condition_false_action \><br>
# <br>
# *Note: the else clause is optional and won't be performed if the loop ended due to a **break** call.*
# 
# 

# In[ ]:


i = 1
prod = 1
while(i < 11):
    prod *= i
    i+=1
else:
    print("{:,}".format(prod))


# In[ ]:


i = 1
prod = 1
while(i < 11):
    prod *= i
    if prod >= 100000:
        break
    i+=1
    
else:
    print("{:,}".format(prod))
print(i)

