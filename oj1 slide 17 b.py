#Subroutine to output the properties of a circle
def properties(d,rad,cif,area,arc, pi):
    return (d,rad,cif,area,arc, pi)

#Main programme
d =44
rad=d/2
pi = 3.14
cif= pi * d
area= pi *rad*rad
arc= (cif*44)/360

print("The radius of the circle is",rad)
print("The area of the circle ", area)
print("The circumference of the circle ", cif)
print("The arc length is",arc)
