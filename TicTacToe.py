matrix = []
for i in range(3):
    row = input().split()
    matrix += [row]
res = "" 
for row in matrix:
    count_1 = 0
    count_2 = 0
    for i in range(3):
        if row[i]=="O" :
            count_1 += 1 
        if row[i]=="X" :
            count_2 += 1    
    if count_1 ==3:
        res = "Abhinav Wins"
        break
    if count_2 ==3:
        res = "Anjali Wins"
        break
    
for i in range(3):
    count_1 = 0
    count_2 = 0
    for row in matrix:
        if row[i]=="O":
            count_1 += 1 
        if row[i]=="X":
            count_2 += 1     
    if count_1 ==3:
        res = "Abhinav Wins"
        break
    if count_2 ==3:
        res = "Anjali Wins"
        break

count_1 = 0
count_2 = 0
for i in range(3):
    if matrix[i][i]=="O" :
        count_1 += 1 
    if matrix[i][i]=="X" :
        count_2 += 1     
if count_1 ==3:
    res = "Abhinav Wins"
if count_2 ==3:
    res = "Anjali Wins"   
    
con = 2   
count_1 = 0
count_2 = 0
for i in range(3):
    j = con - i 
    if matrix[i][j]=="O":
        count_1 +=1 
    if matrix[i][j]=="X":
        count_2 +=1     
if count_1==3:
    res = "Abhinav Wins"
if count_2==3:
    res = "Anjali Wins"
    
if res=="":
    print("Tie")
else:
    print(res)
