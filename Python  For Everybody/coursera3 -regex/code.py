import re
file=open("file.txt")
# for line in file:
#     line=line.rstrip()
#     print(line)
f=file.read()
numbers=re.findall('[0-9]+', f)
print(numbers)
print(type(numbers[1]))
sum =0
for i in numbers:
    print (i)
    sum=sum+int(i)
print("sum of numbers is :", sum)