import os
import tkinter as tk
import time

window = tk.Tk()
window.geometry("300x700")

# Create a list of element texts
source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\\")
element_texts = os.listdir(source_folder)


def create_elements_with_delay():
    for i, text in enumerate(element_texts):
        element = tk.Label(window, text=text)
        element.pack()
        window.update()
        time.sleep(0.5)

create_elements_with_delay()

window.mainloop()
