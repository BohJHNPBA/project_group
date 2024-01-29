import cash_on_hand, overheads, profit_loss

def main():

    overheads_output = overheads.????()
    coh_output = cash_on_hand.coh_function()
    profitloss_output = profit_loss.profit_loss_function()

    return(overheads_output,coh_output,profitloss_output)

(overheads_output,coh_output,profitloss_output) = main()

with open('summary_report.txt', 'w') as file:
    file.write(overhead_output + coh_output + profitloss_output)
