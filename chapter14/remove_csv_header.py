#! python3
# remove_csv_header.py -- Removes the header from all CSV files in the current
# working directory.

import csv
import os

os.makedirs("./chapter14/header_removed", exist_ok=True)

# Loop through every file in the current working directory.

for csv_filename in os.listdir("./chapter14"):

    if not csv_filename.endswith(".csv"):

        continue  # Skip non-csv files.

    print("Removing header from " + csv_filename + "...")

    # Read the CSV file in (skipping first row).
    csv_rows = []
    csv_file_obj = open("./chapter14/" + csv_filename)
    reader_obj = csv.reader(csv_file_obj)

    for row in reader_obj:

        if reader_obj.line_num == 1:

            continue  # Skip first row.

        csv_rows.append(row)

    csv_file_obj.close()

    # Write out the CSV file.
    csv_file_obj = open(os.path.join("./chapter14/header_removed", csv_filename), "w", newline="")
    writer_obj = csv.writer(csv_file_obj)
    for row in csv_rows:

        writer_obj.writerow(row)

    csv_file_obj.close()
