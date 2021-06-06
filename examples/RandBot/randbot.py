#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import random, sys
import interface

class RandBot(interface.Bot):
    """Bot que juega aleatoriamente."""
    NAME = "RandBot"

    def play(self, state):
        """Jugar: llamado cada turno.
        Debe devolver una acción (jugada)."""
        cx, cy = state["position"]
        lighthouses = dict((tuple(lh["position"]), lh)
                            for lh in state["lighthouses"])

        # Si estamos en un faro...
        if (cx, cy) in lighthouses:
            # Probabilidad 60%: conectar con faro remoto válido
            if lighthouses[(cx, cy)]["owner"] == self.player_num:
                if random.randrange(100) < 60:
                    possible_connections = []
                    for dest in lighthouses:
                        # No conectar con sigo mismo
                        # No conectar si no tenemos la clave
                        # No conectar si ya existe la conexión
                        # No conectar si no controlamos el destino
                        # Nota: no comprobamos si la conexión se cruza.
                        if (dest != (cx, cy) and
                            lighthouses[dest]["have_key"] and
                            [cx, cy] not in lighthouses[dest]["connections"] and
                            lighthouses[dest]["owner"] == self.player_num):
                            possible_connections.append(dest)

                    if possible_connections:
                        return self.connect(random.choice(possible_connections))

#        betterManhattan = 9999
#        for lh in (state["lighthouses"]):
#            xLH, yLH = lh["position"]
#            if lh["owner"] != self.player_num:
#                if betterManhattan != 0 and betterManhattan > max(abs(xLH-cx), abs(yLH-cy)):
#                    betterManhattan = max(abs(xLH-cx), abs(yLH-cy))
#                    targetLh = lh["position"]
#        xcoord, ycoord = targetLh["position"]
        lh = state["lighthouses"][1]
        xcoord, ycoord = lh["position"]
        if cx < xcoord:
            if cy < ycoord:
                #return upright
                move = [1,1]
            if cy > ycoord:
                #return downright
                move = [1,-1]
            if cy == ycoord:
                #return right
                move = [1,0]
        if cx > xcoord:
            if cy < target[1]:
                #return upleft
                move = [-1,1]
            if cy > ycoord:
                #return downleft
                move = [-1,-1]
            if cy == ycoord:
                #return left
                move = [-1,0]
        if cx == xcoord:
            if cy < ycoord:
                #return up
                move = [0,1]
            if cy > ycoord:
                #return down
                move = [0,-1]
        return self.move(*move)



if __name__ == "__main__":
    iface = interface.Interface(RandBot)
    iface.run()
