import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# New dataset provided as a multi-line string
new_data = """
HP 840 G8 i7	Valeri Vasilev	01/11/2023
Lenovo X1 Yoga G5	Valeri Vasilev	01/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	01/11/2023
Lenovo X1 Yoga G6 EP	Valeri Vasilev	01/11/2023
Lenovo X1 Yoga G6	Debanga Khatanier	03/11/2023
Lenovo X1 Yoga G6	Debanga Khatanier	03/11/2023
HP 840 G7	Debanga Khatanier	03/11/2023
Lenovo X1 Yoga G6 EP	Debanga Khatanier	03/11/2023
Lenovo X1 Yoga G5 2021	Debanga Khatanier	03/11/2023
Lenovo X1 Yoga G6 EP	John Kemp	02/11/2023
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023
HP 840 G8 i7	Rajnesh Bangerh	06/11/2023
Lenovo X1 Yoga G6 EP	Debanga Khatanier	06/11/2023
HP 840 G8 i7	Debanga Khatanier	06/11/2023
HP 840 G8 i7	Debanga Khatanier	06/11/2023
Lenovo X1 Yoga G6 EP	Debanga Khatanier	06/11/2023
Lenovo X1 Yoga G6 EP	Debanga Khatanier	06/11/2023
HP 840 G8 i7	Debanga Khatanier	06/11/2023
HP 840 G7	Valeri Vasilev	08/11/2023
Lenovo X1 Yoga G6 EP	Valeri Vasilev	08/11/2023
HP 840 G7	Valeri Vasilev	08/11/2023
HP 840 G8 i7	Valeri Vasilev	09/11/2023
HP 840 G8 i7	Valeri Vasilev	09/11/2023
HP 840 G8 i7	Valeri Vasilev	09/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023
HP 840 G8 i7	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023
Lenovo X1 Yoga G6	Keith Ochaya	10/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023
HP 840 G8 i7	Keith Ochaya	14/11/2023
HP 840 G8 i7	Keith Ochaya	14/11/2023
HP 840 G8 i7	Keith Ochaya	14/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	14/11/2023
Lenovo X1 Yoga G6	Keith Ochaya	14/11/2023
Lenovo X1 Yoga G6	Keith Ochaya	17/11/2023
Lenovo X1 Yoga G6	Keith Ochaya	17/11/2023
Microsoft Surface Pro 7+	Keith Ochaya	17/11/2023
Lenovo X1 Yoga G5	Keith Ochaya	20/11/2023
Lenovo X1 Yoga G5 2021	Keith Ochaya	20/11/2023
Lenovo X1 Yoga G5	Rajnesh Bangerh	20/11/2023
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023
HP 840 G8 i7	Keith Ochaya	20/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	20/11/2023
Lenovo X1 Yoga G6	Keith Ochaya	20/11/2023
Lenovo X1 Yoga G6 EP	Keith Ochaya	20/11/2023
Lenovo X1 Yoga G6	Keith Ochaya	20/11/2023

"""

def visualize_the_names(data):
    new_data_lines = new_data.strip().split('\n')
    new_rows = []

    plt.style.use('dark_background')

    for line in new_data_lines:
        parts = line.rsplit(maxsplit=3)
        model = ' '.join(parts[:-3])
        name = parts[-3] + ' ' + parts[-2]
        date = parts[-1]
        new_rows.append([model, name, date])

    # Creating a DataFrame from the parsed data
    new_df = pd.DataFrame(new_rows, columns=['Model', 'Name', 'Date'])

    # Convert 'Date' to datetime
    new_df['Date'] = pd.to_datetime(new_df['Date'], format='%d/%m/%Y')

    # Count the frequency of each name within the date period
    date_period = new_df['Date'].min().strftime('%d/%m/%Y') + ' - ' + new_df['Date'].max().strftime('%d/%m/%Y')
    name_counts = new_df['Name'].value_counts()
    colors = plt.cm.viridis(np.linspace(0, 1, len(name_counts)))

    # Plotting the results for the new dataset
    plt.figure(figsize=(10, 6))
    bars = plt.bar(name_counts.index, name_counts.values, color=colors)

    # Adding the total at the top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, yval, ha='center', va='bottom')


    plt.title(f'Shell Inspections for the period - ({date_period})')
    plt.xlabel('Name of Tech Expert',color='white')
    plt.ylabel('Count of inspections',color='white')
    plt.xticks(rotation=45,color='white')
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()
    plt.style.use('default')


def visualize_the_asset_count(data):
    new_data_lines = new_data.strip().split('\n')
    new_rows = [line.split('\t') for line in new_data_lines]
    new_df = pd.DataFrame(new_rows, columns=['Model', 'Name', 'Date'])

    # Extract the date range for the title
    date_range = f"{new_df['Date'].min()} to {new_df['Date'].max()}"

    # Count the frequency of each PC model
    model_counts = new_df['Model'].value_counts()

    # Generate a color for each bar using a colormap
    colors = plt.cm.viridis(np.linspace(0, 1, len(model_counts)))

    # Plotting the results for the PC model frequency
    plt.figure(figsize=(10, 6), facecolor='black')  # Set the background to dark blue
    ax = plt.axes()
    ax.set_facecolor('black')
    bars = model_counts.plot(kind='bar', color=colors)
    plt.title(f'Frequency of PC Models from {date_range}',color='white')
    plt.xlabel('PC Model',color='white')
    plt.ylabel('Count of PCs',color='white')
    plt.xticks(rotation=45,color='white')

    # Adding the total number of PCs on top of each bar
    for bar in bars.patches:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{int(bar.get_height())}',
                ha='center', color='white', fontweight='bold')

    for spine in ax.spines.values():
        spine.set_edgecolor('white')

    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()



visualize_the_asset_count(new_data)
visualize_the_names(new_data)