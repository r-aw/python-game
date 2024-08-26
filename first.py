import tkinter as tk
from tkinter import PhotoImage, Canvas
import pygame

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
image = canvas.create_image(10,460, anchor = tk.NW, image = spaceship)


# move spaceship

def left(event):
   canvas.move(image, -10, 0)

def right(event):
   canvas.move(image, 10, 0)


window .bind("<Left>", left)
window .bind("<Right>", right)

# Start the main loop
window.mainloop()
