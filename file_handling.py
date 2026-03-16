import os
import shutil

#1
with open("example.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is my first file\n")
print("File created and data written")

#2
with open("example.txt", "r") as f:
    content = f.read()
    print("\nFile content:")
    print(content)

with open("example.txt", "a") as f:
    f.write("New line added\n")
print("\n New line appended")

#3
with open("example.txt", "r") as f:
    print("Updated file content:")
    print(f.read())

#4
shutil.copy("example.txt", "backup.txt")
print("\n File copied (backup.txt created)")

#5
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("\n example.txt deleted")
else:
    print("\nFile not found")
