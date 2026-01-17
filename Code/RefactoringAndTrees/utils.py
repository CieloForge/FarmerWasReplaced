global tilesMax


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
