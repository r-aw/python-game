

enemy_spaceship = ["sprites/enemy_spaceship-1.png", "sprites/enemy_spaceship-2.png", "sprites/enemy_spaceship-3.png", "sprites/enemy_spaceship-4.png"]


class Enemy:
    def __init__(self, tk, canvas, x, y):
        self.canvas = canvas
       # for i in enemy_spaceship:
        self.image = tk.PhotoImage(file="sprites/enemy_spaceship-3.png")
        self.canvas.create_image(x,y, anchor=tk.NW, image=self.image)