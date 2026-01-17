global tilesMax
lc = 0
lm = 5  # Max times the while loop goes.


def MoveDrone(tileAmount):
    mapSize = (
        get_world_size() - 1
    )  # We subtract one because get_world_size() indexes at 1, not 0 like the drone
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
    clear()  # Added so you can redo hay and doesn't break the loop
    lc += 1
