import sys 
from time import sleep
# Takes first name and last name via command  
# line arguments and then display them
n=sys.argv[1] 
n=int(n)
f=open("new.csv","r")

for i in range(0,n+1):
    f.readline()
print(f.readline())
f.close() 
