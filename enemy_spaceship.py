from random import random

enemy_spaceship = [
    "sprites/enemy-spaceship-0.png", "sprites/enemy-spaceship-10.png",
    "sprites/enemy-spaceship-20.png", "sprites/enemy-spaceship-30.png", 
    "sprites/enemy-spaceship-40.png", "sprites/enemy-spaceship-50.png", 
    "sprites/enemy-spaceship-60.png", "sprites/enemy-spaceship-70.png", 
    "sprites/enemy-spaceship-80.png", "sprites/enemy-spaceship-90.png", 
    "sprites/enemy-spaceship-100.png", "sprites/enemy-spaceship-110.png", 
    "sprites/enemy-spaceship-120.png", "sprites/enemy-spaceship-130.png", 
    "sprites/enemy-spaceship-140.png", "sprites/enemy-spaceship-150.png", 
    "sprites/enemy-spaceship-160.png", "sprites/enemy-spaceship-170.png", 
    "sprites/enemy-spaceship-180.png", "sprites/enemy-spaceship-190.png", 
    "sprites/enemy-spaceship-200.png", "sprites/enemy-spaceship-210.png", 
    "sprites/enemy-spaceship-220.png", "sprites/enemy-spaceship-230.png", 
    "sprites/enemy-spaceship-240.png", "sprites/enemy-spaceship-250.png", 
    "sprites/enemy-spaceship-260.png", "sprites/enemy-spaceship-270.png", 
    "sprites/enemy-spaceship-280.png", "sprites/enemy-spaceship-290.png", 
    "sprites/enemy-spaceship-300.png", "sprites/enemy-spaceship-310.png", 
    "sprites/enemy-spaceship-320.png", "sprites/enemy-spaceship-330.png", 
    "sprites/enemy-spaceship-340.png", "sprites/enemy-spaceship-350.png"
]

class Enemy:
      
    def __init__(self, tk, canvas, x, y):
        self.tk = tk
        self.canvas = canvas
        self.x = x
        self.y = y
        self.images = [tk.PhotoImage(file=image) for image in enemy_spaceship]
        self.current_image = 0
        self.id = self.canvas.create_image(x, y, anchor=tk.NW, image=self.images[self.current_image])
        self.move()
        self.animate()

    def move(self):
        if self.id is None:
            return
        
        bbox = self.canvas.bbox(self.id)

        if bbox is None:
            return

        x1, y1, x2, y2 = bbox

        
        direction = round(random())
        enemy_width = x2 - x1
        canvas_width = self.canvas.winfo_width()  # Get canvas width dynamically

        if direction == 0 and x1 > 0:  
            self.canvas.move(self.id, -5, 0)
            
        if direction == 1 and x2 < (canvas_width - enemy_width):
            self.canvas.move(self.id, 5, 0)

        self.canvas.after(100, self.move) 
    
    def position(self):
        return self.canvas.bbox(self.id)

    def remove(self):
        self.canvas.delete(self.id) 

    def animate(self):
        self.current_image = (self.current_image + 2) % len(self.images)
        self.canvas.itemconfig(self.id, image=self.images[self.current_image])
        self.canvas.after(55, self.animate)  # Only one animate call
