import random
import numpy as np
from manim import *
from helper_funcs import *
from diamond_square import default_biome_htc
import random
import numpy as np
from manim import *

def no_rough_diamond_animation(n=2, grid_width=7.0):
    side_length = (2 ** n) + 1
    cell_size = grid_width / side_length
    start_x = -grid_width / 2 + cell_size / 2
    start_y = grid_width / 2 - cell_size / 2

    def idx(r, c):
        return r * side_length + c

    height_matrix = np.zeros((side_length, side_length))
    height_matrix[0, 0] = random.uniform(0.1, 0.9)
    height_matrix[0, side_length-1] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, 0] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, side_length-1] = random.uniform(0.1, 0.9)

    step = side_length - 1
    while step > 1:
        half = step // 2
        for r in range(half, side_length, step):
            for c in range(half, side_length, step):
                avg = (height_matrix[r-half, c-half] + height_matrix[r-half, c+half] + height_matrix[r+half, c-half] + height_matrix[r+half, c+half]) / 4.0
                height_matrix[r, c] = np.clip(avg, 0.0, 1.0)
        for r in range(0, side_length, half):
            shift = half if (r % step == 0) else 0
            for c in range(shift, side_length, step):
                total = 0.0
                count = 0
                if r >= half: total += height_matrix[r-half, c]; count += 1
                if r + half < side_length: total += height_matrix[r+half, c]; count += 1
                if c >= half: total += height_matrix[r, c-half]; count += 1
                if c + half < side_length: total += height_matrix[r, c+half]; count += 1
                height_matrix[r, c] = np.clip((total / count), 0.0, 1.0)

        step = half

    height_map = height_matrix.flatten()
    grid = []
    for r in range(side_length):
        for c in range(side_length):
            i = idx(r, c)
            val = height_map[i]
            pos_x = start_x + (c * cell_size)
            pos_y = start_y - (r * cell_size)
            cell = Square(side_length=cell_size)
            cell.move_to([pos_x, pos_y, 0])
            cell.set_stroke(width=0.2, color=GRAY)
            cell.set_fill(opacity=0)
            grid.append(cell)

    animations = []

    animations.append(Create(VGroup(*grid), run_time=1.0))

    base_corners = [idx(0, 0), idx(0, side_length-1), idx(side_length-1, 0), idx(side_length-1, side_length-1)]
    animations.append(AnimationGroup(
        *[grid[i].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[i])), opacity=1) for i in base_corners],
        run_time=0.4
    ))

    step_size = side_length - 1
    while step_size > 1:
        half_step = step_size // 2
        diamond_flashes = []
        diamond_reveals = []
        for r in range(half_step, side_length, step_size):
            for c in range(half_step, side_length, step_size):
                center = idx(r, c)
                p1, p2 = idx(r - half_step, c - half_step), idx(r - half_step, c + half_step)
                p3, p4 = idx(r + half_step, c - half_step), idx(r + half_step, c + half_step)
                diamond_flashes.extend([grid[p1], grid[p2], grid[p3], grid[p4]])
                diamond_reveals.append(grid[center].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[center])), opacity=1))
        
        if diamond_reveals:
            animations.append(AnimationGroup(*diamond_reveals, run_time=0.4))

        square_flashes = []
        square_reveals = []
        for r in range(0, side_length, half_step):
            col_start = half_step if (r % step_size == 0) else 0
            for c in range(col_start, side_length, step_size):
                midpoint = idx(r, c)
                if r >= half_step: square_flashes.append(grid[idx(r - half_step, c)])
                if r + half_step < side_length: square_flashes.append(grid[idx(r + half_step, c)])
                if c >= half_step: square_flashes.append(grid[idx(r, c - half_step)])
                if c + half_step < side_length: square_flashes.append(grid[idx(r, c + half_step)])
                square_reveals.append(grid[midpoint].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[midpoint])), opacity=1))
        
        if square_reveals:
            animations.append(AnimationGroup(*square_reveals, run_time=0.4))

        step_size = half_step

    animations.append(Wait(5))
    bg_square = Square(25, color=DARKER_GRAY)
    animations.append(FadeIn(bg_square))

    return Succession(*animations)

def fake_diamond_animation(n=2, roughness=0.5, grid_width=7.0):
    side_length = (2 ** n) + 1
    cell_size = grid_width / side_length
    start_x = -grid_width / 2 + cell_size / 2
    start_y = grid_width / 2 - cell_size / 2

    def idx(r, c):
        return r * side_length + c

    height_matrix = np.zeros((side_length, side_length))
    height_matrix[0, 0] = random.uniform(0.1, 0.9)
    height_matrix[0, side_length-1] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, 0] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, side_length-1] = random.uniform(0.1, 0.9)

    step = side_length - 1
    while step > 1:
        half = step // 2
        for r in range(half, side_length, step):
            for c in range(half, side_length, step):
                avg = (height_matrix[r-half, c-half] + height_matrix[r-half, c+half] + height_matrix[r+half, c-half] + height_matrix[r+half, c+half]) / 4.0
                height_matrix[r, c] = np.clip(avg, 0.0, 1.0) + random.uniform(0, roughness)
        for r in range(0, side_length, half):
            shift = half if (r % step == 0) else 0
            for c in range(shift, side_length, step):
                total = 0.0
                count = 0
                if r >= half: total += height_matrix[r-half, c]; count += 1
                if r + half < side_length: total += height_matrix[r+half, c]; count += 1
                if c >= half: total += height_matrix[r, c-half]; count += 1
                if c + half < side_length: total += height_matrix[r, c+half]; count += 1
                height_matrix[r, c] = np.clip((total / count), 0.0, 1.0) + random.uniform(0, roughness)

        step = half

    height_map = height_matrix.flatten()
    grid = []
    for r in range(side_length):
        for c in range(side_length):
            i = idx(r, c)
            val = height_map[i]
            pos_x = start_x + (c * cell_size)
            pos_y = start_y - (r * cell_size)
            cell = Square(side_length=cell_size)
            cell.move_to([pos_x, pos_y, 0])
            cell.set_stroke(width=0.2, color=GRAY)
            cell.set_fill(opacity=0)
            grid.append(cell)

    animations = []

    animations.append(Create(VGroup(*grid), run_time=1.0))

    base_corners = [idx(0, 0), idx(0, side_length-1), idx(side_length-1, 0), idx(side_length-1, side_length-1)]
    animations.append(AnimationGroup(
        *[grid[i].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[i])), opacity=1) for i in base_corners],
        run_time=0.4
    ))

    step_size = side_length - 1
    while step_size > 1:
        half_step = step_size // 2
        diamond_flashes = []
        diamond_reveals = []
        for r in range(half_step, side_length, step_size):
            for c in range(half_step, side_length, step_size):
                center = idx(r, c)
                p1, p2 = idx(r - half_step, c - half_step), idx(r - half_step, c + half_step)
                p3, p4 = idx(r + half_step, c - half_step), idx(r + half_step, c + half_step)
                diamond_flashes.extend([grid[p1], grid[p2], grid[p3], grid[p4]])
                diamond_reveals.append(grid[center].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[center])), opacity=1))
        
        if diamond_reveals:
            animations.append(AnimationGroup(*diamond_reveals, run_time=0.4))

        square_flashes = []
        square_reveals = []
        for r in range(0, side_length, half_step):
            col_start = half_step if (r % step_size == 0) else 0
            for c in range(col_start, side_length, step_size):
                midpoint = idx(r, c)
                if r >= half_step: square_flashes.append(grid[idx(r - half_step, c)])
                if r + half_step < side_length: square_flashes.append(grid[idx(r + half_step, c)])
                if c >= half_step: square_flashes.append(grid[idx(r, c - half_step)])
                if c + half_step < side_length: square_flashes.append(grid[idx(r, c + half_step)])
                square_reveals.append(grid[midpoint].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[midpoint])), opacity=1))
        
        if square_reveals:
            animations.append(AnimationGroup(*square_reveals, run_time=0.4))

        step_size = half_step

    animations.append(Wait(5))
    bg_square = Square(25, color=DARKER_GRAY)
    animations.append(FadeIn(bg_square))

    return Succession(*animations)

def fake_diamond_animation2(n=2, roughness=0.5, grid_width=7.0):
    side_length = (2 ** n) + 1
    cell_size = grid_width / side_length
    start_x = -grid_width / 2 + cell_size / 2
    start_y = grid_width / 2 - cell_size / 2

    def idx(r, c):
        return r * side_length + c

    height_matrix = np.zeros((side_length, side_length))
    height_matrix[0, 0] = random.uniform(0.1, 0.9)
    height_matrix[0, side_length-1] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, 0] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, side_length-1] = random.uniform(0.1, 0.9)

    step = side_length - 1
    while step > 1:
        half = step // 2
        for r in range(half, side_length, step):
            for c in range(half, side_length, step):
                avg = (height_matrix[r-half, c-half] + height_matrix[r-half, c+half] + height_matrix[r+half, c-half] + height_matrix[r+half, c+half]) / 4.0
                height_matrix[r, c] = np.clip(avg, 0.0, 1.0) + random.uniform(-roughness, roughness)
        for r in range(0, side_length, half):
            shift = half if (r % step == 0) else 0
            for c in range(shift, side_length, step):
                total = 0.0
                count = 0
                if r >= half: total += height_matrix[r-half, c]; count += 1
                if r + half < side_length: total += height_matrix[r+half, c]; count += 1
                if c >= half: total += height_matrix[r, c-half]; count += 1
                if c + half < side_length: total += height_matrix[r, c+half]; count += 1
                height_matrix[r, c] = np.clip((total / count), 0.0, 1.0) + random.uniform(-roughness, roughness)

        step = half

    height_map = height_matrix.flatten()
    grid = []
    for r in range(side_length):
        for c in range(side_length):
            i = idx(r, c)
            val = height_map[i]
            pos_x = start_x + (c * cell_size)
            pos_y = start_y - (r * cell_size)
            cell = Square(side_length=cell_size)
            cell.move_to([pos_x, pos_y, 0])
            cell.set_stroke(width=0.2, color=GRAY)
            cell.set_fill(opacity=0)
            grid.append(cell)

    animations = []

    animations.append(Create(VGroup(*grid), run_time=1.0))

    base_corners = [idx(0, 0), idx(0, side_length-1), idx(side_length-1, 0), idx(side_length-1, side_length-1)]
    animations.append(AnimationGroup(
        *[grid[i].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[i])), opacity=1) for i in base_corners],
        run_time=0.4
    ))

    step_size = side_length - 1
    while step_size > 1:
        half_step = step_size // 2
        diamond_flashes = []
        diamond_reveals = []
        for r in range(half_step, side_length, step_size):
            for c in range(half_step, side_length, step_size):
                center = idx(r, c)
                p1, p2 = idx(r - half_step, c - half_step), idx(r - half_step, c + half_step)
                p3, p4 = idx(r + half_step, c - half_step), idx(r + half_step, c + half_step)
                diamond_flashes.extend([grid[p1], grid[p2], grid[p3], grid[p4]])
                diamond_reveals.append(grid[center].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[center])), opacity=1))
        
        if diamond_reveals:
            animations.append(AnimationGroup(*diamond_reveals, run_time=0.4))

        square_flashes = []
        square_reveals = []
        for r in range(0, side_length, half_step):
            col_start = half_step if (r % step_size == 0) else 0
            for c in range(col_start, side_length, step_size):
                midpoint = idx(r, c)
                if r >= half_step: square_flashes.append(grid[idx(r - half_step, c)])
                if r + half_step < side_length: square_flashes.append(grid[idx(r + half_step, c)])
                if c >= half_step: square_flashes.append(grid[idx(r, c - half_step)])
                if c + half_step < side_length: square_flashes.append(grid[idx(r, c + half_step)])
                square_reveals.append(grid[midpoint].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[midpoint])), opacity=1))
        
        if square_reveals:
            animations.append(AnimationGroup(*square_reveals, run_time=0.4))

        step_size = half_step

    animations.append(Wait(5))
    bg_square = Square(25, color=DARKER_GRAY)
    animations.append(FadeIn(bg_square))

    return Succession(*animations)

def diamond_animation(n=2, roughness=0.5, grid_width=7.0):
    side_length = (2 ** n) + 1
    cell_size = grid_width / side_length
    start_x = -grid_width / 2 + cell_size / 2
    start_y = grid_width / 2 - cell_size / 2

    def idx(r, c):
        return r * side_length + c

    height_matrix = np.zeros((side_length, side_length))
    height_matrix[0, 0] = random.uniform(0.1, 0.9)
    height_matrix[0, side_length-1] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, 0] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, side_length-1] = random.uniform(0.1, 0.9)

    step = side_length - 1
    s = roughness
    while step > 1:
        half = step // 2
        for r in range(half, side_length, step):
            for c in range(half, side_length, step):
                avg = (height_matrix[r-half, c-half] + height_matrix[r-half, c+half] + height_matrix[r+half, c-half] + height_matrix[r+half, c+half]) / 4.0
                height_matrix[r, c] = np.clip(avg, 0.0, 1.0) + random.uniform(-s, s)
        for r in range(0, side_length, half):
            shift = half if (r % step == 0) else 0
            for c in range(shift, side_length, step):
                total = 0.0
                count = 0
                if r >= half: total += height_matrix[r-half, c]; count += 1
                if r + half < side_length: total += height_matrix[r+half, c]; count += 1
                if c >= half: total += height_matrix[r, c-half]; count += 1
                if c + half < side_length: total += height_matrix[r, c+half]; count += 1
                height_matrix[r, c] = np.clip((total / count), 0.0, 1.0) + random.uniform(-s, s)

        step = half
        s *= roughness

    height_map = height_matrix.flatten()
    grid = []
    for r in range(side_length):
        for c in range(side_length):
            i = idx(r, c)
            val = height_map[i]
            pos_x = start_x + (c * cell_size)
            pos_y = start_y - (r * cell_size)
            cell = Square(side_length=cell_size)
            cell.move_to([pos_x, pos_y, 0])
            cell.set_stroke(width=0.2, color=GRAY)
            cell.set_fill(opacity=0)
            grid.append(cell)

    animations = []

    animations.append(Create(VGroup(*grid), run_time=1.0))

    base_corners = [idx(0, 0), idx(0, side_length-1), idx(side_length-1, 0), idx(side_length-1, side_length-1)]
    animations.append(AnimationGroup(
        *[grid[i].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[i])), opacity=1) for i in base_corners],
        run_time=0.4
    ))

    step_size = side_length - 1
    while step_size > 1:
        half_step = step_size // 2
        diamond_flashes = []
        diamond_reveals = []
        for r in range(half_step, side_length, step_size):
            for c in range(half_step, side_length, step_size):
                center = idx(r, c)
                p1, p2 = idx(r - half_step, c - half_step), idx(r - half_step, c + half_step)
                p3, p4 = idx(r + half_step, c - half_step), idx(r + half_step, c + half_step)
                diamond_flashes.extend([grid[p1], grid[p2], grid[p3], grid[p4]])
                diamond_reveals.append(grid[center].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[center])), opacity=1))
        
        if diamond_reveals:
            animations.append(AnimationGroup(*diamond_reveals, run_time=0.4))

        square_flashes = []
        square_reveals = []
        for r in range(0, side_length, half_step):
            col_start = half_step if (r % step_size == 0) else 0
            for c in range(col_start, side_length, step_size):
                midpoint = idx(r, c)
                if r >= half_step: square_flashes.append(grid[idx(r - half_step, c)])
                if r + half_step < side_length: square_flashes.append(grid[idx(r + half_step, c)])
                if c >= half_step: square_flashes.append(grid[idx(r, c - half_step)])
                if c + half_step < side_length: square_flashes.append(grid[idx(r, c + half_step)])
                square_reveals.append(grid[midpoint].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[midpoint])), opacity=1))
        
        if square_reveals:
            animations.append(AnimationGroup(*square_reveals, run_time=0.4))

        step_size = half_step

    animations.append(Wait(5))
    bg_square = Square(25, color=DARKER_GRAY)
    animations.append(FadeIn(bg_square))

    return Succession(*animations)

def diamond_animation2(size=5, roughness=0.5, grid_width=7.0):
    side_length = size
    cell_size = grid_width / side_length
    start_x = -grid_width / 2 + cell_size / 2
    start_y = grid_width / 2 - cell_size / 2

    def idx(r, c):
        return r * side_length + c

    height_matrix = np.zeros((side_length, side_length))
    height_matrix[0, 0] = random.uniform(0.1, 0.9)
    height_matrix[0, side_length-1] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, 0] = random.uniform(0.1, 0.9)
    height_matrix[side_length-1, side_length-1] = random.uniform(0.1, 0.9)

    step = side_length - 1
    s = roughness
    while step > 1:
        half = step // 2
        for r in range(half, side_length, step):
            for c in range(half, side_length, step):
                avg = (height_matrix[r-half, c-half] + height_matrix[r-half, c+half] + height_matrix[r+half, c-half] + height_matrix[r+half, c+half]) / 4.0
                height_matrix[r, c] = np.clip(avg, 0.0, 1.0) + random.uniform(-s, s)
        for r in range(0, side_length, half):
            shift = half if (r % step == 0) else 0
            for c in range(shift, side_length, step):
                total = 0.0
                count = 0
                if r >= half: total += height_matrix[r-half, c]; count += 1
                if r + half < side_length: total += height_matrix[r+half, c]; count += 1
                if c >= half: total += height_matrix[r, c-half]; count += 1
                if c + half < side_length: total += height_matrix[r, c+half]; count += 1
                height_matrix[r, c] = np.clip((total / count), 0.0, 1.0) + random.uniform(-s, s)

        step = half
        s *= roughness

    height_map = height_matrix.flatten()
    grid = []
    for r in range(side_length):
        for c in range(side_length):
            i = idx(r, c)
            val = height_map[i]
            pos_x = start_x + (c * cell_size)
            pos_y = start_y - (r * cell_size)
            cell = Square(side_length=cell_size)
            cell.move_to([pos_x, pos_y, 0])
            cell.set_stroke(width=0.2, color=GRAY)
            cell.set_fill(opacity=0)
            grid.append(cell)

    animations = []

    animations.append(Create(VGroup(*grid), run_time=1.0))

    base_corners = [idx(0, 0), idx(0, side_length-1), idx(side_length-1, 0), idx(side_length-1, side_length-1)]
    animations.append(AnimationGroup(
        *[grid[i].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[i])), opacity=1) for i in base_corners],
        run_time=0.4
    ))

    step_size = side_length - 1
    while step_size > 1:
        half_step = step_size // 2
        diamond_flashes = []
        diamond_reveals = []
        for r in range(half_step, side_length, step_size):
            for c in range(half_step, side_length, step_size):
                center = idx(r, c)
                p1, p2 = idx(r - half_step, c - half_step), idx(r - half_step, c + half_step)
                p3, p4 = idx(r + half_step, c - half_step), idx(r + half_step, c + half_step)
                diamond_flashes.extend([grid[p1], grid[p2], grid[p3], grid[p4]])
                diamond_reveals.append(grid[center].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[center])), opacity=1))
        
        if diamond_reveals:
            animations.append(AnimationGroup(*diamond_reveals, run_time=0.4))

        square_flashes = []
        square_reveals = []
        for r in range(0, side_length, half_step):
            col_start = half_step if (r % step_size == 0) else 0
            for c in range(col_start, side_length, step_size):
                midpoint = idx(r, c)
                if r >= half_step: square_flashes.append(grid[idx(r - half_step, c)])
                if r + half_step < side_length: square_flashes.append(grid[idx(r + half_step, c)])
                if c >= half_step: square_flashes.append(grid[idx(r, c - half_step)])
                if c + half_step < side_length: square_flashes.append(grid[idx(r, c + half_step)])
                square_reveals.append(grid[midpoint].animate.set_fill(color=rgb_to_hex(default_biome_htc(height_map[midpoint])), opacity=1))
        
        if square_reveals:
            animations.append(AnimationGroup(*square_reveals, run_time=0.4))

        step_size = half_step

    animations.append(Wait(5))
    bg_square = Square(25, color=DARKER_GRAY)
    animations.append(FadeIn(bg_square))

    return Succession(*animations)
