def profit_loss_function():
    import csv
    
    
    def read_csv_data(file_path):
        """
        Function to read data from a CSV file.
        - Parameter needed is the CSV file path.
        """
        
        data = []
        # Open the file and read the data
        with open(file_path, newline='',encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header row
            for row in reader:
                day = int(row[0])
                profit = int(row[4])
                data.append((day, profit)) # Append the data to the list
        return data # Return the list of data

    # Read the data from the CSV file
    value = read_csv_data("csv_reports/Profit_and_Loss.csv") 

    def case_identifier(value):
        """
     Function to identify the trend in the net net profit data.
     - Parameter needed is the net net profit data.
     """
        Always_increasing = True
        Always_decreasing = True
        # Iterate through the data
        for numbers in range(1, len(value)-1):
            [day, profit] = value[numbers]
            [day_tomorrow, profit_tomorrow] = value[numbers+1]
           # Check if the net profit flow is fluctuating
            if Always_decreasing == False and Always_increasing == False:
                return "Fluctuating"
             # Check if the net profit flow is always increasing or decreasing
            if profit < profit_tomorrow:
                Always_decreasing = False
            if profit > profit_tomorrow:
                Always_increasing = False 
        # Return the identified trend
        if Always_increasing:
            return "Always_increasing"
        
    
    def always_increasing(value):
        """
        Function to analyze the data when the net net profit is always increasing.
        - If the net profit is always increasing, the function will find out
        the day and amount the highest increment occurs.
        """
        
        largest_increase = (0,0)
        for item in range(1, len(value)):
            # Unpack the day and cash value for the current item
            [day , profit] = value[item]
            # Unpack the day and cash value for the previous item
            [prev_day, prev_profit] = value[item-1]
            increase =  profit - prev_profit # Calculate the increase in cash from the previous day to the current day
           # Find the day with the largest increase in net profit
            if increase > largest_increase[1]:
                largest_increase = (day, increase) # Update the largest_increase with the current day and increase
        # Return the day and amount of the largest increase
        return largest_increase

    def always_decreasing(value):
        """
        Function to analyze the data when the net net profit is always decreasing.
        - If the net profit is always decreasing, the function will find out the day and amount the highest decrement occurs.
        """

        largest_decrease = (0,0)
        for item in range(1, len(value)):
            # Unpack the day and cash value for the current item
            [day , profit] = value[item]
             # Unpack the day and cash value for the previous item
            [prev_day, prev_profit] = value[item-1]
            decrease = (prev_profit - profit)
            # Find the day with the largest decrease in net profit
            if decrease > largest_decrease[1]:
                largest_decrease = (day, decrease) # Update the largest_decrease with the current day and decrease
        # Return the day and amount of the largest decrease
        return largest_decrease
    
    def fluctuation(value):
        """
        Function to analyze the data when the net net profit is fluctuating.
        - If the net net profit is fluctuating, the function will find out the days and amounts where the highest decrements occur.
        """

        decrease = (0,0)
        profit_deficit = [] # Initialize an empty list to store the days with profit deficit 
        for item in range(1, len(value)):
            # Unpack the day and cash value for the previous item
            [day , profit] = value[item]
            # Unpack the day and cash value for the previous item
            [prev_day, prev_profit] = value[item-1]
            # Find all the days where there is a decrease in net profit
            if prev_profit > profit:
                decrease = (day, (prev_profit - profit)) # Calculate the decrease in profit and store it with the day
                profit_deficit.append(decrease) # Add the day and decrease to the cash deficit list
         # Find the top 3 days with the largest decrease in net profit
        top_3 = []
        # Copy the net profit deficit list to avoid modifying the original list
        copied_list = profit_deficit.copy() 
        # Find the top 3 days with the largest decrease
        for iteration in range(3):
            greatest_decrease = (0,0) 
            for record in copied_list:
                [day, decrease] = record   # Unpack the day and decrease for the current record
                # If the decrease for the current record is greater than the previously recorded greatest decrease
                if decrease > greatest_decrease[1]:
                    greatest_decrease = (day, decrease) # Update the greatest decrease with the current day and decrease
            # Append the greatest decrease to the top 3 list
            top_3.append(greatest_decrease)
            # Remove the greatest decrease from the copied list to avoid duplication
            copied_list.remove(greatest_decrease)
        # Return the top 3 list and the net profit deficit list
        return [top_3, profit_deficit]
    
    
    def profit_analysis():
        """
     This function will compute the difference in net profit if the current day is
     lower than the previous day. 

     - If the net profit is always increasing, the function will find out
     the day and amount the highest increment occurs.
     - If the net profit is always decreasing, the function will find out
     the day and amount the highest decrement occurs.
     - If the net profit is fluctuating, the function will find out
     the days and amounts where the highest decrements occur.
     """
         # Initialize an empty string to store the analysis results
        result_str = ""
       # Identify the trend of the net profit flow
        case = case_identifier(value)
       # Depending on the trend, perform different analyses
        if case == "Always_increasing":
            [day, amount] = always_increasing(value)
            result_str += f"[NET PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
            result_str += f"[HIGHEST NET PROFIT SURPLUS] DAY: {day}, AMOUNT: SGD{amount}\n"
        elif case == "Always_decreasing":
            [day, amount] = always_decreasing(value)
            result_str += f"[NET PROFIT DEFICIT] PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n"
            result_str += f"[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n"
        else:
            [top_3, list_of_deficits] = fluctuation(value)
            for day,amount in list_of_deficits:
                result_str += f"[NET PROFIT DEFICIT] DAY:{day}, AMOUNT: SGD:{amount}\n"
            result_str += f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_3[0][0]}, AMOUNT: SGD{top_3[0][1]}\n"
            result_str += f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {top_3[1][0]}, AMOUNT: SGD{top_3[1][1]}\n"
            result_str += f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {top_3[2][0]}, AMOUNT: SGD{top_3[2][1]}\n"
        # Return the analysis results
        return result_str

    # Return the result of the net profit analysis
    return profit_analysis()