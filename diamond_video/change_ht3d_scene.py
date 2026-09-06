from manim import *

class ChangeHT3DScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        plane_scale = 1.4
        plane = NumberPlane([0, 1, 0.1], [0, 5.2, 0.2], plane_scale * 2, plane_scale * 5.2).add_coordinates(font_size=18).shift(UP * 0.1)
        x_label = plane.get_x_axis_label(r"\text{Height Value}").scale(0.5).next_to(plane.get_corner(DR), RIGHT)
        y_label = plane.get_y_axis_label(r"\text{Pixel Height}").scale(0.5).next_to(plane.get_edge_center(LEFT), LEFT)
        y_3x_graph = plane.plot(lambda x: 3*x, color=YELLOW)
        y_3x_power_graph = plane.plot(lambda x: (3*x) ** 1.5, color=PINK)
        y_3x_tex = MathTex("y=3x", color=YELLOW).scale(2).to_corner(UR)
        y_3x_power_tex = MathTex("y=(3x)^{1.5}", color=PINK).scale(2).to_corner(UL)

        self.play(Write(plane))
        self.play(Write(x_label))
        self.play(Write(y_label))
        self.wait(1)
        self.play(Write(y_3x_graph))
        self.play(Write(y_3x_tex))
        self.wait(3)
        self.play(Write(y_3x_power_graph))
        self.play(Write(y_3x_power_tex))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = ChangeHT3DScene()
    scene.render()
