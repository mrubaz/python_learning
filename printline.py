# f = open("myfile2.txt", "r")
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break


# for read single file
# f = open("myfile2.txt", "r")
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of Student {i} in SSt is :{m1}")
#     print(f"Marks of Student {i} in Math is :{m2}")
#     print(f"Marks of Student {i} in Urdu is :{m3}")

# for write single in the file and you cal also append with a and append function as well
f = open("myfile2.txt", "w")
lines = []
for i in range(10):
    temp = f"\nLine{i+1}"
    lines.insert(i, temp)
f.writelines(lines)
f.close()
