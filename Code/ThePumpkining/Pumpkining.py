# Imports
import ResourceUtils
import Utils

# Local Variables
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
    if (
        ResourceUtils.storedHay >= desiredHay
        and ResourceUtils.storedWood >= desiredWood
        and tilled <= 0
    ):
        Utils.TillAllTiles()
        tilled = 1
    if ResourceUtils.storedCarrots < desiredCarrot:
        Utils.CarrotFarm(1)
        ResourceUtils.GetAllStored()
    if ResourceUtils.storedPumpkin < desiredPumpkin:
        Utils.PumpkinFarm(1)
        ResourceUtils.GetAllStored()
