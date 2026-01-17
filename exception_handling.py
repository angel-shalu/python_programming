a = 10
b = 0

try:
    c=a/b
    print(c)
except:
    print("Not divisible by zero")
    
    
    
    
tp=()
while(True):
    print("""
press 1 for create a data:
press 2 for read the data:
press 3 for Update the data:
press 4 for delete the data:
press 5 for exit:
""")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        ls=list(tp)
        print("create the data:")
        ndata=int(input("Enter the no of data:"))
        for i in range(ndata):
            print(f"Enter the data {i+1}")
            data=input("Enter the data")
            ls.append(data)
            tp=tuple(ls)
    elif(ch==2):
        print("read the data:")
        for i in tp:
            print(f"your data={i}")
    elif(ch==3):
        print("update the data:")
        ls=list(tp)
        data=input("Enter the data to update:")
        try:
            x=ls.index(data)
            udata=input("Enter the updated data:")
            ls[x]=udata
            tp=tuple(ls)
        except:
            print("data not found")
    elif(ch==4):
        print("Delete the data:")
        ls=list(tp)
        data=input("Enter the data to update:")
        try:
            x=ls.index(data)
            ls.pop(x)
            tp=tuple(ls)
        except:
            print("data not found")
    elif(ch==5):
        print("Thanks for operations with us:")
        break
    else:
        print("choice is invlid")
        continue