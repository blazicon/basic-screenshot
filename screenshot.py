from tkinter import *
import pyautogui
import datetime
from PIL import ImageGrab
import pyperclip

def take_bounded_screenshot(x1, y1, x2, y2):
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    file_name = datetime.datetime.now().strftime("%f")
    image.save("snips/" + file_name + ".png")
    pyperclip.copy(image)

class Application():
    def __init__(self, master):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None

        root.geometry('400x50+200+200')  # window sizing.. change for hdpi if in school
        root.title('Basic Screenshots - blazicon_201 (shivaan)')

        self.menu_frame = Frame(master)
        self.menu_frame.pack(fill=BOTH, expand=YES, padx=1, pady=1)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack()

        # scrnshot button
        self.snipButton = Button(self.buttonBar, width=5, height=5, command=self.create_screen_canvas, background="green")

    def create_screen_canvas(self):
        take_bounded_screenshot(self.start_x, self.start_y, self.current_x, self.current_y)

root = Tk()
app = Application(root)
root.mainloop()
