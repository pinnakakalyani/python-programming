"""
    File IO
    1.
    Open the file in specific mode.
    2.it will return filehandle
    3.use the filehandle to do file operation (read,write,change,delete,change attribute)
    4.close file handle
"""

fh=open("01.py", "r")
print(fh.name)
print(fh.mode)
print(fh.closed)
fh.close()
print(fh.closed)

print("------------------------------")

with open("01.py", "r") as fh:
    print(fh.name)
    print(fh.mode)
    print(fh.closed)
print(fh.closed)


with open("python.txt", "w") as fh:
    fh.write("Hello python \n")
    fh.write("In new line")
    print("------------------------------")

fh=None


with open("python.txt","a") as fh:
    fh.write("\n Hello again python \n")
    fh.write("next is fun")

#open file in read mode and write to console

with open("python.txt","r") as fh:
    content=fh.readlines()
    print(content)
    for r in content:
        print(r)


# read data from file in chunk size
with open("python.txt","r") as fh:
    content1=fh.read(10)
    content2=fh.read(10)
    content3=fh.read(10)
    print(content1)
    print(content2)
    print(content3)
    print(fh.tell())

    #seek (how much do i want to seek, from where)
    #possible values of form where
    # 0-> pointer shift will start from begining offset
    #1-> pointer shift will start from current offset
    #2->EOF wil be current offset

fh.seek(11,0)
print(fh.tell())
print(fh.read(7))
print(fh.tell())
fh.seek(11,1)

#copy data from one file to another file
#with open("eclipse.png","rb") as fh:
    


