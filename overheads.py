def overhead_function():
    import csv
    from pathlib import Path

    fp = Path.cwd()/"csv_reports"/"Overheads.csv"

    overheadrecords = []

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) 

        for row in reader:
            overheadrecords.append([row[0], float(row[1])])   

    def highest_overhead():
        result_str=""
        total_overhead = 0
        highest_overhead = (None, 0)

        for records in overheadrecords:
            [expense, overhead] = records
            total_overhead += overhead

            if overhead > highest_overhead[1]:
                highest_overhead = (expense, overhead)

        percentage_overhead = round((highest_overhead[1]/total_overhead)*100,2)

        result_str += f"[HIGHEST OVERHEAD] {highest_overhead[0].upper()}: {percentage_overhead}%\n"

        return result_str
    return highest_overhead()
