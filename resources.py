import types
import var
import helper
from object import Item
from object import Room
from object import take_item

### Define all Items ###

# Mistgabel
mistgabel = Item("Mistgabel",
    "Eine alte Mistgabel. Der Holzgriff fühlt sich morsch an.")
mistgabel.take = types.MethodType(take_item, mistgabel)

# Haustür
haustür = Item("Haustür",
    "Die Haustür meines Elternhauses. Aus massivem Holz mit einem altmodischem Türstuck. Der Türknauf ist aus Messing und ziemlich in die Jahre gekommen.")

haustür.text_use_room = "Ich versuche die Tür zu öffnen...abgeschlossen."

# Tonschildkröte
tonschildkröte = Item("Tonschildkröte",
    "Eine kleine Schildkröte aus Ton. Schön ist was anderes...")

tonschildkröte.text_use_room = "Ich weiß nicht was ich damit machen soll..."

# Türklingel
türklingel = Item("Türklingel",
    "Eine alte Türklingel aus Messing. Sieht ziemlich abgegriffen aus. Ob sie noch funktioniert?")

türklingel.text_use_room = "Ding Dong ... nichts passiert."

### Define all Rooms ###

# define play room
player = Room("Player")

# define all rooms
vorgarten = Room("Vorgarten")
vorgarten.addDescription("Du stehst vor deinem Elternhaus. Der kleine Weg der durch den Vorgarten zu der Haustür führt ist auf beiden Seiten gesäumt mit vertrockneten Rosen. "
    "In der Dunkelheit sieht das Haus irgendwie bedrohlich aus. Neben der Eingangstür ist der alte gelbe Briefkasten.")
vorgarten.addDescription("Die Türklingel ist aus Messing und schon ziemlich abgegriffen.", türklingel)
vorgarten.addDescription("Hinter den Rosen steht ein kleiner Misthaufen in dem eine Mistgabel steckt.", mistgabel)
vorgarten.addDescription("Am Fuß der Haustür steht immer noch die alte Tonschildkröte.", tonschildkröte)
vorgarten.addDescription("Zwischen den Rosen führt ein kleiner Pfad um das Haus herum in den Garten.")

garten = Room("Garten")
garten.addDescription("Ahhh der Garten, mit einem Pfad und einer Tür zur Gartenlaube.")

gartenlaube = Room("Gartenlaube")
gartenlaube.addDescription("Was ist denn in der Gartenlaube los? Hinter dir führt die Tür wieder in den Garten.")

# add exits
vorgarten.addExit("pfad", garten)
garten.addExit("pfad", vorgarten)
garten.addExit("tür", gartenlaube)
gartenlaube.addExit("tür", garten)

# add items
vorgarten.addItem(mistgabel)
vorgarten.addItem(türklingel)
vorgarten.addItem(tonschildkröte)
vorgarten.addItem(haustür)

# add combinations
mistgabel.addCombination(tonschildkröte, helper.emit)

### Set Start Parameters ###

var.start_room = vorgarten
var.player = player