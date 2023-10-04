#! /usr/bin/python3
'''
#SET IN PYTHON
k = {y for y in "school" if y in " choo"} 
print (k)
print("\n #######################################################")
print ("\n")
#A DICTIONARY IN PYTHON
y = {"name":"John", "Age":31, "State of Origin": "Anambra"}
print (y)

y ["name"]  = "Peter"

y["Address"] = "No 1 Henry Adigwe Close Somolu"

print(y)


v = dict(name="Vin", age = 35, Country= "Nigeria")

print(v)
# To Print the command you type at the terminal
import sys


o =sys.argv

p= int(o[1])+int(o[2])
print (p)

print("\n\n")


print(len(o))

'''
#DECISION MAKING OR EQUALITY TEST

import sys

var = sys.argv

if var[1] == "raining":
    print ("Stay at home")
if  var[1] == "sunny":
    print("You can go out")
