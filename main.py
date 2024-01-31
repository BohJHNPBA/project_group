#Imports the functions of cash_on_hand.py, overhead.py and profit_and_loss.py
import cash_on_hand, overheads, profit_loss 

#Function for putting all 3 functions from the different .py into 1 function
def main():
    """
    - Calls the overhead, cash on hand, and profit and loss functions
    - Store their respective outputs in variables
    """
    overhead_output = overheads.overhead_function()
    coh_output = cash_on_hand.coh_function()
    profitloss_output = profit_loss.profit_loss_function()
    
    return(overhead_output,coh_output,profitloss_output)

# Collates the outputs of 3 different functions into 1
overhead_output,coh_output,profitloss_output = main()

with open('summary_report.txt', 'w') as file:
    file.write(overhead_output + coh_output + profitloss_output)