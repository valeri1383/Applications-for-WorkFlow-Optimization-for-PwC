import os
import tkinter as tk
import time

window = tk.Tk()
window.geometry("300x700")
window.configure(bg='misty rose',border=5)
window.title('Files on the Desktop')

# Create a list of element texts
source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\\")
element_texts = os.listdir(source_folder)


def create_elements_with_delay():
    for i, text in enumerate(element_texts):
        element = tk.Label(window,fg='navy', bg='misty rose', text=text)
        element.pack()
        window.update()
        time.sleep(0.3)

    window.destroy()

create_elements_with_delay()


window.mainloop()
