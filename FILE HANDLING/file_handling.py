"""File handiling is an important part of any web scripting language....
    Python has capability to handle a file using 
    python we can create a new file as well as we can read the file.
    
    To handle a file we use open() method.
    
    Example :- 
    f = open("file.txt)
    print(f.read())
    
    OPEN METHOD :- This method is use to open a file in specified mode...
    This method has two parameter :-
        1. First is the name of the file and 
        2. Second is the mode to open.
        
        SYNTAX :-
        open(filename or path , mode)
        
        MODE:-
        1. .read(r):- Read only mode. This is read the file if file is not exist this mode generate a error.
        
        2. .write(w):- This mode is used to write teh data into a file. 
                       If file dpes not exist this mode create a new file. If the file exist thes mode replace the file.
                      
        3. .append(a):- This mode append the data at the end of the file . If file does not exist this mode create a new file.
        
        4. .write(x):- This mode is used to write data into a file. If file does not exist this mode create a new file.
                       If file exist this mode dose not replace the iold file. 
        
        """
        
# f = open("file_handling.txt","r")
# print(f.readline())

# f = open("file.html","r")
# print(f.readline())                # sirf ek line ko read krta h

# f = open("file.html","r")
# print(f.read())                    # puri file ko read krta h 
 
# f = open("file.html","r")
# print(f.readline(3))
# print(f.read(45))

# x=f.readlines()                   # Saari lines ko list me read karta hai
# # print(x)
# for i in x:
#     print(i)




# ============================================================
f = open("file_handling.txt","w")
f.write("""
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.""")

print("Success")

# =====================================================================
f = open("file_handling.txt","a")
f.write("Twinkle, twinkle, little star")
print("Succes")
# ==================================================
# WAP to create CRUD Operation on file using file handling in python 
# NOTE:- It is choice based.