student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}
print(student)
item = {
    "brand": "Nike",
    "price": 1500,
    "quantity": 2
}
print(item)
#Using curly braces
student_info = {
    "name": "Bob",
    "age": 21,
    "courses": "Computer Science"
}
#Using dict function
student_info2 = dict(name="Emma", age=22, major="Biology")
print(student_info)
print(student_info2)
#Accessing Dictionary Elements
student = {
    "name": "Charlie",
    "age": 19,
    "major": "Physics"
}
print(student["name"])
print(student.get("GPA", "Not Avaialable"))
#Modifying a Dictionary
student = {
    "name": "Dave",
    "age": 20,
    "major": "Chemistry"
}
student["GPA"] = 3.8
student["age"] = 21
student.pop("major")
print(student)
student = {
    "name": "Eve",
    "age": 22,
    "major": "Biology"
}