
import os

# Specify the directory path
path = "/"

# Get the contents of the directory
contents = os.listdir(path)

# Print each file and folder
print("Contents of the directory:")

for item in contents:
    print(item)
