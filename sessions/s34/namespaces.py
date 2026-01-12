#This file contains some sample local and global variables
#to play with the idea of global and local namespaces

z = "I am global variable z"


def local_fun_one():
    #all variables created in this function are local
    #they cannot be accessed outside of this function
    x = 7
    y = "I am local variable y"
    print(x)
    print(y)
    
    return None


def local_fun_two():
    #all variables created in this function are local
    #they cannot be accessed outside of this function
    x = 4

    #what happens when I print x?  Which x is it?

    #what happens if I try to print y from the first
    #function?
    
    return None

def main():
    #what happens if I try to print local x or y?

    #what happens if I try to print global z?

    #what happens if I try to change global z?

    return None

    
    
