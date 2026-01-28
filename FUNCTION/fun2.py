# no return with argument

def user_login(x):
    print("hii",x)
    
user_login(10)



# return with argument 

def user_login(x):
    return x
    
y=user_login(10)
y

# --------------------------------
def user_login(age):
    if(age<18):
        return False
    else:
        return True
    
x=int(input("enter your age"))
var=user_login(x)
if(var==True):
    print("vote")
    
else:
    print("not vote")
    

# ----------------------------------
def user_login(x=5):
    for i in range(1,x+1):
        for i in range(1,i+1):
            print(i,end=" ")
        print() 
        
user_login()

# -----------------------------
def user_login(x=5):
    for i in range(1,x+1):
        for i in range(1,x+1):
            print(i,end=" ")
        print() 
        
user_login()

# ---------------------------------
def user_login(x=5):
    for i in range(1,x+1):
        for i in range(1,i+1):
            print("*",end=" ")
        print() 
        
user_login()

# ----------------------------------------

def user_login(x=5):
    for i in range(1,x+1):
        for j in range(1,x+1):
            if(i==1 or i==5 or j==1 or j==5):
                print("*",end=" ")
                
            else:
                print(" ", end=" ")
                
        print()
        
user_login()

