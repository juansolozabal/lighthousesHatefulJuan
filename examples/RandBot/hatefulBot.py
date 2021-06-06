#!/usr/bin/python
# -*- coding: utf-8 -*-

import random, sys
import interface

def chooseLighthouse(self, lighthouses, cx, cy):
    betterManhattan = 9999
    targetLh = lighthouses[0]
    for lh in lighthouses:
        xLh, yLh = lh["position"]
        if lh["owner"] != self.player_num:
            if betterManhattan != 0 and betterManhattan > max(abs(xLh-cx), abs(yLh-cy)):
                betterManhattan = max(abs(xLh-cx), abs(yLh-cy))
                targetLh = lh
    return targetLh["position"]

def aStar(start, goal, grid):
    return [[1,0]]

def isAStarpossible(lighthouses, cx, cy):
    for lh in lighthouses:
        if(max(abs(lh["position"][0]-cx), abs(lh["position"][1]-cy)<=3)):
            return true
    return false

 def getCloserToLighthouse(xLh, yLh, cx, cy):
    if cx < xLh:
        if cy < yLh:
            #return upright
            return [1,1]
        if cy > yLh:
            #return downright
            return [1,-1]
        if cy == yLh:
            #return right
            return [1,0]
    if cx > xLh:
        if cy < yLh:
            #return upleft
            return [-1,1]
        if cy > yLh:
            #return downleft
            return [-1,-1]
        if cy == yLh:
            #return left
            return [-1,0]
    if cx == xLh:
        if cy < yLh:
            #return up
            return [0,1]
        if cy > yLh:
            #return down
            return [0,-1]

class HatefulBot(interface.Bot):
    """Bot de los hateful four."""
    NAME = "HatefulBot"

    def play(self, state):
        """Jugar: llamado cada turno.
        Debe devolver una acción (jugada)."""
        cx, cy = state["position"]
        lighthouses = dict((tuple(lh["position"]), lh)
                            for lh in state["lighthouses"])
            allLh = []
        for lh in state["lighthouses"]:
            allLh.append(lh)

        # Si estamos en un faro...
        if (cx, cy) in lighthouses:
            # Si podemos hacer conexion, conectar con faro remoto válido
            if lighthouses[(cx, cy)]["owner"] == self.player_num:
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

        allLh = []
        move = [0,0]
        for lh in state["lighthouses"]:
            allLh.append(lh)

        xLh, yLh = chooseLighthouse(self, allLh, cx, cy)
        move = getCloserToLighthouse(xLh, yLh, cx, cy)   

        return self.move(*move)


if __name__ == "__main__":
    iface = interface.Interface(HatefulBot)
    iface.run()