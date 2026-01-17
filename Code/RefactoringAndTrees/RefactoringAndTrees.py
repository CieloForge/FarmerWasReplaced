import Utils

lm = 1
lc = 0

while lc < lm:
    Utils.GetMaxTiles()
    Utils.HayFarm(5)
    Utils.WoodFarm(5)
    Utils.TillAllTiles()
    Utils.CarrotFarm(1)
    clear()
    lc += 1
