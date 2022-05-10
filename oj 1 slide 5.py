# Using variables and constants

#Subroutine to calculate the flow rate of IV infusion flow pump
def FlowRate(Volume,Time):
    return (Volume / Time )* 60
# Main program
Volume = 100
Time = 30
Pump = (Volume / Time )* 60
print("The flow rate of the IV infusion flow pump is", Pump, "ml/hr")
