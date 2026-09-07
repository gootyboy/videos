from manim import *
from helper_funcs import *

class CodeScene(MovingCameraScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        code = get_code(r"""import numpy as np 
import random 

def diamond_square(size, roughness): 
    # Initialize a 2D grid of zeros for the heightmap
    grid = np.zeros((size, size)) 
    
    # Initialize the four corners of the grid with random height values
    grid[0, 0] = random.random() 
    grid[0, size - 1] = random.random() 
    grid[size - 1, 0] = random.random() 
    grid[size - 1, size - 1] = random.random() 
    
    # Set the initial step size to span the entire grid
    step = size - 1 
    current_roughness = roughness 

    # Main loop of the Diamond-Square algorithm
    while step > 1: 
        half = step // 2 

        # --- DIAMOND STEP ---
        # Calculate the midpoint values for each square in the grid
        for x in range(0, size - 1, step): 
            for y in range(0, size - 1, step): 
                # Get heights of the four corner points
                top_left = grid[x, y] 
                top_right = grid[x + step, y] 
                bot_left = grid[x, y + step] 
                bot_right = grid[x + step, y + step] 
                
                # Average the corners and add a random displacement
                avg = (top_left + top_right + bot_left + bot_right) / 4.0 
                grid[x + half, y + half] = avg + random.uniform(-current_roughness, current_roughness) 
                
        # --- SQUARE STEP ---
        # Calculate the midpoint values for each diamond in the grid
        for x in range(0, size, half): 
            # Offset the starting y-coordinate on alternating rows to form the diamond pattern
            start_y = 0 if (x % step == 0) else half 
            for y in range(start_y, size, step): 
                total = 0.0 
                count = 0 
                
                # Check and average adjacent neighbors (handling boundaries)
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

                # Assign the calculated average height with displacement to the diamond center
                grid[x, y] = (total / count) + random.uniform(-current_roughness, current_roughness) 

        # Reduce the step size by half and decrease the roughness for the next detail level
        step //= 2
        current_roughness *= roughness

""")

        code.scale(0.6)
        code.to_edge(UP, buff=1)

        self.play(
            Create(code),
            self.camera.frame.animate.shift(DOWN * 8),
            run_time=90,
            rate_func=linear
        )
        
        self.wait(5)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = CodeScene()
    scene.render()
