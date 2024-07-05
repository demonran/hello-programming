#coding=UTF-8
while True:
    num = raw_input("Enter a number :")
    print "You enterd: ",num
    if int(num) == 0:
        break;
print "Good bye","saf"

fruits = ['banana', 'apple',  'mango']
print len(fruits)

print range(len(fruits))

for x in range(len(fruits)):
    print '当前:',x
    
for x in range(2,10,2):
    print x