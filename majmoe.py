y = int(input('please write number : '))
sum = 0
sumb = 0
for i in range(y+1):
    if(i%2):
        sum +=i

    if(i%5 ==  0):
       sumb +=i
print(sumb+sum)
