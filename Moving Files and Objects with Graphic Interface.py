import time
import tkinter as tk

def option_selected(option):
    print(option[-1])
    if option[-1] == '1':
        pass
    elif option[-1] == '2':
        pass
    elif option[-1] == '3':
        pass
    elif option[-1] == '4':
        pass
    elif option[-1] == '5':
        pass



# Create the main window
window = tk.Tk()
window.geometry("500x400")
window.configure(bg='misty rose')

# Define the options with descriptions
options = [
    {"name": "Option 1", "description": "1. Move Files by extension or Folders by name"},
    {"name": "Option 2", "description": "2. Move all Files and Folders"},
    {"name": "Option 3", "description": "3. Copy files by extension and Folders by name"},
    {"name": "Option 4", "description": "4. Copy all Files and Folders"},
    {"name": "Option 5", "description": "5. Exit"}
]

# Create and position the buttons with descriptions
for option in options:
    label = tk.Label(window,bg='misty rose',fg='blue', text=option["description"], font=85)
    label.pack()
    window.update()
    time.sleep(0.4)
    button = tk.Button(window,bg='khaki', padx=50, pady=10, text=option["name"], command=lambda option=option: option_selected(option["name"]))
    button.pack()
    window.update()
    time.sleep(0.4)



# Start the main event loop
window.mainloop()

