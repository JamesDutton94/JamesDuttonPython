#James Dutton (this program will give all the numbers that are prime from 2 to the upper limit)
N = int(raw_input("Please enter a number as an upper limit: "))

for i in range(2,N):
    check_var = True;
    for k in range(2,i):
        if (i%k)== 0:
            check_var = False
    if check_var:
         print(i)

