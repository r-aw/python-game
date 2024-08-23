import tkinter as tk
from tkinter import PhotoImage, Canvas

# Create the main window
window = tk.Tk()



# Load the background image and keep a reference to it
bg = PhotoImage(file = "sprites/purple_nebula.png")


# Create the Canvas and place the background image
canvas = Canvas(window)
canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.pack(fill="both", expand=True)

#create canvas for spaceship
img = tk.PhotoImage(file = "sprites/spaceship.png")
image = canvas.create_image(10,460, anchor = tk.NW, image = img)


# Set window properties
window.title('SPACE INVADERS 🛸')
window.geometry('320x500')
window.minsize(320, 500)
window.maxsize(320, 500)


# Start the main loop
window.mainloop()
