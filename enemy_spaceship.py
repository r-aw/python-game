from random import random

enemy_spaceship = ["sprites/enemy_spaceship-1.png", "sprites/enemy_spaceship-2.png", "sprites/enemy_spaceship-3.png", "sprites/enemy_spaceship-4.png"]


class Enemy:
      
    def __init__(self, tk, canvas, x, y):
        self.tk = tk
        self.canvas = canvas
        self.x = x
        self.y = y
        self.images = [tk.PhotoImage(file = image) for image in enemy_spaceship]
        self.current_image = 0
        self.id = self.canvas.create_image(x,y, anchor=tk.NW, image=self.images[self.current_image])
        self.move()
        self.animate()

    def move(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        direction = round(random())
        enemy_width = x2 - x1

        if direction == 0 and x1 > 0:  
            self.canvas.move(self.id, -5, 0)
            
        if direction == 1 and x2 < (320 - enemy_width):
            self.canvas.move(self.id, 5, 0)

        self.canvas.after(100, self.move) 
    
    def position(self):
        return self.canvas.bbox(self.id)

    def remove(self):
        self.canvas.delete(self.id) 

    def animate(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.canvas.itemconfig(self.id, image=self.images[self.current_image])

        self.canvas.after(100, self.animate)

