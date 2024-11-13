import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from openpyxl import load_workbook

# Function to load asset numbers from a CSV file
def load_assets_from_csv(file_path):
    assets = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Check if the row is not empty
                assets.append(row[0])
    return assets

# Function to load asset numbers from an Excel file
def load_assets_from_excel(file_path):
    workbook = load_workbook(filename=file_path)
    sheet = workbook.active
    assets = [cell.value for cell in sheet['A'] if cell.value is not None]
    return assets

# Function to compare asset lists
def compare_assets(list_stock, list_scanned):
    matching_items = [item for item in list_stock if item in list_scanned]
    missing_assets = [item for item in list_stock[1:] if item not in list_scanned]
    extra_in_scanned = [item for item in list_scanned if item not in list_stock]
    return matching_items, missing_assets, extra_in_scanned

# Function to load stock CSV file
def load_stock_file():
    global list_stock
    stock_file_path = filedialog.askopenfilename(title="Select Stock CSV File", filetypes=[("CSV files", "*.csv")])
    if stock_file_path:
        list_stock = load_assets_from_csv(stock_file_path)
        stock_label.config(text=f"Stock file loaded: {stock_file_path}")

# Function to load scanned Excel file
def load_scanned_file():
    global list_scanned
    scanned_file_path = filedialog.askopenfilename(title="Select Scanned Excel File", filetypes=[("Excel files", "*.xlsx")])
    if scanned_file_path:
        list_scanned = load_assets_from_excel(scanned_file_path)
        scanned_label.config(text=f"Scanned file loaded: {scanned_file_path}")

# Function to compare loaded files
def load_and_compare():
    if not list_stock or not list_scanned:
        messagebox.showerror("Error", "Please load both files.")
        return

    global matching_items, missing_assets, extra_in_scanned
    matching_items, missing_assets, extra_in_scanned = compare_assets(list_stock, list_scanned)

    update_result_label()

# Function to update result label with colored text
def update_result_label():
    result_text.delete(1.0, tk.END)  # Clear previous text

    if show_accounted:
        result_text.insert(tk.END, "Accounted assets:\n", "accounted")
        result_text.insert(tk.END, f"{matching_items}\n\n", "accounted")
        result_text.insert(tk.END, f"Total accounted assets: {len(matching_items)}\n\n", "accounted")

    result_text.insert(tk.END, "Missing assets:\n", "missing")
    result_text.insert(tk.END, f"{missing_assets}\n\n", "missing")
    result_text.insert(tk.END, f"Total missing assets: {len(missing_assets)}\n\n","missing")

    result_text.insert(tk.END, "Extra items:\n", "extra")
    result_text.insert(tk.END, f"{extra_in_scanned}\n\n", "extra")
    result_text.insert(tk.END, f"Total extra assets: {len(extra_in_scanned)}\n\n","extra")


# Function to toggle the visibility of accounted assets
def toggle_accounted_assets():
    global show_accounted
    show_accounted = not show_accounted
    update_result_label()
    toggle_button.config(text="Hide Accounted Assets" if show_accounted else "Show Accounted Assets")

# Function to export results to a CSV file
def export_to_csv():
    if not matching_items and not missing_assets and not extra_in_scanned:
        messagebox.showerror("Error", "No data to export. Please compare the files first.")
        return

    export_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if export_file_path:
        with open(export_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Accounted Assets"])
            writer.writerows([[item] for item in matching_items])
            writer.writerow([])
            writer.writerow(["Missing Assets"])
            writer.writerows([[item] for item in missing_assets])
            writer.writerow([])
            writer.writerow(["Extra Items"])
            writer.writerows([[item] for item in extra_in_scanned])
        messagebox.showinfo("Export Successful", f"Results exported to {export_file_path}")

# Function to copy results to clipboard
def copy_results():
    root.clipboard_clear()
    root.clipboard_append(result_text.get(1.0, tk.END))
    messagebox.showinfo("Copied", "Results copied to clipboard")

# Initialize global variables
list_stock = []
list_scanned = []
matching_items = []
missing_assets = []
extra_in_scanned = []
show_accounted = True

# Create the main window
root = tk.Tk()
root.title("Asset Comparison Tool")
root.geometry("900x700")  # Set the window size

# Create and place the widgets
load_stock_button = tk.Button(root, text="Load Stock CSV File", bg='lemon chiffon', command=load_stock_file)
load_stock_button.pack(pady=10)

stock_label = tk.Label(root, text="No stock file loaded", justify=tk.LEFT, wraplength=500)
stock_label.pack(pady=5)

load_scanned_button = tk.Button(root, text="Load Scanned Excel File", bg='lemon chiffon', command=load_scanned_file)
load_scanned_button.pack(pady=10)

scanned_label = tk.Label(root, text="No scanned file loaded", justify=tk.LEFT, wraplength=500)
scanned_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

compare_button = tk.Button(button_frame, text="Compare Files", fg='green', bg='lightgrey', command=load_and_compare)
compare_button.pack(side=tk.LEFT, padx=5)

toggle_button = tk.Button(button_frame, text="Hide Accounted Assets", bg='lightgrey', command=toggle_accounted_assets)
toggle_button.pack(side=tk.LEFT, padx=5)

export_button = tk.Button(button_frame, text="Export to CSV", fg='red', bg='lightgrey', command=export_to_csv)
export_button.pack(side=tk.LEFT, padx=5)

# Add a button to copy results to clipboard
copy_button = tk.Button(button_frame, text="Copy Results",fg='dodger blue', bg='lightgrey', command=copy_results)
copy_button.pack(side=tk.LEFT, padx=5)

result_text = tk.Text(root, wrap=tk.WORD, width=80, height=25)  # Increased size
result_text.pack(pady=20)

# Configure text tags for coloring
result_text.tag_configure("accounted", foreground="green")
result_text.tag_configure("missing", foreground="red")
result_text.tag_configure("extra", foreground="blue")

# Run the application
root.mainloop()
