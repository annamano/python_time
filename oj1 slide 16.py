# Subroutine to find the cost of fitting a carpet

#Main Program
w = 7
l = 6
room_area = w*l
carpet_price = room_area*17
underlay_cost = 3*room_area
gripper= (w*2)+ (l*2)
fitting_fee= 50
total_cost= fitting_fee + gripper+ underlay_cost +carpet_price
print('Total cost of fitting is £',total_cost)


