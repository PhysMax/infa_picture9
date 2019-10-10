from util import *

# Background
brushColor(sky_clr)
rectangle(0, 0, 500, 400)
brushColor('white')
rectangle(0, 400, 500, 600)

# Sun
penColor(sun_clr)
brushColor(sun_clr)
circle(350, 180, 150)

penColor(sky_clr)
brushColor(sky_clr)
circle(350, 180, 120)
penColor(sun_clr)
brushColor(sun_clr)
rectangle(335, 35, 365, 325)
rectangle(205, 165, 500, 195)

penColor('white')
brushColor('white')
circle(350, 180, 25)
circle(215, 180, 15)
circle(485, 180, 15)

penColor('black')
draw_bear(460, 350, -0.3, 0.3, 2)
draw_bear(300, 380, -0.4, 0.4, 2)
draw_bear(20, 440, 0.45, 0.45, 2)
draw_bear(520, 400, -0.8, 0.8, 2)

run()
