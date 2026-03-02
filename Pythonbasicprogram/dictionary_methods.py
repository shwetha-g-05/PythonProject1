from xml.sax.xmlreader import Locator

my_dict = {"name" : "Charvi" ,
            "Age" : 25,
            "Job role": "Engineer",
           "location" :{ "home address": "BA",
                       "Office location": "KA"}}


print(my_dict.items())

print(my_dict.keys())
print(my_dict.values())

print(my_dict["Age"])
print(my_dict["location"]["home address"])
print(my_dict.get("Job role"))
my_dict["Age"]=30
print(my_dict)


