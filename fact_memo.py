memo = {}
def fab_n(n):
    if(n==0 or n==1):
        return 1
    if(n>=2):
        memo[n]=(n*fab_n(n-1))
        return memo[n]
     
for i in range(0,999):   
     print ("i:",fab_n(i))