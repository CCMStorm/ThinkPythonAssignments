# Import Statements

# Function Definitions
# Create a calculate_tip function: amount of bill, tip percentage
def calculate_tip( amount_of_bill, tip_percentage ):
    # Print the amount of the bill
    print ("Amount of bill: " + str(amount_of_bill))
    
    # Calculate sales tip amount
    sales_tax_rate = 0.0675
    sales_tax_amount = amount_of_bill * sales_tax_rate
    print ("Sales tax : " + str(sales_tax_amount))

    # Calculate subtotal (amount of the bill + sales tax amount)
    subtotal = amount_of_bill + sales_tax_amount
    print ("Subtotal : " + str(subtotal))

    # Calculate tip amount (subtotal * tip percentage)
    tip_amount = subtotal * tip_percentage
    print ("Tip, based on a " + str(tip_percentage * 100) + "% tip: " + str(tip_amount))

    # Display tip amount
    print (tip_amount)

    # Calculate total bill, including the tip
    total_bill = subtotal + tip_amount
    print ("Total bill: " + str(total_bill))
    
# Program Logic
# Call my calculate_tip function with an example
calculate_tip( 200, 0.15 )
calculate_tip( 100, 0.20 )    