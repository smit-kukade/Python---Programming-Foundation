# d = {} -> Empty dictionary

marks = {
    "Smit": 84,
    "Sneha": 99,
    "Janhavi": 94
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Smit": 87})
print(marks)

print(marks.get("Janhavi G")) # Prints None
print(marks["Janhavi G"]) # Returns an error


