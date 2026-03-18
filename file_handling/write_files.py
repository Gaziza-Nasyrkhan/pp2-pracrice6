#1
with open("file1.txt", "w") as f:
    f.write("Hello World\n")

#2
with open("file2.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

#3
lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("file3.txt", "w") as f:
    f.writelines(lines)

#4
number = 123
with open("file4.txt", "w") as f:
    f.write(str(number))

#5
text = input("Enter text: ")
with open("file5.txt", "w") as f:
    f.write(text)
print("5 write examples done")