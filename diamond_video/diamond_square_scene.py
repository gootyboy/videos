from manim import *
from diamond_animation import no_rough_diamond_animation

class DiamondSquareScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        no_rough_img = ImageMobject("diamond_video/images/no_roughness.png").scale(1.8)
        rough_img = ImageMobject("diamond_video/images/default_image.png").scale(0.75).shift(LEFT * 3.5)

        self.play(no_rough_diamond_animation(2))
        self.wait(3)
        self.play(no_rough_diamond_animation(8))
        self.wait(3)
        self.clear()
        self.add(no_rough_img)
        self.play(no_rough_img.animate.shift(RIGHT * 3.5), FadeIn(rough_img))
        self.wait(5)
        self.play(no_rough_img.animate.shift(LEFT * 3.5), FadeOut(rough_img))
        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": False}):
    scene = DiamondSquareScene()
    scene.render()
