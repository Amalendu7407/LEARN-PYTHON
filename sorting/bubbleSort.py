no = [50,20,10,70,80,30,-78 , -1 , 0 , -88]
n = len(no)
for i in range(n):
    flag = False
    for j in range(n-i-1):
        if no[j] > no[j+1]:
            # swap
            no[j] , no[j+1] = no[j+1] , no[j]
            flag = True

    if flag == False :
        break
print(no)    

'''

TIME COMPLEXITY  = O(n*n)
SPACE COMPLEXITY = o(1)

'''