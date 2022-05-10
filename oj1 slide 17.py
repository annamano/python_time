#Energy bill calulator

#Subroutine to calculate energy bill
def unit_used(cr,pr):
    return (cr-pr)

#Main program
cr =100
pr =40
cv =float(input(39.3))
energy_price=float(input(2.84))
kWh = unit_used * 1.022 * energy_price *(cv/3.6)
print('Your total for your energy usage is', kWh)
