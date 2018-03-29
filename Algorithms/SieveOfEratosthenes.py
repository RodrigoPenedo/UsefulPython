def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    i = 2 #number we start from
    
    while i * i <= n:
        #ignore any number that's excluded already
        if prime[i]:
            
            #remove all multiples of the number, increment by i
            for num in range(i * 2, n+1, i):
                prime[num] = False
        i += 1
    #Prints all prime numbers
    for num in range(2, n):
        if prime[num]:
            print(num)
