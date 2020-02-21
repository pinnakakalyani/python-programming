#sets will not have Duplicates
number_set={5,20,13,5,6,20,5}
print(number_set)

mixed_type={4,5,6,(55,5,10)}
print(mixed_type)

number_list=[4,5,4,5,6,7]
number_set=set(number_list)
print(number_set)
number_set.add(5) # it wont add number to set because its already exist
print(number_set)
number_set.add(10)
print(number_set)

#remove item fron set
number_set.remove(5)
print(number_set)

#will throw key error as 38 is not present
#number_set.remove(38)
#print(number_set)

#Discard will remove element if it was not present it wont through error
number_set.discard(34)
print(number_set)

#pop item for set
print(number_set.pop())

#unions and intersections
score1={58,78,68,98,38}
score2={18,28,38,48,78}
print(score1.union(score2))
print(score1.intersection(score2))

#subraction
#those element of score1 which are not in score 2
print(score1)
print(score2)
print(score1-score2)
print(score2-score1)

for s in score1:
    print(s in score1)
    print()

#clear - it will cleare all the elements in set
number_set.add(28)
print(number_set)
number_set.clear()
print(number_set)

#frozen set- it is used to freez the set
number_set.add(4)
number_set.add(3)
number_set.add(5)
print(number_set)
freeze=frozenset(number_set)
print(freeze)

# could not able to add or modify frozenset
#freeze.add(7)
#print(freeze)
