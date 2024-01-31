def overhead_function():
    import csv
    from pathlib import Path

    # Create a file path to the CSV file.
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"

    # Create an empty list to store overhead records.
    overheadrecords = []

    # Open the CSV file and read the data.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row.

        # Iterate over each row in the CSV file.
        for row in reader:
            overheadrecords.append([row[0], float(row[1])])   

    def highest_overhead():
        result_str=""
        total_overhead = 0
        highest_overhead = (None, 0)

        # Iterate over each record in the overhead records.
        for records in overheadrecords:
            [expense, overhead] = records
            total_overhead += overhead

            # Check if the current overhead is higher than the highest recorded overhead.
            if overhead > highest_overhead[1]:
                highest_overhead = (expense, overhead)

        # Calculate the percentage of the highest overhead.
        percentage_overhead = round((highest_overhead[1]/total_overhead)*100,2)

        # Add the highest overhead to the result string.
        result_str += f"[HIGHEST OVERHEAD] {highest_overhead[0].upper()}: {percentage_overhead}%\n"

        # Return the result string.
        return result_str
    return highest_overhead()