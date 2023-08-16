import random;

print("Welcome...");
print("U have to guess a number between 1 and 100 provided 10 attempts to guess the number correcty as generated randomly by computer")
r=random.randint(1,100)
c=1;

while(c):
    print("Enter your guess.!!   ")
    n=int(input())
    for i in range(1,10):
        if(n<=100 and n>0):
            
            if n==r:
                print("you won at chance no  ",i );
                break;
            elif(n<r):
                print("Too low\n");
                print("Enter your next guess.!!   ")
                n=int(input())
            elif(n>r):
                print("Too High\n");
                print("Enter your next guess.!!   ")
                n=int(input())
        
            else:
                print("Invalid")
        else:
            print("Guessing bound is between 1 and 100\n")
            print("Enter your next guess.!!   ")
            n=int(input())
   
    if(i==9) and n!=r:
        print("Oops.!!, You Lost ...Try Again.!!")
    print("\n1- Play Again\n0- Exit")
    c=int(input());
    if(c==0):
        print("Thank You.!!!")





