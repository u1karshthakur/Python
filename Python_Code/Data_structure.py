list = [1,2,3,4]#list creation 

print ( list)
tuple = tuple ( list) #conversion of list into tuple
print ( tuple )

#creating dictionary
dict = {"name":"Utkarsh Thakur" , 1 : [123456]}
print (dict)
print ( dict["name"])

dict1 = {x : x*2 for x in [1,2,3,4,5,6,7]}
print(dict1[7])