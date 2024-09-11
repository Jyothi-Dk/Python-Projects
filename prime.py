flag=0
def is_prime(n):
    global flag
    
    """Check if a number is prime."""
    if n==0 or n==1:
        print("It's not a prime number")
    for i in range(2,n):
        if n % i == 0:
            flag=1
            break
    if flag==1:
        print("It's not a prime number")
    else:
        print("It's a prime number")
    
            
num=int(input("Enter a number:"))
is_prime(num)

