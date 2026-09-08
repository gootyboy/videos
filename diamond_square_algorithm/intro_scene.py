from manim import *
from helper_funcs import *
from video_mobject import VideoMobject

def run_scene(scene, low_q = True):
    if low_q:
        temp_config = {"preview": True, "quality": "low_quality", "disable-caching": False}
    else:
        temp_config = {"preview": True, "quality": "fourk_quality", "disable-caching": True}

    with tempconfig(temp_config):
        scene.render()

class IntroScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        default3d_video = VideoMobject(r"diamond_video/videos/default3d.mov", 1)
        default3d_video_start = ImageMobject("diamond_video/images/default3d_start.png")
        default3d_image = ImageMobject("diamond_video/images/default3d_end.png")
        default3d_image_copy = default3d_image.copy()
        question_mark = Text("?", color=RED).scale(15)
        default3d_image_dark = darken_image(default3d_image)
        default_image = ImageMobject("diamond_video/images/default_image.png")
        default_image_dark = darken_image(default_image)
        diamond_square = Paragraph("Diamond-Square", "Algorithm", t2c={"Diamond": YELLOW, "Square": RED, "Algorithm": BLUE}, alignment="center").scale(2)

        self.wait(5)
        self.play(FadeIn(default3d_video_start))
        self.add(default3d_video)
        self.remove(default3d_video_start)
        self.wait(60)
        self.remove(default3d_video)
        self.add(default3d_image)
        self.play(Write(question_mark), ReplacementTransform(default3d_image, default3d_image_dark))
        self.wait(5)
        self.play(FadeOut(question_mark), ReplacementTransform(default3d_image_dark, default3d_image_copy))
        self.wait(5)
        self.play(FadeOut(default3d_image_copy), FadeIn(default_image))
        self.wait(5)
        self.play(Write(diamond_square), ReplacementTransform(default_image, default_image_dark))
        self.wait(5)
        self.play(FadeOut(diamond_square, default_image_dark))

        random_colors = ImageMobject("diamond_video/images/random_colors.png")
        color_func = MathTex(r"f(x, y) = (r, g, b)", substrings_to_isolate=["x", "y", "r", "g", "b"]).scale(2)
        color_func.set_color_by_tex("x", YELLOW)
        color_func.set_color_by_tex("y", PINK)
        color_func.set_color_by_tex("r", RED)
        color_func.set_color_by_tex("g", GREEN)
        color_func.set_color_by_tex("b", BLUE)
        color_func_x = Cross(color_func)
        height_func = MathTex(r"f(x, y) = h", substrings_to_isolate=["x", "y", "h"]).scale(2.5)
        height_func.set_color_by_tex("x", YELLOW)
        height_func.set_color_by_tex("y", PINK)
        height_func.set_color_by_tex("h", GREEN)
        color_map = {
            "(0, 0, 108)":"#00006C",
            "(0, 50, 170)":"#0032AA",
            "(194, 178, 128)":"#C2B280",
            "(34, 139, 34)":"#228B22",
            "(0, 100, 0)":"#006400",
            "(120, 110, 100)":"#786E64",
            "(160, 160, 160)":"#A0A0A0",
            "(255, 255, 255)":"#FFFFFF",
        }
        htc_func = MathTex(
            r""" g(h) = \begin{cases} 
            (0, 0, 108) & \text{if } h < 0.2 \\ 
            (0, 50, 170) & \text{if } 0.2 \le h < 0.3 \\ 
            (194, 178, 128) & \text{if } 0.3 \le h < 0.35 \\ 
            (34, 139, 34) & \text{if } 0.35 \le h < 0.5 \\ 
            (0, 100, 0) & \text{if } 0.5 \le h < 0.6 \\ 
            (120, 110, 100) & \text{if } 0.6 \le h < 0.75 \\ 
            (160, 160, 160) & \text{if } 0.75 \le h < 0.9 \\ 
            (255, 255, 255) & \text{if } h \ge 0.9 
            \end{cases}""",
            substrings_to_isolate=list(color_map.keys())
        ).shift(LEFT)

        for text_substring, hex_color in color_map.items():
            htc_func.set_color_by_tex(text_substring, hex_color)

        self.play(FadeIn(random_colors))
        self.wait(3)
        self.play(FadeOut(random_colors))
        self.wait(3)
        self.play(Write(color_func))
        self.wait(3)
        self.play(Write(color_func_x))
        self.wait(3)
        self.play(FadeOut(color_func, color_func_x))
        self.wait(3)
        self.play(Write(height_func))
        self.wait(3)
        self.play(height_func.animate.scale(0.7).shift(UP * 3, RIGHT * 4.75), AnimationGroup(Wait(1), Write(htc_func, run_time=10)))
        self.wait(10)
        self.play(FadeOut(height_func, htc_func))

with tempconfig({"preview": True, "quality": "fourk_quality", "disable-caching": True}):
    scene = IntroScene()
    scene.render()
