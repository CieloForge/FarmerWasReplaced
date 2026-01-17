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
