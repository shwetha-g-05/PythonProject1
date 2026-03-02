#by value

my_dict ={"a": 3 , "b" : 2,"c":1}
val =dict( sorted(my_dict.items(), reverse=True))
print(val)



#by key
my_dict ={"a": 3 , "b" : 2,"c":1}
val =dict( sorted(my_dict.items()))
print(val)