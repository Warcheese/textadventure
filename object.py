import var
from helper import emit
from helper import RepresentsInt
from colorama import Fore, Style

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):                
        emit(self.name, color=Fore.MAGENTA)
        emit(self.description)
    
    def use(self):                
        emit("Ich kann '" + self.name + "' nicht benutzen.", color=Fore.RED)                
    
    def take(self):               
        emit("Ich kann '" + self.name + "' nicht nehmen.", color=Fore.RED)

class Room(Object):
    def __init__(self, name):
        super().__init__(name, {})        
        self.items = {}
        self.exits = {}        
        self.directions = []

    def describe(self):
        desc = ""
        for k, v in self.description.items():
            if RepresentsInt(k) or (k.lower() in self.getItemNames()):
                desc = desc + " " + v        
        emit(self.name, color=Fore.MAGENTA)        
        emit(desc.rstrip(), keywords1=self.getItemNames(), keywords2=self.directions)

    def addDescription(self, text, item=None):
        if item:
            self.description[item.name] = text
        else:            
            self.description[len(self.description)] = text    

    def getItemNames(self):
        list = []
        for key in self.items:
            list.append(self.items[key].name.lower())
        return list

    def getItem(self, name):
        if name.lower() in self.items:
            return self.items[name.lower()]
        else:
            emit("***ERROR***", color=Fore.RED)
            emit("Das Item '%s' ist nicht vorhanden!" % name, color=Fore.RED)  

    def addItem(self, item):
        if item.location is None:
            self.items[item.name.lower()] = item
            item.location = self.name
        else:
            emit("***ERROR***", color=Fore.RED)
            emit("Das Item '%s' wird noch woanders verwendet!" % item.name, color=Fore.RED)
        
    def addExit(self, direction, exits):
        self.directions.append(direction)
        self.exits[direction] = exits

    def removeExit(self, direction):
        while direction in self.directions:
            self.directions.remove(direction)
        del self.exits[direction]

    def removeItem(self, item):
        if item.name.lower() in self.items:
            del self.items[item.name.lower()]
            item.location = None
        else:
            emit("***ERROR***", color=Fore.RED)
            emit("Kann das Item nicht aus dem Raum entfernen.", color=Fore.RED)

class Item(Object):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.location = None
        self.combinations = {}
        self.text_use_player = "Was soll ich mit '"+ self.name + "' machen?"
        self.text_use_room = "Ich kann '"+ self.name + "' nicht benutzen."

    def use(self):
        if self.location is "Player":                   
            emit(self.text_use_player, color=Fore.MAGENTA)            
        else:                    
            emit(self.text_use_room, color=Fore.MAGENTA)
    
    def addCombination(self, item, function):
        self.combinations[item.name.lower()] = function
    
    #TODO use with functionality
    def runCombination(self, itemName):
        if itemName in self.combinations:   
            self.combinations[itemName]("wurst")   
            return True
        else:            
            return False            

### Common Item Functions ###
def take_item(self):
        var.current_room.removeItem(self)
        var.player.addItem(self)