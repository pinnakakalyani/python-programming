'''
try:
    pass
except expression as identifier:
   pass
else:
    pass

'''
try:
    fh=open("myfile.txt","w")
    fh.write("File exception!")

except BaseException as exception:
    print("Error while working with file",exception)

else:
    fh.close()
    print("File operation successful")
