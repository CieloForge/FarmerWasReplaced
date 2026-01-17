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
