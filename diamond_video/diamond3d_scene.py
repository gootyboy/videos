import random
from video_mobject import VideoMobject
import numpy as np
from manim import *
from diamond_square import default_biome_htc

class Diamond3DScene(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        # n = 5
        # roughness = 0.65
        # grid_width = 7.0
        
        # side_length = (2 ** n) + 1
        # cell_size = grid_width / side_length
        # start_x = -grid_width / 2 + cell_size / 2
        # start_y = grid_width / 2 - cell_size / 2

        # self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # def idx(r, c): 
        #     return r * side_length + c

        # height_matrix = np.zeros((side_length, side_length))
        # height_matrix[0, 0] = random.uniform(0.1, 0.9)
        # height_matrix[0, side_length-1] = random.uniform(0.1, 0.9)
        # height_matrix[side_length-1, 0] = random.uniform(0.1, 0.9)
        # height_matrix[side_length-1, side_length-1] = random.uniform(0.1, 0.9)
        
        # step = side_length - 1
        # s = roughness
        # while step > 1:
        #     half = step // 2
        #     for r in range(half, side_length, step):
        #         for c in range(half, side_length, step):
        #             avg = (height_matrix[r-half, c-half] + height_matrix[r-half, c+half] + height_matrix[r+half, c-half] + height_matrix[r+half, c+half]) / 4.0
        #             height_matrix[r, c] = np.clip(avg, 0.0, 1.0) + random.uniform(-s, s)
        #     for r in range(0, side_length, half):
        #         shift = half if (r % step == 0) else 0
        #         for c in range(shift, side_length, step):
        #             total = 0.0
        #             count = 0
        #             if r >= half: total += height_matrix[r-half, c]; count += 1
        #             if r + half < side_length: total += height_matrix[r+half, c]; count += 1
        #             if c >= half: total += height_matrix[r, c-half]; count += 1
        #             if c + half < side_length: total += height_matrix[r, c+half]; count += 1
        #             height_matrix[r, c] = np.clip((total / count), 0.0, 1.0) + random.uniform(-s, s)
        #     step = half
        #     s *= roughness

        # height_map = height_matrix.flatten()

        # grid = VGroup()
        # for r in range(side_length):
        #     for c in range(side_length):
        #         i = idx(r, c)
        #         pos_x = start_x + (c * cell_size)
        #         pos_y = start_y - (r * cell_size)

        #         cell = Prism(dimensions=[cell_size, cell_size, 0.01])
        #         cell.move_to([pos_x, pos_y, 0])
        #         cell.set_stroke(width=0.2, color=GRAY)
        #         cell.set_fill(opacity=0)
        #         grid.add(cell)

        # self.play(Create(grid, run_time=1.0))
        
        # base_corners = [idx(0, 0), idx(0, side_length-1), idx(side_length-1, 0), idx(side_length-1, side_length-1)]
        # self.play(AnimationGroup(
        #     *[grid[i].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[i])), opacity=1) for i in base_corners],
        #     run_time=0.4
        # ))

        # step_size = side_length - 1
        # while step_size > 1:
        #     half_step = step_size // 2
        #     diamond_reveals = []
        #     for r in range(half_step, side_length, step_size):
        #         for c in range(half_step, side_length, step_size):
        #             center = idx(r, c)
        #             diamond_reveals.append(grid[center].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[center])), opacity=1))
        #     if diamond_reveals:
        #         self.play(AnimationGroup(*diamond_reveals, run_time=0.4))

        #     square_reveals = []
        #     for r in range(0, side_length, half_step):
        #         col_start = half_step if (r % step_size == 0) else 0
        #         for c in range(col_start, side_length, step_size):
        #             midpoint = idx(r, c)
        #             square_reveals.append(grid[midpoint].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[midpoint])), opacity=1))
        #     if square_reveals:
        #         self.play(AnimationGroup(*square_reveals, run_time=0.4))
        #     step_size = half_step

        # self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=2.5)
        # self.wait(1)
        # self.begin_ambient_camera_rotation(0.05)
        # self.wait(3)

        # extrusion_animations = []
        # for r in range(side_length):
        #     for c in range(side_length):
        #         i = idx(r, c)
        #         val = height_map[i]
        #         if val <= 0:
        #             val = 0.01
        #         target_height = val

        #         pos_x = start_x + (c * cell_size)
        #         pos_y = start_y - (r * cell_size)
        #         target_z = target_height / 2.0
                
        #         extrusion_animations.append(
        #             grid[i].animate.stretch_to_fit_depth(target_height)
        #                            .move_to([pos_x, pos_y, target_z])
        #                            .set_stroke(width=0.05)
        #         )

        # self.play(AnimationGroup(*extrusion_animations, run_time=3))
        # self.wait(3)
        # self.stop_ambient_camera_rotation()
        # self.play(FadeOut(grid))

        # plane = NumberPlane(x_range=[0, 1, 0.1], y_range=[0, 1, 0.1], x_length=5, y_length=5)
        # self.add_fixed_in_frame_mobjects(plane)
        # self.remove(plane)
        # x_label = plane.get_x_axis_label(r"\text{Height Value}")
        # y_label = plane.get_y_axis_label(r"\text{Pixel Height}")
        # self.add_fixed_in_frame_mobjects(x_label, y_label)
        # self.remove(x_label, y_label)
        # self.play(Write(plane))
        # self.play(Write(x_label))
        # self.play(Write(y_label))
        # graph = Arrow(plane.c2p((0, 0)), plane.c2p((1, 1)), color=YELLOW)
        # self.add_fixed_in_frame_mobjects(graph)
        # self.remove(graph)
        # label = MathTex("y=x").move_to(graph.get_center()).shift(RIGHT * 0.75)
        # self.add_fixed_in_frame_mobjects(label)
        # self.remove(label)
        # self.play(Write(graph))
        # self.play(Write(label))
        # self.wait(3)
        # self.play(FadeOut(graph, plane, label, x_label, y_label))

        # self.play(FadeIn(grid))
        # self.begin_ambient_camera_rotation(0.05)
        # self.wait(3)
        # times_text = MathTex("h * 3").scale(2)
        # self.add_fixed_in_frame_mobjects(times_text)
        # self.remove(times_text)
        # times_text.to_corner(UR)
        # self.move_camera(zoom=0.8)
        # self.play(Write(times_text))
        # extrusion_animations = []
        # for r in range(side_length):
        #     for c in range(side_length):
        #         i = idx(r, c)
        #         val = height_map[i]
        #         if val <= 0:
        #             val = 0.01
        #         target_height = val * 3

        #         pos_x = start_x + (c * cell_size)
        #         pos_y = start_y - (r * cell_size)
        #         target_z = target_height / 2.0
                
        #         extrusion_animations.append(
        #             grid[i].animate.stretch_to_fit_depth(target_height)
        #                            .move_to([pos_x, pos_y, target_z])
        #                            .set_stroke(width=0.05)
        #         )

        # self.play(AnimationGroup(*extrusion_animations, run_time=2.5))
        # self.wait(20)
        # self.play(FadeOut(*self.mobjects))
        # self.wait(3)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": False}):
    scene = Diamond3DScene()
    scene.render()
