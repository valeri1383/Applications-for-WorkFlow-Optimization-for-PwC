import tkinter as tk
import time

window = tk.Tk()
window.geometry("500x300")

# Create a list of element texts
element_texts = ["Element 1", "Element 2", "Element 3", "Element 4", "Element 5"]

# Function to create and pack elements with delay
def create_elements_with_delay():
    for i, text in enumerate(element_texts):
        # Create the element
        element = tk.Label(window, text=text)

        # Pack the element
        element.pack()

        # Update the window to show the new element
        window.update()

        # Delay for 1 second
        time.sleep(0.5)

# Call the function to create and pack elements with delay
create_elements_with_delay()

window.mainloop()
