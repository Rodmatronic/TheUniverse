import tkinter as tk
import random
import math

l = ["#60f7b2", "#ffba4a", "#4abaff", "#8c4aff", "#ff654a"]

class Universe(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)
        self.bind("<Button-1>", self.zoom_in)
        self.bind("<Button-3>", self.zoom_out)
        self.scale_factor = 1.0

    def zoom_in(self, event):
        self.scale_factor *= 1.1
        self.scale("all", event.x, event.y, 1.1, 1.1)

    def zoom_out(self, event):
        self.scale_factor /= 1.1
        self.scale("all", event.x, event.y, 0.9, 0.9)

def draw_circle(canvas, x, y, radius, **kwargs):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, **kwargs)

def create_galaxy_layer(canvas, num_big_stars, num_small_stars, big_radius_range, small_radius_range):
    for _ in range(num_big_stars):
        x = random.randint(0, canvas.winfo_reqwidth())
        y = random.randint(0, canvas.winfo_reqheight())
        big_radius = random.uniform(*big_radius_range)
        draw_circle(canvas, x, y, big_radius, fill="white")
        
        for _ in range(num_small_stars):
            small_radius = random.uniform(*small_radius_range)
            angle = random.uniform(0, 2 * 3.14159)  # Random angle in radians
            small_x = x + big_radius * 1.9 * random.uniform(1, 3) * math.cos(angle)
            small_y = y + big_radius * 1.9 * random.uniform(1, 3) * math.sin(angle)
            draw_circle(canvas, small_x, small_y, small_radius, fill=random.choice(l))
            small_x = x + big_radius * 1.9 * random.uniform(12, 16) * math.cos(angle)
            small_y = y + big_radius * 1.9 * random.uniform(12, 16) * math.sin(angle)
            draw_circle(canvas, small_x, small_y, small_radius, fill="#ffffff")
            # small_x2 = x + big_radius * 0.1 * random.uniform(90, 90) * math.cos(angle)
            # small_y2 = y + big_radius * 0.1 * random.uniform(60, 89) * math.sin(angle)
            # draw_circle(canvas, small_x2, small_x2, small_radius, fill="cyan")

def main():
    root = tk.Tk()
    root.title("The Universe")

    main_canvas = Universe(root, width=800, height=800, bg="black")
    main_canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Create a layer with big stars and smaller stars around them
    create_galaxy_layer(main_canvas, num_big_stars=1590, num_small_stars=25, big_radius_range=(0.5, 1), small_radius_range=(0.1, 0.4))

    root.mainloop()

if __name__ == "__main__":
    main()
