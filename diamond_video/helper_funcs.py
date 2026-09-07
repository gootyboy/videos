import numpy as np
import random
from manim import *

def darken_image(mobject):
    copy = mobject.copy()
    copy.pixel_array[:, :, :3] = (copy.pixel_array[:, :, :3] * 0.3).astype(np.uint8)

    return copy

def rgb_to_hex(rgb):
    r, g, b, = rgb
    return f"#{r:02X}{g:02X}{b:02X}"

def get_matching_color(rgb):
    r, g, b = rgb
    luminance = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    if luminance > 128:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

def fake_diamond_square(n=2, roughness=0.5, tl=0.51, tr=0.17, bl=0.0, br=0.61):
    size = (2 ** n) + 1
    grid = [[0.0] * size for _ in range(size)]
    
    # Initialize corners
    grid[0][0] = tl
    grid[0][size-1] = tr
    grid[size-1][0] = bl
    grid[size-1][size-1] = br
    
    step = size - 1
    
    while step > 1:
        half = step // 2
        
        # Diamond step
        for x in range(0, size - 1, step):
            for y in range(0, size - 1, step):
                avg = (grid[x][y] + grid[x + step][y] + grid[x][y + step] + grid[x + step][y + step]) / 4.0
                grid[x + half][y + half] = avg + random.uniform(0, roughness)
                
        # Square step
        for x in range(0, size, half):
            for y in range((x + half) % step, size, step):
                total = 0.0
                count = 0
                if x - half >= 0:
                    total += grid[x - half][y]; count += 1
                if x + half < size:
                    total += grid[x + half][y]; count += 1
                if y - half >= 0:
                    total += grid[x][y - half]; count += 1
                if y + half < size:
                    total += grid[x][y + half]; count += 1
                    
                grid[x][y] = (total / count) + random.uniform(0, roughness)
                
        step = half
        
    return [round(item, 4) for row in grid for item in row]

def fake_diamond_square2(n=2, roughness=0.5, tl=0.51, tr=0.17, bl=0.0, br=0.61):
    size = (2 ** n) + 1
    grid = [[0.0] * size for _ in range(size)]

    grid[0][0] = tl
    grid[0][size-1] = tr
    grid[size-1][0] = bl
    grid[size-1][size-1] = br
    
    step = size - 1
    
    while step > 1:
        half = step // 2

        for x in range(0, size - 1, step):
            for y in range(0, size - 1, step):
                avg = (grid[x][y] + grid[x + step][y] + grid[x][y + step] + grid[x + step][y + step]) / 4.0
                grid[x + half][y + half] = avg + random.uniform(-roughness, roughness)

        for x in range(0, size, half):
            for y in range((x + half) % step, size, step):
                total = 0.0
                count = 0
                if x - half >= 0:
                    total += grid[x - half][y]; count += 1
                if x + half < size:
                    total += grid[x + half][y]; count += 1
                if y - half >= 0:
                    total += grid[x][y - half]; count += 1
                if y + half < size:
                    total += grid[x][y + half]; count += 1
                    
                grid[x][y] = (total / count) + random.uniform(-roughness, roughness)

        step = half

    return [round(item, 2) for row in grid for item in row]

def diamond_square(n, roughness, tl, tr, bl, br):
    size = (2 ** n) + 1
    grid = np.zeros((size, size))

    grid[0, 0] = tl
    grid[0, size - 1] = tr
    grid[size - 1, 0] = bl
    grid[size - 1, size - 1] = br
    
    step = size - 1
    scale = roughness
    
    while step > 1:
        half = step // 2

        for x in range(0, size - 1, step):
            for y in range(0, size - 1, step):
                top_left  = grid[x, y]
                top_right = grid[x + step, y]
                bot_left  = grid[x, y + step]
                bot_right = grid[x + step, y + step]

                avg = (top_left + top_right + bot_left + bot_right) / 4.0
                grid[x + half, y + half] = avg + random.uniform(-scale, scale)

        for x in range(0, size, half):
            start_y = 0 if (x % step == 0) else half
            for y in range(start_y, size, step):
                total = 0.0
                count = 0

                if x - half >= 0:
                    total += grid[x - half, y]
                    count += 1
                if x + half < size:
                    total += grid[x + half, y]
                    count += 1
                if y - half >= 0:
                    total += grid[x, y - half]
                    count += 1
                if y + half < size:
                    total += grid[x, y + half]
                    count += 1
                    
                grid[x, y] = (total / count) + random.uniform(-scale, scale)

        step //= 2
        scale *= roughness
        
    return [float(round(item, 2)) for row in grid for item in row]

def get_code(string):
    return Code(
        code_string=string,
        language="python",
        background="window",
        tab_width=4,
        add_line_numbers=True,
        formatter_style="monokai",
        background_config={ 
            "stroke_color": BLUE,
            "stroke_width": 2,
            "fill_opacity": 0.8
        }
    )
