#def sum_ave():
numbers=[10,20,30,35,35]
arraycount=len(numbers)
print(arraycount)
count=0
sum=0
while count<arraycount:
    sum+=numbers[count]
    count+=1
print(sum)
#sum_ave[10,20,30,35,35]

def sum_ave(a:int,b:int,c:int,d:int,e:int)->int:
    numbers=[a,b,c,d,e]
    arraycount=len(numbers)
    print(arraycount)
    count=0
    sum=0
    while count<arraycount:
        sum+=(numbers[count])
        count+=1
    return sum
results=sum_ave(20,23,19,30,45)
otheresults=sum_ave(1,2,3,4,5)
print(results)
print(otheresults)

    