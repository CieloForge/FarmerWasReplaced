while True:
    if can_harvest():
        harvest()
        plant(Entities.Bush)  # This can be commented out if you just trying to get Hay.
        move(North)
    else:
        move(North)
