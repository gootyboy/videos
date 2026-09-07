from diamond_animation import *
from grow_shrink import GrowShrink
from manim import *
from diamond_square import default_biome_htc
from helper_funcs import *

class SizeScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        grid = VGroup(*[Square(side_length=1.425) for i in range(25)])
        grid.arrange_in_grid(rows=5, cols=5, buff=0)
        grid.set_stroke(color=WHITE, width=2)
        grid.set_fill(opacity=0)
        grid2 = VGroup(*[Square(side_length=1.14) for i in range(16)])
        grid2.arrange_in_grid(rows=4, cols=4, buff=0)
        grid2.set_stroke(color=WHITE, width=2)
        grid2.set_fill(opacity=0)
        height_map = [0.17, 0.51, 0.61, 0.0, 0.12]
        hmap_mobjects = VGroup()
        hmap_mobjects.add(MathTex(f"{height_map[0]}", color=get_matching_color(default_biome_htc(height_map[0])), z_index=100).move_to(grid[0]))
        hmap_mobjects.add(MathTex(f"{height_map[1]}", color=get_matching_color(default_biome_htc(height_map[1])), z_index=100).move_to(grid[4]))
        hmap_mobjects.add(MathTex(f"{height_map[2]}", color=get_matching_color(default_biome_htc(height_map[2])), z_index=100).move_to(grid[20]))
        hmap_mobjects.add(MathTex(f"{height_map[3]}", color=get_matching_color(default_biome_htc(height_map[3])), z_index=100).move_to(grid[24]))
        hmap_mobjects.add(MathTex(f"{height_map[4]}", color=get_matching_color(default_biome_htc(height_map[4])), z_index=100).move_to(grid[12]))
        height_map2 = [0.17, 0.51, 0.61, 0.0]
        hmap_mobjects2 = VGroup()
        hmap_mobjects2.add(MathTex(f"{height_map2[0]}", color=get_matching_color(default_biome_htc(height_map2[0])), z_index=100).move_to(grid2[0]))
        hmap_mobjects2.add(MathTex(f"{height_map2[1]}", color=get_matching_color(default_biome_htc(height_map2[1])), z_index=100).move_to(grid2[3]))
        hmap_mobjects2.add(MathTex(f"{height_map2[2]}", color=get_matching_color(default_biome_htc(height_map2[2])), z_index=100).move_to(grid2[12]))
        hmap_mobjects2.add(MathTex(f"{height_map2[3]}", color=get_matching_color(default_biome_htc(height_map2[3])), z_index=100).move_to(grid2[15]))

        self.play(Write(grid))
        self.play(Write(hmap_mobjects[0]), grid[0].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[0])), opacity=1))
        self.play(Write(hmap_mobjects[1]), grid[4].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[1])), opacity=1))
        self.play(Write(hmap_mobjects[2]), grid[20].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[2])), opacity=1))
        self.play(Write(hmap_mobjects[3]), grid[24].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[3])), opacity=1))
        self.play(Write(hmap_mobjects[4]), grid[12].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[4])), opacity=1))
        self.wait(3)
        self.play(FadeOut(grid, hmap_mobjects), FadeIn(grid2))
        self.play(Write(hmap_mobjects2[0]), grid2[0].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map2[0])), opacity=1))
        self.play(Write(hmap_mobjects2[1]), grid2[3].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map2[1])), opacity=1))
        self.play(Write(hmap_mobjects2[2]), grid2[12].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map2[2])), opacity=1))
        self.play(Write(hmap_mobjects2[3]), grid2[15].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map2[3])), opacity=1))
        self.wait(3)
        self.play(GrowShrink(grid2[5], grid2[6], grid2[9], grid2[10]))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.wait(1)

        seven_size_img = ImageMobject("diamond_video/images/seven_size_image.png").scale_to_fit_height(config.frame_height)
        base_box = Square(seven_size_img.height / 7 * 4, stroke_width=5)
        tl_box = base_box.copy().move_to(seven_size_img.get_corner(UL)).shift(RIGHT * (seven_size_img.height / 7 * 2), DOWN * (seven_size_img.height / 7 * 2))
        tr_box = base_box.copy().move_to(seven_size_img.get_corner(UR)).shift(LEFT * (seven_size_img.height / 7 * 2), DOWN * (seven_size_img.height / 7 * 2))
        bl_box = base_box.copy().move_to(seven_size_img.get_corner(DL)).shift(RIGHT * (seven_size_img.height / 7 * 2), UP * (seven_size_img.height / 7 * 2))
        br_box = base_box.copy().move_to(seven_size_img.get_corner(DR)).shift(LEFT * (seven_size_img.height / 7 * 2), UP * (seven_size_img.height / 7 * 2))

        self.add(seven_size_img)
        self.wait(1)
        self.play(GrowShrink(tl_box))
        self.play(FadeOut(tl_box), run_time=0.5)
        self.play(GrowShrink(tr_box))
        self.play(FadeOut(tr_box), run_time=0.5)
        self.play(GrowShrink(bl_box))
        self.play(FadeOut(bl_box), run_time=0.5)
        self.play(GrowShrink(br_box))
        self.play(FadeOut(br_box), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

        tex = MathTex("s = 2^n+1").scale(4).shift(UP)
        tex2 = Tex("$s:$ \"size\"").scale(2).next_to(tex, DOWN)
        self.play(Write(tex))
        self.play(Write(tex2))

        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = SizeScene()
    scene.render()
