import unittest
import os

def diagonalDifference(arr):
    r, l = 0, 0 
    for n in range(len(arr)):
        for m in range(len(arr[n])):
            if n == m:
                r += arr[n][m] 
                
            if (n+m == len(arr)-1):
                l += arr[n][m] 
                  
    return abs(r-l)

def plusMinus(arr):
    n = len(arr)
    po = 0
    ne = 0
    ze = 0
    count = 0
    condition = True
    
    while(condition):
        
        # process
        if arr[count] == 0:
            ze += 1
        elif arr[count] > 0:
            po += 1
        elif arr[count] < 0:
            ne += 1
        
        # increment
        count += 1
        
        # end loop
        if count == n:
            condition= False
            
    print("{:.6f}".format(po/n))
    print("{:.6f}".format(ne/n))
    print("{:.6f}".format(ze/n))
    print(f"count positivos: {po/n}, negativos: {ne/n}, zeros: {ze/n}")

def staircase(n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        print("#"*(i+1))
    
    for j in range(n-1, 0, -1):
        print(" "*(n-j), end="")
        print("#"*j)
        

def main():
    os.system("clear")
    # input
    n = 10
    staircase(n)
    
   
    


if __name__ == "__main__":
    main()
