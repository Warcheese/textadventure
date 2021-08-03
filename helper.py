import time
from colorama import Fore, Style
from var import text_speed

def emit(s="", width=80, timer=text_speed, color=Fore.WHITE, keywords1=[], keywords2=[]):    
    column = 0
    print()
    for word in str(s).split():
        column += len(word) + 1
        if column > width:
            column = len(word) + 1
            print()
        if word.rstrip(",.?!§$%&").lower() in [x.lower() for x in keywords1]:
            for char in word:
                print(Fore.YELLOW + char, sep="", end="", flush=True)
                time.sleep(timer)
        elif word.rstrip(",.?!§$%&").lower() in [x.lower() for x in keywords2]:
            for char in word:
                print(Fore.CYAN + char, sep="", end="", flush=True)
                time.sleep(timer)
        else:
            for char in word:
                print(color + char, sep="", end="", flush=True)
                time.sleep(timer)
        print(" ", end="")        
        time.sleep(timer)
    print()

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False