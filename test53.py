# from test52 import test1
# greeting = test1.greet("Vishal" , "Morning")
# print(greeting)

# creating modules 
# modules are nothing but the folder containing multiple files 
# inside those files we will have utility functions
# and you can import it in your current working file using the keyword import 

import test52
from test52 import test1
from test52.test1 import greet

greeting = test1.greet("Vishal" , "Morning")
