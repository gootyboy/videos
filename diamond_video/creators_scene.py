from manim import *
from helper_funcs import *
from video_mobject import VideoMobject

class CreatorsScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        text3 = Text("Loren Carpenter", font_size=144)
        text2 = Text("Alain Fournier", font_size=144)
        text1 = Text("Don Fussell", font_size=144)

        self.play(Write(text1))
        self.wait(1)
        self.play(text1.animate.shift(UP * 2.5))
        self.play(Write(text2))
        self.wait(1)
        self.play(text2.animate.shift(DOWN * 2.5))
        self.play(Write(text3))
        self.wait(3)
        self.play(FadeOut(text1, text2, text3))
        self.wait(3)

        github_text = Text(r"github.com/gootyboy/videos/diamond_video")
        thanks_text = Paragraph("Thanks for", "watching!", alignment="center").scale_to_fit_width(config.frame_width).scale(0.75)

        self.play(Write(github_text))
        self.wait(3)
        self.play(FadeOut(github_text))
        self.play(Write(thanks_text))
        self.wait(3)
        self.play(FadeOut(thanks_text))
        self.wait(3)

        diamond_square = Text("diamond-square").scale(2.5)
        link = Text(r"pypi.org/project/diamond-square/").next_to(diamond_square, DOWN)
        pip = Text("pip install diamond-square").next_to(link, DOWN)
        code = get_code(r"""from diamond_square import *

Panda3DInteractive().run()""").scale(1.75)
        video = VideoMobject("diamond_video/videos/interactive3d.mov")

        self.play(Write(diamond_square))
        self.wait(2)
        self.play(Write(link))
        self.wait(2)
        self.play(Write(pip))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.play(Create(code), run_time=5)
        self.wait(3)
        self.play(FadeOut(code))
        self.play(FadeIn(video))
        self.wait(90)

        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = CreatorsScene()
    scene.render()
