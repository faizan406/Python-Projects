from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image slideshoe viewer")

image_path=[
    r"D:\RAMZAN\wp11989268-cool-tanjiro-wallpapers.jpg",
    r"D:\RAMZAN\wp6922634-far-cry-6-wallpapers.jpg",
    r"D:\RAMZAN\wp1888514-daryl-dixon-wallpapers.jpg",
    r"D:\RAMZAN\wp10033332-barbaroslar-wallpapers.jpg"
]

image_size=(1080,1080)

images=[Image.open(path).resize(image_size) for path in image_path]

photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(2)
        
slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_path)):
        update_image()
        
play_button=tk.Button(root,text="play slideshow",command=start_slideshow)
play_button.pack()

root.mainloop()
