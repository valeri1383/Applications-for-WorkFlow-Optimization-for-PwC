import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


data_for_model_percentage = """
Model\tTester\tDate\tStatus
HP 840 G7	Ashish Bhudia	30/10/2023	PASS
HP ZBook Firefly G10 14	Ashish Bhudia	30/10/2023	PASS
HP ZBook Firefly G10 14	Ashish Bhudia	30/10/2023	PASS
Lenovo X1 Yoga G6 EP	Ashish Bhudia	30/10/2023	PASS
HP 840 G7	Ashish Bhudia	30/10/2023	PASS
Lenovo X1 Yoga G6 EP	Ashish Bhudia	30/10/2023	PASS
Lenovo X1 Yoga G6 EP	Ashish Bhudia	30/10/2023	PASS
HP 840 G7	Ashish Bhudia	30/10/2023	PASS
HP 840 G7	Valeri Vasilev	31/10/2023	PASS
Lenovo X1 Yoga G6 EP	Valeri Vasilev	31/10/2023	PASS
HP 840 G7	Valeri Vasilev	31/10/2023	PASS
HP 840 G8 i7	Valeri Vasilev	31/10/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	31/10/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	31/10/2023	PASS
HP 840 G8 i7	Debanga Khatanier	31/10/2023	PASS
HP 840 G8 i7	Debanga Khatanier	31/10/2023	PASS
HP 840 G8 i7	Debanga Khatanier	31/10/2023	PASS
Lenovo X1 Yoga G6 EP	Debanga Khatanier	31/10/2023	FAIL
HP 840 G8 i7	Valeri Vasilev	01/11/2023	PASS
Lenovo X1 Yoga G5	Valeri Vasilev	01/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	01/11/2023	PASS
Lenovo X1 Yoga G6 EP	Valeri Vasilev	01/11/2023	PASS
Lenovo X1 Yoga G6	Debanga Khatanier	03/11/2023	PASS
Lenovo X1 Yoga G6	Debanga Khatanier	03/11/2023	PASS
HP 840 G7	Debanga Khatanier	03/11/2023	PASS
Lenovo X1 Yoga G6 EP	Debanga Khatanier	03/11/2023	PASS
Lenovo X1 Yoga G5 2021	Debanga Khatanier	03/11/2023	PASS
Lenovo X1 Yoga G6 EP	John Kemp	02/11/2023	FAIL
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Rajnesh Bangerh	06/11/2023	PASS
HP 840 G8 i7	Rajnesh Bangerh	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Debanga Khatanier	06/11/2023	PASS
HP 840 G8 i7	Debanga Khatanier	06/11/2023	PASS
HP 840 G8 i7	Debanga Khatanier	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Debanga Khatanier	06/11/2023	PASS
Lenovo X1 Yoga G6 EP	Debanga Khatanier	06/11/2023	PASS
HP 840 G8 i7	Debanga Khatanier	06/11/2023	PASS
HP 840 G7	Valeri Vasilev	08/11/2023	PASS
Lenovo X1 Yoga G6 EP	Valeri Vasilev	08/11/2023	PASS
HP 840 G7	Valeri Vasilev	08/11/2023	PASS
HP 840 G8 i7	Valeri Vasilev	09/11/2023	PASS
HP 840 G8 i7	Valeri Vasilev	09/11/2023	FAIL
HP 840 G8 i7	Valeri Vasilev	09/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023	PASS
HP 840 G8 i7	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	10/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	10/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	10/11/2023	PASS
HP 840 G8 i7	Keith Ochaya	14/11/2023	PASS
HP 840 G8 i7	Keith Ochaya	14/11/2023	PASS
HP 840 G8 i7	Keith Ochaya	14/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	14/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	14/11/2023	FAIL
Lenovo X1 Yoga G6	Keith Ochaya	17/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	17/11/2023	PASS
Microsoft Surface Pro 7+	Keith Ochaya	17/11/2023	PASS
Lenovo X1 Yoga G5	Keith Ochaya	20/11/2023	PASS
Lenovo X1 Yoga G5 2021	Keith Ochaya	20/11/2023	PASS
Lenovo X1 Yoga G5	Rajnesh Bangerh	20/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	20/11/2023	PASS
HP 840 G8 i7	Keith Ochaya	20/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	20/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	20/11/2023	PASS
Lenovo X1 Yoga G6 EP	Keith Ochaya	20/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	20/11/2023	FAIL
Lenovo X1 Yoga G6	Keith Ochaya	21/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	21/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	21/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	21/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	21/11/2023	PASS
HP 840 G8 i7	Keith Ochaya	21/11/2023	FAIL
HP 840 G7	Keith Ochaya	21/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	21/11/2023	PASS
Lenovo X1 Yoga G6	John Kemp	21/11/2023	PASS
Lenovo X1 Yoga G6	John Kemp	21/11/2023	PASS
Lenovo X1 Yoga G6	John Kemp	21/11/2023	PASS
HP 840 G8 i7	John Kemp	21/11/2023	PASS
HP 840 G8 i7	Peter Sosu	22/11/2023	PASS
HP 840 G8 i7	Peter Sosu	22/11/2023	PASS
HP 840 G8 i7	Peter Sosu	22/11/2023	PASS
Lenovo X1 Yoga G6	Valeri Vasilev	24/11/2023	PASS
HP 840 G7	Valeri Vasilev	24/11/2023	PASS
HP 840 G8 i7	Valeri Vasilev	24/11/2023	PASS
HP 840 G7	Keith Ochaya	24/11/2023	PASS
Lenovo X1 Yoga G6	Keith Ochaya	24/11/2023	PASS
HP 840 G7	Keith Ochaya	24/11/2023	PASS
Lenovo X1 Yoga G5	Rajnesh Bangerh	24/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	24/11/2023	PASS
HP 840 G8 i7	Rajnesh Bangerh	24/11/2023	PASS
Lenovo X1 Yoga G6	Rajnesh Bangerh	24/11/2023	PASS
Lenovo X1 Yoga G6	John Kemp	24/11/2023	FAIL
Lenovo X1 Yoga G5 2021	John Kemp	24/11/2023	PASS
Lenovo X1 Yoga G6	John Kemp	24/11/2023	PASS
"""

def overview_of_good_and_bad_laptops_barchat(data):
    # Converting the string data to a pandas DataFrame
    data_io = StringIO(data)
    df = pd.read_csv(data_io, sep='\t')

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')  # Handle any date parsing errors

    # Normalizing the status to have consistent casing
    df['Status'] = df['Status'].str.upper()

    # Grouping by Model, Date, and Status and counting the occurrences
    grouped_df = df.groupby(['Model', 'Date', 'Status']).size().unstack(fill_value=0).stack()

    # Resetting index to make 'Status' a column again
    grouped_df = grouped_df.reset_index(name='Count')

    # Pivot to have separate columns for PASS and FAIL counts per model per date
    pivot_df = grouped_df.pivot_table(index=['Model', 'Date'], columns='Status', fill_value=0)

    # Flatten the columns multi-index
    pivot_df.columns = [f'{status}' for _, status in pivot_df.columns]
    pivot_df.reset_index(inplace=True)

    # Sorting by Date to have a chronological order
    pivot_df.sort_values(by='Date', inplace=True)

    # First, we determine the date period for the title
    date_period = f"{df['Date'].min().strftime('%d/%m/%Y')} - {df['Date'].max().strftime('%d/%m/%Y')}"

    # Set the background color and frame for the plot
    plt.rcParams['figure.facecolor'] = 'black'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['axes.edgecolor'] = 'white'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['legend.edgecolor'] = 'white'

    # Creating a bar plot
    fig, ax = plt.subplots(figsize=(11, 6))

    # Plotting bars for each model with PASS and FAIL counts and adding count annotations
    for i, model in enumerate(pivot_df['Model'].unique()):
        model_data = pivot_df[pivot_df['Model'] == model]
        pass_fail_counts = model_data[['PASS', 'FAIL']].sum()
        pass_bar = ax.bar(i, pass_fail_counts['PASS'], color='green', width=0.8, label='PASS' if i == 0 else "")
        fail_bar = ax.bar(i, pass_fail_counts['FAIL'], bottom=pass_fail_counts['PASS'], color='red', width=0.8,
                          label='FAIL' if i == 0 else "")

        # Annotating the PASS count
        ax.annotate(f'{pass_fail_counts["PASS"]}',
                    xy=(pass_bar[0].get_x() + pass_bar[0].get_width() / 2, pass_fail_counts["PASS"] / 2),
                    xytext=(0, 0),  # no offset
                    textcoords="offset points",
                    ha='center', va='center',
                    color='white', fontsize=10, fontweight='bold')

        # Annotating the FAIL count
        if pass_fail_counts['FAIL'] > 0:  # only annotate if there are fails
            ax.annotate(f'{pass_fail_counts["FAIL"]}',
                        xy=(fail_bar[0].get_x() + fail_bar[0].get_width() / 2,
                            pass_fail_counts["PASS"] + pass_fail_counts["FAIL"] / 2),
                        xytext=(0, 0),  # no offset
                        textcoords="offset points",
                        ha='center', va='center',
                        color='white', fontsize=10, fontweight='bold')

    # Customizing the plot
    ax.set_xticks(range(len(pivot_df['Model'].unique())))
    ax.set_xticklabels(pivot_df['Model'].unique(), rotation=45, ha='right')
    ax.set_ylabel('Count')
    ax.set_title(f'Pass and Fail Counts per Model\nDate Period: {date_period}', color='white')

    # Changing the color of the labels and ticks to white
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white', which='both')

    # Adding legend with black background and white text
    legend = ax.legend(facecolor='black')
    plt.setp(legend.get_texts(), color='white')

    plt.tight_layout()
    plt.show()


def overview_of_good_and_bad_laptops_piechart(input_data):
    # Converting the string data to a pandas DataFrame
    data_io = StringIO(input_data)
    df = pd.read_csv(data_io, sep='\t')

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')  # Handle any date parsing errors

    # Normalizing the status to have consistent casing
    df['Status'] = df['Status'].str.upper()

    # Grouping by Model and Status and counting the occurrences
    model_status_counts = df.groupby(['Model', 'Status']).size().unstack(fill_value=0)

    # Plotting pie charts for each model
    fig, axes = plt.subplots(1, model_status_counts.shape[0], figsize=(12, 6))
    fig.set_facecolor('grey')

    # Iterate over models and their respective counts
    for ax, (model, counts) in zip(axes, model_status_counts.iterrows()):
        colors = ['red' if status == 'FAIL' else 'green' for status in counts.index]
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=colors)

        # Set the title as the model name with line breaks if it's too long
        if len(model) > 20:
            model = '\n'.join([model[i:i + 20] for i in range(0, len(model), 20)])
        ax.set_title(model, fontsize=12, rotation=30, ha='center')

    # Filter out rows with invalid dates (if any)
    df = df.dropna(subset=['Date'])

    # Setting the date frame as the overall title
    date_period = f"{df['Date'].min().strftime('%d/%m/%Y')} - {df['Date'].max().strftime('%d/%m/%Y')}"
    plt.suptitle(date_period, fontsize=14)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust the rect so the title fits and does not overlap with the plots
    plt.show()


overview_of_good_and_bad_laptops_piechart(data_for_model_percentage)
overview_of_good_and_bad_laptops_barchat(data_for_model_percentage)