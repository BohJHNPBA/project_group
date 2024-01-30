def coh_function():
    import csv
    
    
    def read_csv_data(file_path):
        """
        Function to read data from a CSV file.
        - Parameter needed is the CSV file path: 
        """
        
        data = []
        # Open the file and read the data
        with open(file_path, newline='',encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header row
            for row in reader:
                day = int(row[0])
                cash = int(row[1])
                data.append((day, cash)) # Append the data to the list
        return data # Return the list of data

    # Read the data from the CSV file
    value = read_csv_data("csv_reports/Cash_on_Hand.csv") 

    
    def mod(x):
        """
        Function to calculate the absolute value of a number.
        - Parameter needed is the number to calculate the absolute value of.
        """
        if x < 0:
            return -x
        else:
            return x

    def case_identifier(value):
        """
     Function to identify the trend in thecash data.
     - Parameter needed is thecash data.
     """
        Always_increasing = True
        Always_decreasing = True
        # Iterate through the data
        for numbers in range(1, len(value)-1):
            [day, cash] = value[numbers]
            [day_tomorrow, cash_tomorrow] = value[numbers+1]
           # Check if the cash flow is fluctuating
            if Always_decreasing == False and Always_increasing == False:
                return "Fluctuating"
             # Check if the cash flow is always increasing or decreasing
            if cash < cash_tomorrow:
                Always_decreasing = False
            if cash > cash_tomorrow:
                Always_increasing = False
        # Return the identified trend
        if Always_increasing:
            return "Always_increasing"
        
    
    def always_increasing(value):
        """
        Function to analyze the data when thecash is always increasing.
        - If the cash is always increasing, the function will find out
        the day and amount the highest increment occurs.
        """
        
        largest_increase = (0,0)
        for item in range(1, len(value)):
            [day , cash] = value[item]
            [prev_day, prev_cash] = value[item-1]
            increase =  cash - prev_cash
           # Find the day with the largest increase in cash
            if increase > largest_increase[1]:
                largest_increase = (day, increase)
        # Return the day and amount of the largest increase
        return largest_increase

    def always_decreasing(value):
        """
        Function to analyze the data when thecash is always decreasing.
        - If the cash is always decreasing, the function will find out the day and amount the highest decrement occurs.
        """

        largest_decrease = (0,0)
        for item in range(1, len(value)):
            [day , cash] = value[item]
            [prev_day, prev_cash] = value[item-1]
            decrease = mod(prev_cash-cash)
            # Find the day with the largest decrease in cash
            if decrease > largest_decrease[1]:
                largest_decrease = (day, decrease)
        # Return the day and amount of the largest decrease
        return largest_decrease
    def fluctuation(value):
        """
        Function to analyze the data when thecash is fluctuating.
        - If the cash is fluctuating, the function will find out the days and amounts where the highest decrements occur.
        """
        decrease = (0,0)
        cash_deficit = [] 
        for item in range(1, len(value)):
            [day , cash] = value[item]
            [prev_day, prev_cash] = value[item-1]
            # Find all the days where there is a decrease in net cash
            if prev_cash > cash:
                decrease = (day, mod(prev_cash - cash))
                cash_deficit.append(decrease)
        # Find the top 3 days with the largest decrease in cash
        top_3 = []
        # Copy the cash deficit list
        copied_list = cash_deficit.copy()
        for iteration in range(3):
            greatest_decrease = (0,0)
            for record in copied_list:
                [day, decrease] = record
                if decrease > greatest_decrease[1]:
                    greatest_decrease = (day, decrease)
            # Append the greatest decrease to the top 3 list
            top_3.append(greatest_decrease)
            # Remove the greatest decrease from the copied list
            copied_list.remove(greatest_decrease)
        # Return the top 3 list and the cash deficit list
        return [top_3, cash_deficit]

    
    def cash_analysis():
        """
     This function will compute the difference in cash if the current day is
     lower than the previous day. 

     - If the cash is always increasing, the function will find out
     the day and amount the highest increment occurs.
     - If the cash is always decreasing, the function will find out
     the day and amount the highest decrement occurs.
     - If the cash is fluctuating, the function will find out
     the days and amounts where the highest decrements occur.
     """
         # Initialize an empty string to store the analysis results
        result_str = ""
       # Identify the trend of the cash flow
        case = case_identifier(value)
       # Depending on the trend, perform different analyses
        if case == "Always_increasing":
            [day, amount] = always_increasing(value)
            result_str += f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
            result_str += f"[HIGHEST CASH SURPLUS] DAY: {day}, AMOUNT: SGD{amount}\n"
        elif case == "Always_decreasing":
            [day, amount] = always_decreasing(value)
            result_str += f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n"
            result_str += f"[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n"
        else:
            [top_3, list_of_deficits] = fluctuation(value)
            for day,amount in list_of_deficits:
                result_str += f"[CASH DEFICIT] DAY:{day}, AMOUNT: SGD:{amount}\n"
            result_str += f"[HIGHEST CASH DEFICIT] DAY: {top_3[0][0]}, AMOUNT: SGD{top_3[0][1]}\n"
            result_str += f"[2ND HIGHEST CASH DEFICIT] DAY: {top_3[1][0]}, AMOUNT: SGD{top_3[1][1]}\n"
            result_str += f"[3RD HIGHEST CASH DEFICIT] DAY: {top_3[2][0]}, AMOUNT: SGD{top_3[2][1]}\n"
        # Return the analysis results
        return result_str

    # Return the result of the cash analysis
    return cash_analysis()
