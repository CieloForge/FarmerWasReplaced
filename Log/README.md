# The Journey of *The Farmer Was Replaced*:

---

## 📖 Overview

This is simply a document a person can read if desired that breaks down the entire playthough with code snippest within this readme, thus allowing them to understand my logic, thought processes, and copy/paste code without navigating other folders or file structures. 

## 📋 Table of Contents

- [First Launch:](#First-Launch:)

- [First Upgrade:](#First-Upgrade:)

- [Larger Map & New Crop:](#Larger-Map-&-New-Crop:)

- [First Basic MultiFarm:](#First-Basic-MultiFarm:)

- [The Reckoning of Variables and new Functions:](#The-Reckoning-of-Variables-and-new-Functions:)

- [The Refactoring and Trees](#The-Refactoring-and-Trees)

- [The Pumpkining](#The-Pumpkining)



---







### First Launch:

We are given the instructions in the First little Wiki Popup. Basically we are allowed at the start 3 functions we can call. The only important one is harvest(), which is what gains us hay...the resouce we will need for our first upgrade.

So since we need 5 hay for the first upgrade let us make a simple chain of calling the harvest function. Like so;

```python
harvest()
harvest()
harvest()
harvest()
harvest()
```

After that goes through we have enough to get our first upgrade.

### First Upgrade:

So we've gotten the hay required and now we can purcahse the first upgrade. This upgrade gives us the *while* function which really helps simplify and start our automation journey. This upgrade will now allow us to idle the game running the code;

```python
while True:
    harvest()
```

which just is an infinite while loop that harvests for us. We will run this until we have enough for the next following upgrades;

- Grass

- Speed

- Hats

The hats aren't really needed and can be skipped, its mearly cosmentic at this point. I'd recommend getting the speed first, but be forewarned you will have to change your code once you upgrade speed to this;

```python
while True:
    if can_harvest():
        harvest()
```

As with the speed upgrade you are actually faster than the growth rate of grass, thus without this check you would be harvesting grass that is still immature. Immature crops give 0 crop which is bad.  We will proceed to gain enough Hay until we can get the next upgrades;

- Bush

- Expand Level 1

### Larger Map & New Crop:

Now that the map is a little bigger and we have more functions we can use, along with a new crop/resource type. It is really starting to kick off one could say. So with these upgrades we should change our code to now use the entire map, however I personally think due to the difference in growing speeds between bushes and grass, its best to just single out a single crop for now. 

We will farm each crop until we have enough for the following upgrades;

- Speed Level 2

- Operators

- Senses

- Print

- Expand Level 2

- Carrots

Print function isnt required but it is helpful for debugging and unlocks the debugging functions tree which will be useful later.

So what I used for the hay farm with before getting the upgrades above was;

```python
while True:
    if can_harvest():
        harvest()
        move(North)
    else: 
        move(North)
```

Which can be simply modified for the bushes like so;

```python
while True:
    if can_harvest():
        harvest()
        plant(Entities.Bush)
        move(North)
    else:
        move(North)
```

We will use this until we can afford the upgrades above. We left the *Expand* for the last upgrade because it adds a little more logic and its best if we have the ability to tell where we are, which the *Senses* upgrade gives us. 

### First Basic MultiFarm:

Now that we have obtained the *Expand* upgrade again, we have the ability to move on the X axis. We also have the ability to grow carrots, and like the little wiki pop-up told us carrots can not just be planted. They require us to use the function till() to turn the tile into a plowed tile. They also have a slower growth cycle than bushes, but since we have 2 more additional columns we can now start our first mutli-row farm. Where each row will have a crop type. 

We can do this like this;

```python
while True:
    if get_pos_x() == 0:
        harvest()
        move(North)
        harvest()
        move(North)
        harvest()
        move(North)
        move(East)
    elif get_pos_x() == 1:
        if can_harvest():
            harvest()
            plant(Entities.Bush)
            move(North)
            if can_harvest():
                harvest()
                plant(Entities.Bush)
                move(North)
                if can_harvest():
                    harvest()
                    plant(Entities.Bush)
                    move(North)
                    move(East)
                else:
                    move(North)
            else: 
                move(North)
        else:
            move(North)
    elif get_pos_x() == 2:
        if get_ground_type() != Grounds.Soil:
            till()
            plant(Entities.Carrot)
            move(North)
            till()
            plant(Entities.Carrot)
            move(North)
            till()
            plant(Entities.Carrot)
            move(North)
        elif can_harvest():
            harvest()
            plant(Entities.Carrot)
            move(North)
            harvest()
            plant(Entities.Carrot)
            move(North)
            harvest()
            plant(Entities.Carrot)
            move(North)
            move(East)
        else:
            move(North)
    else:
        move(East)
```

It's not super ideal, and it lacks efficiency but overall it farms all 3 types of crop. Untill we have more advanced functions this is good enough. We will save up enough resources for the following upgrades:

- Expand Level 3 20

- Variables 35 

- Defs 40

### The Reckoning of Variables and new Functions:

Now that we have expanded some more, and gotten the ability to use variables and defs its sort of our next big milestone of efficiency and programming. With these we can do a lot more, and improve our farm signifcantly and start the base bones of what would eventually be a utility script.

Now our first Monolithic Script able to Move the drone, get the map size, and plant each time of crop. It will make the entire map one crop, x amount of times leading for a more efficient method of planting crops and it will also allow for tweaking what gets more by passing a variable into it. 

Annoyingly you have to have the defs above the while loop, but it will look something like this;

```python
global tilesMax
lc = 0
lm = 5 # Max times the while loop goes. 



def MoveDrone(tileAmount):
    mapSize = get_world_size() -1 # We subtract one because get_world_size() indexes at 1, not 0 like the drone
    for s in range(tileAmount):
        if get_pos_y() != mapSize:
            move(North)
        else:
            move(East)
            move(North)

def GetMaxTiles():
    global tilesMax
    tilesMax = get_world_size() * get_world_size()

def HarvestAllTiles():
    global tilesMax
    for t in range(tilesMax):
        harvest()
        MoveDrone(1)
    clear()

def TillAllTiles():
    global tilesMax
    HarvestAllTiles()
    for t in range(tilesMax):
        if get_ground_type() != Grounds.Soil:
            till()
        MoveDrone(1)

# Farm Loops

def HayFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            harvest()
            MoveDrone(1)
        loopCount += 1

def BushFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Bush)
                MoveDrone(1)
            elif get_entity_type() != Entities.Bush:
                plant(Entities.Bush)
            else:
                MoveDrone(1)
        loopCount += 1

def CarrotFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Carrot)
                MoveDrone(1)
            elif get_entity_type() != Entities.Carrot:
                plant(Entities.Carrot)
                MoveDrone(1)
            else:
                MoveDrone(1)

while lc < lm:
    GetMaxTiles()
    HayFarm(2)
    BushFarm(2)
    TillAllTiles()
    CarrotFarm(2)
    clear() # Added so you can redo hay and doesn't break the loop
    lc += 1
```

This will eventually be refactored into a utility script minus the while loop and its direct variables it checks for. 

### The Refactoring and Trees

After running the monolithic script for a little bit you should be able to afford our next upgrades:

- Speed Level 3

- Import

- Trees Level 1

- Trees Level 2

- Expand Level 4

Now with this we now can start refactoring and adding some new functions to a new script called utils

It will look like this;

```python
global tilesMax


def MoveDrone(tileAmount):
    mapSize = get_world_size() -1 # We subtract one because get_world_size() indexes at 1, not 0 like the drone
    for s in range(tileAmount):
        if get_pos_y() != mapSize:
            move(North)
        else:
            move(East)
            move(North)

def isTileEven(tile):
    return tile % 2 == 0

def GetMaxTiles():
    global tilesMax
    tilesMax = get_world_size() * get_world_size()

def HarvestAllTiles():
    global tilesMax
    for t in range(tilesMax):
        harvest()
        MoveDrone(1)
    clear()

def TillAllTiles():
    global tilesMax
    HarvestAllTiles()
    for t in range(tilesMax):
        if get_ground_type() != Grounds.Soil:
            till()
        MoveDrone(1)

# Farm Loops

def HayFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            harvest()
            MoveDrone(1)
        loopCount += 1

def BushFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Bush)
                MoveDrone(1)
            elif get_entity_type() != Entities.Bush:
                plant(Entities.Bush)
            else:
                MoveDrone(1)
        loopCount += 1

def CarrotFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Carrot)
                MoveDrone(1)
            elif get_entity_type() != Entities.Carrot:
                plant(Entities.Carrot)
                MoveDrone(1)
            else:
                MoveDrone(1)

def WoodFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            posX = get_pos_x()
            posY = get_pos_y()
            if isTileEven(posX) and isTileEven(posY):
                if can_harvest():
                    harvest()
                    plant(Entities.Tree)
                    MoveDrone(1)
                elif get_entity_type() != Entities.Tree:
                    plant(Entities.Tree)
                    MoveDrone(1)
                else:
                    MoveDrone(1)
            else:
                if can_harvest():
                    harvest()
                    plant(Entities.Bush)
                    MoveDrone(1)
                elif get_entity_type() != Entities.Bush:
                    plant(Entities.Bush)
                    MoveDrone(1)
                else:
                    MoveDrone(1)
        loopCount += 1
```

Then the main script will look something like ths;

```python
import Utils
lm = 1
lc = 0

while lc < lm:
    Utils.GetMaxTiles()
    Utils.HayFarm(20)
    Utils.WoodFarm(20)
    Utils.TillAllTiles()
    Utils.CarrotFarm(5)
    clear()
    lc += 1
```

As you can see much cleaner and easier to manage, another cool thing we can do is make a conditional statement to keep doing a specific farm until we have enough for a specific upgrade we might want, or to make sure we have enough of a resource.

Which I like to keep track of stored resources and resource logic parts in their own script for clean use.  It will look something like this;

```python
# Global Variables 
storedHay = 0
storedWood = 0
storedCarrots = 0


# Get all Stored Reosurces:
def GetAllStored():
    GetStoredHay()
    GetStoredWood()
    GetStoredCarrots()

# Get Items Fucntions
def GetStoredHay():
    global storedHay
    storedHay = num_items(Items.Hay)
    return storedHay

def GetStoredWood():
    global storedWood
    storedWood = num_items(Items.Wood)
    return storedWood

def GetStoredCarrots():
    global storedCarrots
    storedCarrots = num_items(Items.Carrot)
    return storedCarrots
```

and the new main script will look like this;

```python
# Imports
import Utils
import ResourceUtils

#Local Variables
lm = 1
lc = 0
desiredHay = 2000
desiredWood = 2000
desiredCarrot = 2000


while True:
    ResourceUtils.GetAllStored()
    Utils.GetMaxTiles()
    beg = 0
    if beg == 0:
        Utils.HarvestAllTiles()
        beg += 1
    if ResourceUtils.storedHay < desiredHay:
        Utils.HayFarm(1)
        ResourceUtils.GetAllStored()
    elif ResourceUtils.storedWood < desiredWood:
        Utils.WoodFarm(1)
        ResourceUtils.GetAllStored()
    elif ResourceUtils.storedHay >= desiredHay and ResourceUtils.storedWood >= desiredWood:
        Utils.TillAllTiles()
    else:
        pass
    if ResourceUtils.storedCarrots < desiredCarrot:
        Utils.CarrotFarm(1)
        ResourceUtils.GetAllStored()
```

This will give us easy way of looping specific farms until we have a specific amount of resources, we could also alter the first while loop to just be true for even easier automation.

Now we are just saving up for these upgrades;

- Trees Level 3

- Carrots Level 2

- Water Level 1

- Grass Level 3

- Speed Level 4

- Lists 

- Fertilizer Level 1

- Water Level 2

- Pumpkins Level 1

### The Pumpkining

Now that we have pumpkins things get a little tricky, as they are a little different. They can be planted quite large, but if a pumpkin dies, it fails to make a mega-pumpkin. We could plant the entire map as Pumpkins which initally we will probably do.

To do that we just need to add some new functions to various scripts.

Lets start with the ResourceUtils script

```python
# Global Variables 
storedHay = 0
storedWood = 0
storedCarrots = 0
storedPumpkin = 0

storedWater = 0
storedFert = 0


# Get all Stored Reosurces:
def GetAllStored():
    GetStoredHay()
    GetStoredWood()
    GetStoredCarrots()
    GetStoredPumpkin()
    # Usable Items
    GetStoredWater()
    GetStoredFert()

# Get Items Fucntions
def GetStoredHay():
    global storedHay
    storedHay = num_items(Items.Hay)
    return storedHay

def GetStoredWood():
    global storedWood
    storedWood = num_items(Items.Wood)
    return storedWood

def GetStoredCarrots():
    global storedCarrots
    storedCarrots = num_items(Items.Carrot)
    return storedCarrots

def GetStoredPumpkin():
    global storedPumpkin
    storedPumpkin = num_items(Items.Pumpkin)
    return storedPumpkin

def GetStoredWater():
    global storedWater
    storedWater = num_items(Items.Water)
    return storedWater

def GetStoredFert():
    global storedFert
    storedFert = num_items(Items.Fertilizer)
    return storedFert
```

Then the Utils script will look like this;

```python
global tilesMax


def MoveDrone(tileAmount):
    mapSize = get_world_size() -1 # We subtract one because get_world_size() indexes at 1, not 0 like the drone
    for s in range(tileAmount):
        if get_pos_y() != mapSize:
            move(North)
        else:
            move(East)
            move(North)

def isTileEven(tile):
    return tile % 2 == 0

def GetMaxTiles():
    global tilesMax
    tilesMax = get_world_size() * get_world_size()

def HarvestAllTiles():
    global tilesMax
    for t in range(tilesMax):
        harvest()
        MoveDrone(1)
    clear()

def TillAllTiles():
    global tilesMax
    HarvestAllTiles()
    for t in range(tilesMax):
        if get_ground_type() != Grounds.Soil:
            till()
        MoveDrone(1)

# Farm Loops

def HayFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            harvest()
            MoveDrone(1)
        loopCount += 1

def BushFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Bush)
                MoveDrone(1)
            elif get_entity_type() != Entities.Bush:
                plant(Entities.Bush)
            else:
                MoveDrone(1)
        loopCount += 1

def CarrotFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Carrot)
                MoveDrone(1)
            elif get_entity_type() != Entities.Carrot:
                plant(Entities.Carrot)
                MoveDrone(1)
            else:
                MoveDrone(1)

def WoodFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            posX = get_pos_x()
            posY = get_pos_y()
            if isTileEven(posX) and isTileEven(posY):
                if can_harvest():
                    harvest()
                    plant(Entities.Tree)
                    MoveDrone(1)
                elif get_entity_type() != Entities.Tree:
                    plant(Entities.Tree)
                    MoveDrone(1)
                else:
                    MoveDrone(1)
            else:
                if can_harvest():
                    harvest()
                    plant(Entities.Bush)
                    MoveDrone(1)
                elif get_entity_type() != Entities.Bush:
                    plant(Entities.Bush)
                    MoveDrone(1)
                else:
                    MoveDrone(1)
        loopCount += 1

def PumpkinFarm(loopAmount):
    global tilesMax
    loopCount = 0
    while loopCount < loopAmount:
        for t in range(tilesMax):
            if can_harvest():
                harvest()
                plant(Entities.Pumpkin)
                MoveDrone(1)
            elif get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
                MoveDrone(1)
            else:
                MoveDrone(1)
        loopCount += 1
```

Then our main script will look like this;

```python
# Imports
import Utils
import ResourceUtils

#Local Variables
lm = 1
lc = 0
tilled = 1
desiredHay = 5000
desiredWood = 5000
desiredCarrot = 2000
desiredPumpkin = 2000




while True:
    ResourceUtils.GetAllStored()
    Utils.GetMaxTiles()
    if ResourceUtils.storedHay < desiredHay:
        Utils.HayFarm(1)
        ResourceUtils.GetAllStored()
    if ResourceUtils.storedWood < desiredWood:
        Utils.WoodFarm(1)
        ResourceUtils.GetAllStored()
    if ResourceUtils.storedHay >= desiredHay and ResourceUtils.storedWood >= desiredWood and tilled <= 0:
        Utils.TillAllTiles()
        tilled = 1
    if ResourceUtils.storedCarrots < desiredCarrot:
        Utils.CarrotFarm(1)
        ResourceUtils.GetAllStored()
    if ResourceUtils.storedPumpkin < desiredPumpkin:
        Utils.PumpkinFarm(1)
        ResourceUtils.GetAllStored()
```

You will notice some pumpkins are dying, this is unavoidable, and some pumpkins merge. Its a little RNG if we get the big boys or not, but this can be improved by improving the speed of our drone.

So now we will get the following upgrades when available;

- Speed Level 5

- Sunflowers

- Pumpkins Level 2

- Expand Level 5

- 

Then we will work on improving the scripts, as you notice there is some issues...



### More to Come...
