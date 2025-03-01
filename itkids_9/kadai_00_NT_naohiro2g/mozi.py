import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po

from lcd_font_mc import LCD_font as LCD_font_mc

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)

display2 = LCD_font_mc(mc)
display2.init_col(COLOR_ON=param.IRON_BLOCK, COLOR_OFF=param.AIR)
display2.init_row(X_ORG=-35, Y_ORG=param.Y_SEA + 71, Z_ORG=-20, COL_INTV=6)

#12=!,13=?,14=A,15=B,16=C,17=D,18=E,19=F,20=G,21=H,22=I,23=J,24=K,25=L,26=M,27=N,28=O,29=P,30=Q,31=R,32=S,33=T,34=U,35=V,36=W,37=X,38=Y,39=Z
display2.update_col(col=0, code=21)
display2.update_col(col=1, code=18)
display2.update_col(col=2, code=25)
display2.update_col(col=3, code=25)
display2.update_col(col=4, code=28)
display2.update_col(col=6, code=18)
display2.update_col(col=7, code=35)
display2.update_col(col=8, code=18)
display2.update_col(col=9, code=31)
display2.update_col(col=10, code=38)
display2.update_col(col=11, code=28)
display2.update_col(col=12, code=27)
display2.update_col(col=13, code=18)
display2.update_col(col=14, code=12)
