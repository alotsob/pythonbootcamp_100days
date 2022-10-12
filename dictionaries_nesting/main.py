
# fruits_dict = {"1": "Apple", "2": "Banana", 3: "Orange", None: "NA"}
#     print(fruits_dict)

# fruits_dict = {"1": "Apple", "2": "Banana"}
 
# print(f'Original Dictionary = {fruits_dict}')
 
# # insert
# fruits_dict["3"] = "Orange"
 
# # update
# fruits_dict["1"] = "Kiwi"
 
print(f'Updated Dictionary = {fruits_dict}')

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

var = people.get(4)
print(f"Mr peter's age is {var.get('age')}),\nhis sex is {var.get('sex')}")