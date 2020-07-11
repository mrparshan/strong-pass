import string
import random
import os
os.system("clear")
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    RED2 = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN2 = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

red = color.RED2
blue = color.BLUE 
white = color.WHITE
bold = color.BOLD
reset = color.RESET

while True:
    print(f"""{red}       					
					╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔╦╗╦═╗╔═╗╔╗╔╔═╗  ╔═╗╔═╗╔═╗╔═╗╦ ╦╔╦╗
					║  ╠╦╝║╣ ╠═╣ ║ ║╣   ╚═╗ ║ ╠╦╝║ ║║║║║ ╦  ╠═╝╠═╣╚═╗╚═╗║║║ ║║
					╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝  ╚═╝ ╩ ╩╚═╚═╝╝╚╝╚═╝  ╩  ╩ ╩╚═╝╚═╝╚╩╝═╩╝					
							   {bold} {blue}GITHUB: mrparshan
							   {bold}{blue}VERSION: WINDOWS{reset}
	{white}""")
    length = int(input(f"\n{white} [ + ] Enter your length password: {blue}"))
    print(color.WHITE)
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-/.~<>,?"
    password = "".join([random.choice(chars) for r in range(length)])
    show_pass = print(f"\n [***] Your password is\n " , color.GREEN2 , password , color.WHITE)
    while True:
        ask = input(f"\n [+] Do you want anthor password? [Y/n]: {blue}").lower()
        if ask == "n" or ask == "y":
            break
        elif ask != "n" or ask != "y":
            print(color.RED , "\n [ERR] Sorry, Try again." , color.WHITE)
    if ask == "n":
        print(f"""{white}
 
 +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ 
 |T|h|a|n|k|s| |f|o|r| |t|r|y|i|n|g| |t|h|i|s| |a|p|p|!| 
 +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ 

{white}""")
        break
    elif ask == "y":
        os.system("clear")        
