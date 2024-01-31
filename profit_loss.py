def profit_loss_function():
    import csv
    
    
    def read_csv_data(Profit_and_Loss):
        """
        Function to read data from a CSV file.
        - Parameter needed is the CSV file path.
        """
        
        data = []
        # Open the file and read the data
        with open(Profit_and_Loss, newline='',encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header row
            for row in reader:
                day = int(row[0])
                profit = int(row[4])
                data.append((day, profit)) # Append the data to the list
        return data # Return the list of data

    # Read the data from the CSV file
    value = read_csv_data("csv_reports/Profit_and_Loss.csv") 

    
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
            [day , profit] = value[item]
            [prev_day, prev_profit] = value[item-1]
            increase =  profit - prev_profit
           # Find the day with the largest increase in net profit
            if increase > largest_increase[1]:
                largest_increase = (day, increase)
        # Return the day and amount of the largest increase
        return largest_increase

    def always_decreasing(value):
        """
        Function to analyze the data when the net net profit is always decreasing.
        - If the net profit is always decreasing, the function will find out the day and amount the highest decrement occurs.
        """

        largest_decrease = (0,0)
        for item in range(1, len(value)):
            [day , profit] = value[item]
            [prev_day, prev_profit] = value[item-1]
            decrease = mod(prev_profit - profit)
            # Find the day with the largest decrease in net profit
            if decrease > largest_decrease[1]:
                largest_decrease = (day, decrease)
        # Return the day and amount of the largest decrease
        return largest_decrease
    