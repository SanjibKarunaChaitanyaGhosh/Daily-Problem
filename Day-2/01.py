# Fibonacci series

arr = [0,1]

nextDigit = 0

def fibonacci(n):
    if n<3 :
      print(arr)
    else : 
       for i in range(n-2):
            nextDigit = arr[i]+arr[i+1]
            arr.append(nextDigit)
    print(arr)

            
    reverseFibonacci = [arr[i-1] for i in range(len(arr),0,-1)]
    print("Reverse fibonacci series is..........\n",reverseFibonacci)

n=int(input("Enter any number : "))
fibonacci(n)

