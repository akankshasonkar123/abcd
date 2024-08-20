memo={}
def fabonnaci_series(n):
    if(n==1 or n==2):
        return 1
    if(n>2):
        memo[n]=fabonnaci_series(n-1)+fabonnaci_series(n-2)
        return memo[n]
print(fabonnaci_series(10))