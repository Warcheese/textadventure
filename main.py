import colorama
import resources
from var import start_room
from interface import enter_room, execute_command

def play():    
    enter_room(start_room)
    while execute_command():
        pass

if __name__ == "__main__":
    colorama.init()
    play()