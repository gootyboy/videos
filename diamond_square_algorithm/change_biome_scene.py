from manim import *

class ChangeBiomeScene(Scene):
    def construct(self):
        self.camera.background_color = GRAY

        volcanic_color_map = {
            "(20, 20, 20)": "#141414",
            "(40, 40, 40)": "#282828",
            "(80, 0, 0)": "#500000",
            "(200, 50, 0)": "#C83200",
            "(255, 120, 50)": "#FF7832",
        }
        volcanic_htc_func = MathTex(
            r"""
            v(h) = \begin{cases}
            (20, 20, 20) & \text{if } h < 0.2 \\
            (40, 40, 40) & \text{if } 0.2 \le h < 0.3 \\
            (80, 0, 0) & \text{if } 0.3 \le h < 0.5 \\
            (200, 50, 0) & \text{if } 0.5 \le h < 0.8 \\
            (255, 120, 50) & \text{if } h \ge 0.8
            \end{cases}""",
            substrings_to_isolate=list(volcanic_color_map.keys())
        ).scale(1.5)

        for text_substring, hex_color in volcanic_color_map.items():
            volcanic_htc_func.set_color_by_tex(text_substring, hex_color)

        volcanic_image = ImageMobject("diamond_video/images/volcanic_image.png").scale(0.75)

        self.play(Write(volcanic_htc_func, run_time=10))
        self.wait(10)
        self.play(FadeOut(volcanic_htc_func))
        self.wait(3)
        self.play(FadeIn(volcanic_image))

        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = ChangeBiomeScene()
    scene.render()
