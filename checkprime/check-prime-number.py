
def prime_checker(number):

    if(number/1==number and number/number == 1):
        if(number%2==0 or number%3==0):
            if(number>3):
                print("It's not a prime number.")
        else:
            print("It's a prime number.")        

n = int(input("Check this number: "))
prime_checker(number=n)
