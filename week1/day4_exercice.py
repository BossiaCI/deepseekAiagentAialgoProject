person = {"name": "Alice", "age": 24, "grade": "A"}

# Add new key-value pair
person["address"] = "123 Main St"

# update Age
person["age"] = 32

# Remove grade
if "grade" in person:
    del person["grade"]

print(person)

