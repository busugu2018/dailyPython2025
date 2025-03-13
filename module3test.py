# Question 1
# An operator able to check whether two values are equal is coded as: ==

#Q2
# x = 1
# x = x == x        #True

#Q3
i = 0
while i <= 3 :
    i += 2
    print("*") #2

#Q4
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")    #one

#Q5
for i in range(1):
    print("#")
else:
    print("#")

#Q6
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")   #6

#Q7
var = 1
while var < 10:
    print("#")
    var = var << 1  #     4 * ####

#Q8
z = 10
y = 0
x = y < z and z > y or y > z and z < y #True

#Q9
a = 1
b = 0
c = a & b #------> 0
print(c)

a = 1
b = 0
c = a & b
print(c)
d = a | b
print(d)
e = a ^ b
print(e)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
 
print(c + d + e)


#Q10
my_list = [3, 1, -2]
print(my_list[my_list[-1]])

#Q11
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

#Q12
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]

#Q13
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(sum(vals))

#Q14
nums = [1, 2, 3]
vals = nums
del vals[1:2]

#Q15
nums = [1, 2, 3]
vals = nums[-1:-2]
print(vals)

#Q16
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

#Q17
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

#Q18
my_list = [i for i in range(-1, 2)]

#Q19
t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

#Q20
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])






