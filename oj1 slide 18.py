#Programme to find volume of ball and ball pit and number of balls needed to fill the ball pit

#Subroutine for ball problem
def info (pi,radius,height, bp_rad ,vol_bp,_vol_ball, no_ball):
    return(pi,radius,height, bp_rad ,vol_bp,_vol_ball, no_ball)

#Main program

pi= 3.14
radius= 0.05
height=0.2
bp_rad = 1
vol_bp=pi*bp_rad*bp_rad* height
vol_ball= 4/3*pi*radius *radius* radius
no_ball= (vol_bp/vol_ball)* 0.75
print("the volume of the ball pit is  " ,vol_bp)
print("the volume of each ball is" , vol_ball)
print("the number of balls that are needed to fill the pit is " , no_ball)

