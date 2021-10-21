def fac(n):
        factorial=1
        for i in range(n):
          factorial=factorial * (i+1)
          print(factorial)
def trailinffac(n):
  count=0
  i=5
  while(n//i!=0):
    count+=int(n/i)
    i=i*5
    return count

if __name__ == '__main__':
    n=int(input("Enter a number:"))
    # fa=fac(n) 
    print(trailinffac(n))
