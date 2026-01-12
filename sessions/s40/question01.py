"""
Create a function called lineNumbers() that takes no parameters.  It should
open a file called 'test.txt', read each line, and produce an output file
with line numbers at the beginning of each line.  Let's name the output file
output.txt.


Hi
There
Stuff

1 Hi
2 There
3 Stuff
"""
def lineNumber():
    fin = open("test.txt","r")
    fout = open("output.txt","w")

    count = 1

    for line in fin:  #line = fin.readline()
        line_to_write = str(count)+" "+line
        fout.write(line_to_write)
        count += 1

    fin.close()
    fout.close()
