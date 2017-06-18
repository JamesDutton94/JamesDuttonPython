#James Dutton
#hw2c Diopphantine equation in python
#define globals
A = 6
B = 9
C = 20
#prototype function call
#function recursively calls as it decrements x
def solveDis(x):
    #Check to see if it is divisible by 9
    if (x % B) == 0:
        x = x - B
        #Once it is 0 let the user know
        if(x == 0):
            print("It worked")
            print(B)
        else:
            solveDis(x)
            print(B)
    elif x % 3 == 0:#Second, check to see if it is divisible by 3 
        if (x - B)%C==0:
            x = x - B
            solveDis(x)
            print(B)
        elif x >= A:
            x = x - A           
            if x == 0:#If it is 0 let user know it worked                
                print("It Worked")
                print(A)
            else:
                solveDis(x)
                print(A)
    elif x  > C:#Make sure the number is larger than 20 then subtract
        x = x - C
        solveDis(x)
        print(C)        
    else:#If it does not fit these criteria it will not work.
        print("Does not work")
        
     

T = int(raw_input("Please enter a number of chicken nuggets (0 will end the program: "))
while T != 0:
    solveDis(T)
    T = int(raw_input("Please enter a number of chicken nuggets (0 will end the program: "))




