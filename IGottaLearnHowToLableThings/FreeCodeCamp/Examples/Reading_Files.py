
#This assigns a var to a File 
xfile = open('Ex04_06.py')




#File Handle as a Sequence
def SequenceHandle():
    for cheese in xfile:
        print(cheese)

#Counting Lines in a File

def CountLine():
    count = 0
    #Use for loop to read each line
    for file in xfile:
        count += 1
    print('Line Count', count)


#Read everything
def Count_Whole_Line():
    
    #inp is the file
    inp = xfile.read()
    #len reads the file and reads the total
    print(len(inp))


#searches for line with the word If as their prefix...
def Search_Through_File():
    for line in xfile:
        #rstrip gets rid of white space in the right side
        line = line.rstrip()
        if line.startswith('if ') :
            print(line)        

#Skipping with continue
def SkippingAndContinue():
    for line in xfile:
        line = line.rstrip()
        if not line.startswith('if') :
            continue
    print(line)


#Prompt file name

def PromptFile():
    fname = input('Enter the file name: ')
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith('def '):
            count += 1
    print('There were', count, 'subject lines in', fname)

def QUIT():
    if input("Choose input: ").upper() == "Quit":
        print("you quitted!")


