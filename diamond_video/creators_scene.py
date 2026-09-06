from manim import *

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

        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = CreatorsScene()
    scene.render()
