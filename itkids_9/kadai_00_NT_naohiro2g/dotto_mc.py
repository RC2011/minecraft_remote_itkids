import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po


from lcd_font_mc import LCD_font as LCD_font_mc
from lcd_font_mc import LCD_font_styles

from datetime import datetime

import pygame
from seven_seg_pg import Seven_seg

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)


display2 = LCD_font_mc(mc)
display2.init_col(COLOR_ON=param.IRON_BLOCK, COLOR_OFF=param.AIR)
display2.init_row(X_ORG=-35, Y_ORG=param.Y_SEA + 61, Z_ORG=-20, COL_INTV=6)

display3 = LCD_font_mc(mc)
display3.init_col(COLOR_ON=param.IRON_BLOCK, COLOR_OFF=param.AIR)
display3.init_row(X_ORG=-35, Y_ORG=param.Y_SEA + 51, Z_ORG=-20, COL_INTV=6)

dt_now = datetime.now()
time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
display2.update_col(col=0, code=int(str(dt_now.year)[0]))
display2.update_col(col=1, code=int(str(dt_now.year)[1]))
display2.update_col(col=2, code=int(str(dt_now.year)[2]))
display2.update_col(col=3, code=int(str(dt_now.year)[3]))
display2.update_col(col=4, code=10)
display2.update_col(col=5, code=dt_now.month // 10)
display2.update_col(col=6, code=dt_now.month % 10)
display2.update_col(col=7, code=10)
display2.update_col(col=8, code=dt_now.day // 10)
display2.update_col(col=9, code=dt_now.day % 10)



display3.update_col(col=0, code=dt_now.hour // 10)
display3.update_col(col=1, code=dt_now.hour % 10)
display3.update_col(col=2, code=11)
display3.update_col(col=3, code=dt_now.minute // 10)
display3.update_col(col=4, code=dt_now.minute % 10)
display3.update_col(col=5, code=11)
display3.update_col(col=6, code=dt_now.second // 10)
display3.update_col(col=7, code=dt_now.second % 10)

mc.setBlock()
