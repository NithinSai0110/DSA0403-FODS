import numpy as n
scores= n.array([[90,82,79,69],[88,98,79,89],[33,78,66,97],[79,82,91,73]])
avg=n.mean(scores,axis=0)
print("The avarage of scores of students are:",avg)
sub=n.argmax(avg)
subnames=n.array(["Math","Science","English","History"])
print("The sub with hieghst avarage is:",subnames[sub])
av=[]
for i in range(len(scores[0])):
               s=0
               for j in scores:
                   s+=j[i]
               av.append(s/4)
print(subnames[av.index(max(av))],"has highest average :",max(av))
print(subnames[av.index(min(av))],"has lowest average :",min(av))