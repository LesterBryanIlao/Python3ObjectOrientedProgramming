from dataclasses import dataclass, make_dataclass
from myobject import MyObject
from  casestudy import Character

myObj = MyObject()
myObj.PASSWORD = "123456"
print(myObj.PASSWORD)

# create a sample named tuple
from collections import namedtuple

MyNamedTuple = namedtuple("MyNamedTuple", ["name", "age"])
my_named_tuple = MyNamedTuple("John", 25)
print(type(my_named_tuple)) 
print(my_named_tuple) 

MyDataClass = make_dataclass("MyDataClass", ["name", "age"])
my_dataclass = MyDataClass("John", 25)
print(type(my_dataclass)) 
print(my_dataclass) 

types = {"MyNamedTuple": MyNamedTuple, "MyDataClass": MyDataClass}