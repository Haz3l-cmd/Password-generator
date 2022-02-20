import random
import sys

#This array stores ascii characters excluding contro; characters
letters  =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',  ']', '^', '_', '`', '{', '|', '}', '~']
#Each character of the generated in appended to this array
pass_arr = []
help = '\n\nSynopsis :\n\npython [option] [filename]\n\nThis small python program ramdomly generates a password of any length and stores it in a file. *NOTE file is specified on cli, for more info run program with -h or --help.\n\nOptions :\n\n-c, --create     Creates a file with specified name\n\n-h, --help    prints helpful informations\n\n'

#Checks for number of arguements 
if len(sys.argv) == 3 :
 
 #Checks if 2nd arguement = '-c' i.e the one after the program name   
 if sys.argv[1] == '-c' or sys.argv[1] == '--create' : 
    
    #Asks user for password length, stops program if variavlie pass_len is not an integer
    try:
        pass_len = int(input("Enter passowrd length : "))
    except ValueError:
        print(" ERROR : Invalid input, make sure to enter value of type integer")
        sys.exit("__Program has stopped executing__")

    i =  0
    
    #Generating the random password
    while i < pass_len :
        rdm_val = letters[random.randint(0, len(letters)-1)]
        pass_arr.append((f"{rdm_val.replace(' ', '')}"))
        i += 1
    
    #Joins character from the pass_arr  to actually form the password
    pass_gen = ''.join(pass_arr)
    
    

    #Creates the file and appends the password
    with open(sys.argv[2], "a" ) as file:
        file.write(f"\nPassword generaetd is : {pass_gen}")
        file.close()

#Checks command line arguement and print the manual
elif len(sys.argv) == 2 :
    if sys.argv[1] == '-h' or sys.argv[0] == '--help' :
        print(help)

#Closes program if no conditions are met
else :
    sys.exit('Program takes 1 or 2 command line arguements\nRun program with -h or --help')
        




    

    
    