#1
with open("file1.txt", "r") as f:
    print(f.read())

#2
with open("file2.txt", "r") as f:
    print(f.readline())

#3
with open("file2.txt", "r") as f:
    print(f.readlines())

#4
with open("file3.txt", "r") as f:
    for line in f:
        print(line.strip())

#5
with open("file3.txt", "r") as f:
    print(f.read(5)) 
print("5 read examples done")