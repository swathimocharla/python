import random
num=8
tri=[]



for i in range(1, num+1):
    a=[]
    for j in range(1, (i*2)):
        a.append(random.randint(1,9))
    tri.append(a)
#print tri    

for i in range(1, num+1):
    for j in range(num -  i,  0,  -1):
        print("    "),
    for j in tri[i-1]:
        print(format(j, "4d")),
    print
    
for j in range(num-2,-1, -1):
    for i in range(0,len(tri[j])):
        tri[j][i]+= min (tri[j+1][i],tri[j+1][i+2])
        # print tri[j][i]
        
print ("shortest path:  ")
print tri[0][0]