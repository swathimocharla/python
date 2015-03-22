'''
Created on Nov 29, 2014

@author: smocharl
'''
knapsack=5
#knapsack=32
items=[[5,3],[3,2],[4,1]]
#items= [[3,3],[1,4],[3,8],[4,10],[3,15],[6,20]]

print('item weights and values:')
print items

row= len(items)+1
col= knapsack

m = [[0 for i in range(col)] for i in range(row)]
size= len(items)

for i in (range(size)):
    for j in range(col):
        if items[i][1]>j+1:
            m[i+1][j]=0
        elif items[i][1]==j+1:
            m[i+1][j]=items[i][0]
        elif j+1>items[i][1]:
            temp= j-items[i][1]
            m[i+1][j]=items[i][0]+ m[i][temp]

        if m[i][j]>m[i+1][j]:
            m[i+1][j]= m[i][j]

print ('knapsack matrix:')            
print m
            
k = [[0 for i in range(col)] for i in range(row)]           

for i in (range(size)):
    for j in range(col):
        if m[i+1][j]> m[i][j]:
            k[i+1][j]=1
            
print ('keep matrix:')  
print k


j= knapsack
finalknapsack=[]
for i in range((size),0,-1):
    if k[i][j-1]==1:
        finalknapsack.append(i)
        j=j-items[i-1][1]           
    
    if j<=0:
        break

print ('finalknapsack:')
print finalknapsack
    
            
    



            
        