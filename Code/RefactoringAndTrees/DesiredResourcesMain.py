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
