'''
    Filter

    it works on iterable!
    works with two parameters
    1.Function name/lambda
    2.iterable

    function named/lambda will evaluate for each item in iterable

    map->it will 


'''

numbers=[55,45,65,85,22,13,5,88,78]
selectes=filter(lambda a:a>45, numbers)
print(list(selectes))

evennumber=filter(lambda a:a%2 ==0, numbers)
print(list(evennumber))

oddnumber=filter(lambda a:a%2 !=0, numbers)
print(list(oddnumber))

palindromlist=["madam","malayalam","peep","chick","amore, roma","daga"]
palin=list(filter(lambda x: (x=="". join(reversed(x))),palindromlist))
print(palin)

palin=list(filter(lambda x: (x== x[::-1]),palindromlist))
print(palin)

alphabets=['a','b','c','d','e','f','g','h','i']
vowel=['a','e','i','o','u']
checkvowelsinalpha=filter(lambda alpha:alpha in vowel, alphabets)
print(list(checkvowelsinalpha))



