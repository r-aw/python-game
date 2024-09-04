from random import random
import time

enemy_spaceship = ["sprites/enemy_spaceship-1.png", "sprites/enemy_spaceship-2.png", "sprites/enemy_spaceship-3.png", "sprites/enemy_spaceship-4.png"]


class Enemy:
      
    def __init__(self, tk, canvas, x, y):
        self.canvas = canvas
       # for i in enemy_spaceship:
        self.image = tk.PhotoImage(file="sprites/enemy_spaceship-3.png")
        self.id = self.canvas.create_image(x,y, anchor=tk.NW, image=self.image)
        self.walk = 0
        self.move()

    def move(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        direction = round(random())
        if direction == 0 and x1 > 0:  
            self.canvas.move(self.id, -10, 0)
            
        if direction == 1 and x2 < 320:
            self.canvas.move(self.id, 10, 0)

        self.canvas.after(150, self.move) 
    
    def position(self):
        return self.canvas.bbox(self.id)

    def remove(self):
        self.canvas.delete(self.id) 
