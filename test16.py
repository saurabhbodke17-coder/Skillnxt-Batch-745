data = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

res = data["brand"]
print(res)

# res = data["colour"]
# print(res) # KeyError: 'colour'

# if key is not present in the dictionary it shoud return me the default value 

# res = data.get("colour")
# print(res) # None


# if the key is not present inside the dict then this get will return
# the default value 
res = data.get("colour" , "Red")
print(res) # Red

