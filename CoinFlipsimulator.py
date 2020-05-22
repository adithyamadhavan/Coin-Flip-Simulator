
import random 
N = int(input("Enter number of times need to be flipped:"))
for i in range(0,N):
    flip =  random.randint(0,1)
    userans = input("Heads or Tails:")
    if flip == 1 and userans == "Heads":
        print("Heads")
    else:
         print("Tails")