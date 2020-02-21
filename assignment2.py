
data1=input("search the key: ")
data2=input("replace the key:")

with open ("python.txt","r") as fh:
    content=fh.readlines()
    content=content.replace(data1,data2)
fh.close()
with open ("python.txt","w") as f:
    f.write(content)
f.close()

