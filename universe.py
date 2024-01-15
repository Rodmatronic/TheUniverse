import tkinter as tk
import random
import math

l = ["#60f7b2", "#ffba4a", "#4abaff", "#8c4aff", "#ff654a", "#FFE6AD", "#46E366", "#E34673", "#664FE6", "#4FA3E6", "#E6E54F", "#CA6B55", "#E1B9B0"]

class Universe(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        print("Init!")
        print("Caution! This runs best on Linux!")
        tk.Canvas.__init__(self, master, **kwargs)
        self.bind("<Button-1>", self.zoom_in)
        self.bind("<Button-3>", self.zoom_out)
        self.scale_factor = 1.0

    def smooth_zoom(self, target_scale, event):
        current_scale = self.scale_factor
        steps = 10  # Adjust the number of steps for smoother animation

        for step in range(1, steps + 1):
            scale_ratio = 1 + (target_scale - current_scale) * step / steps
            self.scale("all", event.x, event.y, scale_ratio, scale_ratio)
            self.update_idletasks()
            self.after(10)  # Adjust the delay for smoother animation

        self.scale_factor = target_scale

    def zoom_in(self, event):
        self.smooth_zoom(self.scale_factor * 1.1, event)

    def zoom_out(self, event):
        self.smooth_zoom(self.scale_factor / 1.1, event)

def draw_circle(canvas, x, y, radius, star_id, **kwargs):
    star = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=None, **kwargs)
    canvas.tag_bind(star, "<Enter>", lambda event, id=star_id: show_star_name(canvas, id))
    canvas.tag_bind(star, "<Leave>", lambda event: clear_star_name(canvas))

def show_star_name(canvas, star_id):
    names = ["Sosnowiec", "Atmos", "Betelgeuse", "Cosudos", "Proxima", "Furvol", "Prossuni", "Uranus", "Primatos", "Linus", "Torvulda", "Amadaco", "Forfol", "Maticus", "Anamaticus", "Vixed", "Vecxed", "Krystol", "Kristal", "Amicus", "Adastra", "Flamen", "Bahamy", "Rhetoric", "Ariaul", "Portolsus", "Bopicus", "Biticus", "Portasjay", "Irixinus", "Nationne", "252-PL22", "612-PL21", "947-PI22", "915-PF20", "772-JF34", "Pi", "Pie", "Strobirrie", "Fristoriq"]
    name = random.choice(names)
    canvas.create_text(10, 10, anchor=tk.NW, text=f"Name: {name}", fill="white", font=("Arial", 12), tags="star_name")

def clear_star_name(canvas):
    canvas.delete("star_name")

def create_galaxy_layer(canvas, num_big_stars, num_small_stars, big_radius_range, small_radius_range):
    for star_id in range(num_big_stars):
        x = random.randint(0, canvas.winfo_reqwidth())
        y = random.randint(0, canvas.winfo_reqheight())
        big_radius = random.uniform(*big_radius_range)
        draw_circle(canvas, x, y, big_radius, star_id, fill="white")

        for _ in range(5):
            small_radius = random.uniform(*small_radius_range)
            angle = random.uniform(0, 2 * 3.1415926535)
	    
	    # Asteroids
            small_x2 = x + big_radius * 1.9 * random.uniform(16, 30) * math.cos(angle)
            small_y2 = y + big_radius * 1.9 * random.uniform(16, 30) * math.sin(angle)
            draw_circle(canvas, small_x2, small_y2, 0.2, star_id, fill="#545454")

        for _ in range(num_small_stars):
            small_radius = random.uniform(*small_radius_range)
            angle = random.uniform(0, 2 * 3.1415926535)

	    # Planets that orbit stars
            small_x = x + big_radius * 1.9 * random.uniform(1, 3) * math.cos(angle)
            small_y = y + big_radius * 1.9 * random.uniform(1, 3) * math.sin(angle)
            draw_circle(canvas, small_x, small_y, 0.3, star_id, fill=random.choice(l))
	    
        for _ in range(2):
            small_radius = random.uniform(*small_radius_range)
            angle = random.uniform(0, 2 * 3.1415926535)
	    
	    # Smaller stars to spread out, non-galaxy
            small_x2 = x + big_radius * 1.9 * random.uniform(16, 90) * math.cos(angle)
            small_y2 = y + big_radius * 1.9 * random.uniform(16, 90) * math.sin(angle)
            draw_circle(canvas, small_x2, small_y2, 0.5, star_id, fill="#ffffff")

def main():
    root = tk.Tk()
    root.title("The Universe")

    main_canvas = Universe(root, width=1920, height=1080, bg="black")
    main_canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Create a layer with big stars and smaller stars around them
    print("Generating Giant stars")
    create_galaxy_layer(main_canvas, num_big_stars=100, num_small_stars=0, big_radius_range=(3, 5), small_radius_range=(0.1, 0.4))
    print("Generating Main stars")
    create_galaxy_layer(main_canvas, num_big_stars=1000, num_small_stars=12, big_radius_range=(1.2, 2.3), small_radius_range=(0.1, 0.4))
    print("Generating Sub stars")
    create_galaxy_layer(main_canvas, num_big_stars=500, num_small_stars=7, big_radius_range=(0.5, 1.2), small_radius_range=(0.1, 0.4))
    print("Generating Smaller sub stars")
    create_galaxy_layer(main_canvas, num_big_stars=250, num_small_stars=2, big_radius_range=(0.3, 1), small_radius_range=(0.1, 0.4))
    print("Generating Tiny stars")
    create_galaxy_layer(main_canvas, num_big_stars=25, num_small_stars=2, big_radius_range=(2.3, 3), small_radius_range=(0.1, 0.4))
    root.mainloop()

if __name__ == "__main__":
    main()
