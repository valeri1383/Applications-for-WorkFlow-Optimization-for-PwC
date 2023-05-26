import csv, sys


# Writing to CSV file


with open('test_csv.csv', 'w', newline='') as csvfile:
    fieldnames = ['User', 'Asset', 'Time Inspected']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    user = 'ivan'
    asset = 'petrov'
    time = '1990'
    info = {f'User': user, f'Asset': asset, f'Time Inspected': time}
    writer.writerow(info)
