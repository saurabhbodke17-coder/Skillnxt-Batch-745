# # next datatype
# # Dictionary
# d = dict()
# print(d , type(d))

# # this is the mapping datatype
# # in this datatype we map key and values
# # declared by using the {}
# # key:value pair 

# d = {"name":"saurabh" , "job":"ai engineer"}
# print(d) # {'name': 'saurabh', 'job': 'ai engineer'}
# print(type(d)) # <class 'dict'>

# # all the payloads in software engineering which frontend 
# # send to backend and backend send to frontend all are in dict format 
# # same thing javascript is called as object

# # list of tuples --> dict

# l = [("name" , "saurabh") , ("job" , "ai engineer")]
# d = dict(l)
# print(d) # {'name': 'saurabh', 'job': 'ai engineer'}

# l = [["name" , "saurabh"] , ["job" , "ai engineer"]]
# d = dict(l)
# print(d) # {'name': 'saurabh', 'job': 'ai engineer'}

# l = (("name" , "saurabh") , ("job" , "ai engineer"))
# d = dict(l)
# print(d) # {'name': 'saurabh', 'job': 'ai engineer'}

# l = (("name" , "saurabh" , 10) , ("job" , "ai engineer" , 20))
# d = dict(l)
# print(d) # ValueError: dictionary update sequence element #0 has length 3; 2 is required

# how to extract the data from dictionary
# this is also unorderd collection of elements 
# in this you cant use indexing or slicing 
# you need to acces the value by key name 

data = {"name":"saurabh" , "job":"ai engineer"}
res = data["name"]
print(res) # saurabh

res = data["job"]
print(res) # ai engineer


data = {"name":"saurabh" , "job":"ai engineer" , "job":"data scientist"}
print(data["job"]) 
# data scientist -> because last declared key will be 
# considerd as a final one 

# a key which in not there but i want to extract 
# how can i extract it 
# res = data["age"]
# print(res) # KeyError: 'age'

# you want to extract the value and if its not there you can return a default value
# for this we have the method
# get

res = data.get("age")
print(res) # None

res = data.get("age" , "age is not present inside the data")
print(res) # age is not present inside the data

# how to add and update data in dictionary 
data = {"name":"saurabh" , "job":"ai engineer" , "prev_job":"data scientist"}
data["job"] = "Deep learning engineer"
print(data)
# {'name': 'saurabh', 'job': 'Deep learning engineer', 'prev_job': 'data scientist'}
# so you can see above the data is updated
# 
# if i want to add totally new key and value 

data["gender"] = "male"
print(data) 
# {'name': 'saurabh', 'job': 'Deep learning engineer', 'prev_job': 'data scientist', 'gender': 'male'}
# we can have the same value but not same key
# yo add new e;ement you can simply do below step 

collection = {}
collection["key"] = "value"
print(collection) # {'key': 'value'}

# imp part was we can use dict to dcreate the dataframe 
# also this is very usefull in doing any kind of project 
# by using dict you can add any value in dataset 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") 
print(car) # {'brand': 'Ford', 'year': 1964}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White" , "wheels":4})
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White', 'wheels': 4}
print(car)

# dict unbinding
data = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

data1 = data.items()
print(data1)
print(type(data1))
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# <class 'dict_items'>

data2 = list(data1)
print(data2 , type(data2))
# [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)] <class 'list'>