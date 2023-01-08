import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thorX = initial_tx
thorY = initial_ty
#OPPURE
#thorX, thorY = initial_tx, initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direzione_x=""
    direzione_y=""
    if thorY > light_y:
        direzione_y += "N"
        thorY -= 1
    elif thorY < light_y:
        direzione_y += "S"
        thorY += 1

    if thorX > light_x:
        direzione_x = "W"
        thorX -= 1
    elif thorX < light_x:
        direzione_x = "E"
        thorX += 1


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direzione_y + direzione_x)
    
