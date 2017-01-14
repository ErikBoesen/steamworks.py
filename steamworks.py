import math

def calculate_rotors(gears):
    return (4 if gears > 13 else round(math.sqrt(gears)))

def score():
    pass
