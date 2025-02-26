import sys
from time import sleep

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po


# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)

mc.postToChat('kadai #3  seven columns')

x = -21
z = 9
for _n in range(7):
    y = param.Y_SEA + 1
    for _i in range(10):
        mc.setBlock(x, y, z,  param.IRON_BLOCK)
        sleep(0.25)
        y += 1
    x += 2
