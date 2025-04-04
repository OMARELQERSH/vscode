with open("newfile.txt" , mode="w") as fd :
    fd.write("hello world\n")
    fd.writelines(["omar\n","adel\n","elqersh\n"])

with open("newfile.txt",mode="r") as fd:
    text1 = fd.read()
    text2 = fd.readline()
    text3 = fd.readlines()


print(text1)
print(text2)
print(text3)