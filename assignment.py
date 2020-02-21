
list=[]
numberlist=int(input("Enter the length of list :"))
for x in range(numberlist):
    list_data=int(input("Enter list"))
    #numberlist.append(list_data)
    list.insert(x,list_data)
print(list) 
slice1=int(input("Input slice start number :"))
slice2=int(input("Input slice start number :"))
list=list[slice1:slice2]
list.sort()
print("sorted slice: " ,list)




"""lengthOfList=int (input("Enter the length of list :- "))
list=[]
for i in range(lengthOfList) :
    list.insert(i,int (input("Enter element in list:-")))

print(list)
sliceStart=int(input("Slice Start :- "))
sliceEnd=int(input("Slice End :- ")
list=list[sliceStart:sliceEnd]
list.sort()
print(list)  """