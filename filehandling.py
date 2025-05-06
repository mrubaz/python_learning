# for read a file
# f = open("myfile.txt", "+r")
# print(f.read())
# f.close()

# for append mode
# f = open("myfile1.txt", "+a")
# text = f.write("\nI have 2+ years of expereince as a Software Engineer")
# f.close()

# For opening binary file like jgp, jpeg, pdf, image file, etc. we use "rb"
# f = open("myfile2.txt", "+rb")
# print(f.read())
# f.close()

# "with" statement, it doesn't need close function

with open("myfile.txt", "r") as f:
    print(f.read())
