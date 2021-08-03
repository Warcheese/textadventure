import var
from var import player
from helper import emit
from colorama import Fore, Style

def execute_command():    
    words = read_command()
    for article in var.text_article:
        while article in words:
            words.remove(article)
    if words:
        #MOVE
        if words[0] in var.text_move:
            if len(words) > 2 and words[1] in var.text_to:
                execute_go(words[2])
            elif len(words) > 1:
                execute_go(words[1])
            else:
                emit("Wohin soll ich gehen?", color=Fore.BLUE)                             
        elif words[0] in var.current_room.directions:
            execute_go(words[0])
        #INSPECT
        elif words[0] in var.text_inspect:
            if len(words) > 1:
                execute_inspect(words[1])
            else:
                emit("Was soll ich untersuchen?", color=Fore.BLUE)
        #TAKE
        elif words[0] in var.text_take:
            if len(words) > 1:
                execute_take(words[1])
            else:
                emit("Was soll ich nehmen?", color=Fore.BLUE)
        #USE
        elif words[0] in var.text_use: 
            if len(words) > 1:
                if len(words) > 3 and words[2] in var.text_combine:
                    execute_use_with(words[1], words[3])
                else:
                    execute_use(words[1])            
            else:
                emit("Was soll ich machen?", color=Fore.BLUE)        
        #END
        elif words[0] == "ende":
            emit("E N D E", color=Fore.WHITE, timer=var.text_speed*5)
            return False
        #EASTER EGGS
        elif words[0] in var.easter_eggs:
            emit("Geisterhafte Stimme des Entwicklers: " + var.easter_eggs[words[0]], color=Fore.CYAN, timer=var.text_speed*5)        
        #TODO: HILFE
        #TODO: In die Tasche schauen
        else:
            emit("Ich verstehe '%s' nicht." % " ".join(words), color=Fore.RED)            
    return True

def read_command():
    print()
    print(Fore.YELLOW + "Befehl: ", end="")    
    print(Fore.GREEN, end="")
    return [word.lower() for word in input("").rstrip(",.?!§$%&").split()]

def execute_go(direction):
    emit("==> Gehe nach '%s'" % direction.capitalize(), color=Fore.BLUE, timer=var.text_speed*5) 
    room = var.current_room.exits.get(direction)
    if room:
        enter_room(room)
    else:                
        emit("Ich kann nicht nach '%s' gehen." % direction.capitalize(), color=Fore.RED)        

def execute_take(item):
    emit("==> Nehme '%s'" % item.capitalize(), color=Fore.BLUE, timer=var.text_speed*5)
    if item in ([var.current_room.name.lower()] + var.text_place):
        var.current_room.take()    
    elif item in var.current_room.getItemNames():
        var.current_room.getItem(item).take()
    elif item in player.getItemNames():
        emit("Ich habe '%s' bereits in meiner Tasche." % item.capitalize(), color=Fore.RED)
    else:        
        emit("Ich finde '%s' nicht." % item.capitalize(), color=Fore.RED)        

def execute_use(item):
    emit("==> Benutze '%s'" % item.capitalize(), color=Fore.BLUE, timer=var.text_speed*5)    
    if item in ([var.current_room.name.lower()] + var.text_place):
        var.current_room.use()
    elif item in var.current_room.getItemNames():
        var.current_room.getItem(item).use()
    elif item in player.getItemNames():
        player.getItem(item).use()    
    else:        
        emit("Ich finde '%s' nicht." % item.capitalize(), color=Fore.RED)        

def execute_use_with(item1, item2):
    #TODO implement use with and test this stuff
    if item1 in (var.current_room.getItemNames() + player.getItemNames()):
        if item2 in (var.current_room.getItemNames() + player.getItemNames()):
            if item1 in var.current_room.getItemNames():
                var.current_room.getItem(item1).runCombination(item2)
            else:
                player.getItem(item1).runCombination(item2)
                #TODO rund function
        else:
            emit("Ich finde '%s' nicht." % item2.capitalize(), color=Fore.RED) 
    else:
        emit("Ich finde '%s' nicht." % item2.capitalize(), color=Fore.RED)        

def execute_inspect(item):
    emit("==> Untersuche '%s'" % item.capitalize(), color=Fore.BLUE, timer=var.text_speed*5)    
    if item in ([var.current_room.name.lower()] + var.text_place):
        var.current_room.describe()
    elif item in var.current_room.getItemNames():
        var.current_room.getItem(item).describe()
    elif item in player.getItemNames():
        player.getItem(item).describe()    
    else:        
        emit("Ich finde '%s' nicht." % item.capitalize(), color=Fore.RED)        

def enter_room(room):    
    var.current_room = room
    room.describe()

    