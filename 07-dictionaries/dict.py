Marks={
    "Abhijeet": 98,
    "John": 85,
    "Alice": 92
}

print(Marks["John"])  # Output: 85

print(Marks.get("Alice"))  # Output: 92

print(Marks.get("Alicee"))  # Output: None

print(Marks)

print(Marks.keys())

print(Marks.values())

print(Marks.items())

print(len(Marks))

print("Abhijeet" in Marks)  # Output: True

print("Alicee" in Marks)  # Output: False
