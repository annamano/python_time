# Using variables and constants

# Subroutines to calculate price
def Discount(Total, Rate):
    return Total -(Total * Rate/100)

# Main program
print(Discount(55,20))
