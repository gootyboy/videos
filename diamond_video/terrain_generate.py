from diamond_square import *

my_biome = Biome("My Biome", default_biome_htc, lambda h: (h * 10))

terrain3d = Terrain3D(size=2 ** 8 + 1, biome=DEFAULT_BIOME, roughness=0.65, scale=5, pos=(1, 1, 1))

class Panda3DTerrain3D(Panda3DBase):
    def __init__(self):
        super().__init__()

        terrain3d.draw_panda3d(obj=self)

app = Panda3DTerrain3D()

app.run()
