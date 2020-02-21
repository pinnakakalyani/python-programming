newdict={}
print(type(newdict))
# except float it can be any thing in key 
score={1:"monday","bigday":"tuesday",'a':"wednesday","friends":["ama","afa","afw"]}
print(score['bigday'])
print(score["friends"])

#create dictionary from list of tuples
friends=dict([("chennai",8),("mumbai",7),("hyderbad",9)])
print(friends)

print(friends["chennai"])
print(friends.get("hyderbad"))

friends.update({'mumbai':18})
print(friends)

#iterate through dictonary
for key,value in friends.items(): #without using items we will get an error ValueError: too many values to unpack (expected 2)
    print(key," : ", value)

#create a dictionary where key is string
#and values is lenght of string from the list strings!

friends=['amar','akbar','antony','tiger','lion']
#somedict={'amar':4,'akbar':5,'antony':6,'tiger':5,'lion':4}

somedict={value:len(value) for value in friends}
print(somedict)

# if key values are same it wont display all data
weekdays={1:"monday",2:"tuesday",3:"wednesday"}
month={11:"jan",12:"feb",13:"march"}
all={}
all.update(weekdays)
all.update(month)

print(weekdays)
print(month)
print(all)

#use unpacking operator to merge dictionaries! **
allunpacked={}
allunpacked={**weekdays,**month}
print(allunpacked)



