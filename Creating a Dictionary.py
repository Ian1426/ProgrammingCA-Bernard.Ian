#Creating a Dictionary
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}
print("Name:", student["Name"])
print("Major:", student["Major"])
#Adding GPA and Age
student["GPA"] = 3.8
student["Age"] = 25
print(student)
#Loop Through a Dictionary
for key, value in student.items():
    print(f"{key}: {value}")
#Checking if a Key Exists
def check_key(dictionary, key):
    if key in dictionary:
        return "Key exists"
    else:
        return "Key does not exist"
print(check_key(student, "Name"))
print(check_key(student, "Hobbies"))
#Count Occurences
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
#Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
#Remove Keys
student.pop("Age", None)
print(student)
#Nested Dictionaries
classroom = {
    "Student1": {"Name": "John", "Age": 20}, 
    "Student2": {"Name": "Emma", "Age": 22}
}
print("Student2 Name:", classroom["Student2"]["Name"])
print("Student2 Age:", classroom["Student1"]["Age"])
#Sorting a dictionary
data = {"2": 10, "b": 5, "a": 15}
sorted_by_keys = dict(sorted(data.items()))
print("Sorted by keys:", sorted_by_keys)
sorted_by_values = dict(sorted(data.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)
         