from enum import Enum

class Type(Enum):
    ALL_SEAONS = 0
    WINTER = 1 
    SUMMER = 2
    INVALID = 3

def classify_tire(traction_index, pressure, circonference):
    if pressure < 36.0: # In PSI
        return Type.INVALID

    if circonference < 26: # In Inch
        return Type.INVALID

    if traction_index >= 110 : 
        return Type.WINTER
    elif traction_index < 110 and traction_index > 90:
        return Type.ALL_SEAONS
    elif traction_index <= 90 and traction_index > 40:
        return Type.SUMMER
    else:
        return Type.INVALID
