import tkinter as tk
from tkinter import PhotoImage, Canvas

HEIGHT = 500
WIDHT = 320

# Create the main window
window = tk.Tk()

# Set window properties
window.title('SPACE INVADERS 🛸')
window.geometry('320x500')
window.minsize(320, 500)
window.maxsize(320, 500)


# Load the background image and keep a reference to it
bg = PhotoImage(file = "sprites/purple_nebula.png")

# Create the Canvas and place the background image
canvas = Canvas(window)
canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.pack(fill="both", expand=True)

#create canvas for spaceship
spaceship = tk.PhotoImage(file = "sprites/spaceship.png")
player_ship = canvas.create_image(10,470, anchor = tk.NW, image = spaceship)

#fireball

class Fireball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.image = PhotoImage(file="sprites/fireball.png")
        self.id = self.canvas.create_image(x, y, anchor=tk.NW, image=self.image)
        self.move_up()

    def move_up(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        if y1 > 0:  # Move the fireball up if it's still within the window
            self.canvas.move(self.id, 0, -10)
             # Continue moving up every 50ms
            self.canvas.after(50, self.move_up) 
        else:
            # Remove the fireball when it goes off-screen
            self.canvas.delete(self.id)  



# commands

def left(event):
   x1, y1, x2, y2 = canvas.bbox(player_ship)
   if x1 > 10:  
      canvas.move(player_ship, -10, 0)

def right(event):
   x1, y1, x2, y2 = canvas.bbox(player_ship)
   if x2 < (WIDHT - 10):
      canvas.move(player_ship, 10, 0)

def up(event):
   x1, y1, x2, y2 = canvas.bbox(player_ship)
   if y1 > 0:
      canvas.move(player_ship, 0, -10)

def down(event):
   x1, y1, x2, y2 = canvas.bbox(player_ship)
   if y2 < (HEIGHT - 20):
      canvas.move(player_ship, 0, 10 )
      
# shoot fireball from centre of the playship.

def fire(event):
    x1, y1, x2, y2 = canvas.bbox(player_ship)
    fireball = Fireball(canvas, x1 + (x2-x1)//2, y1)  

# bind commands to keyboard

window.bind("<space>", fire)
window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)

# Start the main loop
window.mainloop()
