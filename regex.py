import re
file=open("regex_sum_2063084.txt","r")
sum=0
for line in file:
    numbers=re.findall('[0-9]+',line)
    for number in numbers:
        sum+=int(number)
print(sum)