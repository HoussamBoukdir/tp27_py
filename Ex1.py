#ce programme permet de calcule et
#d'affiche le volume d'une sphere
import math 
r=float(input("taper le rayon du sphere:"))
#v=4/3*math.pi*r**3
v=4/3*math.pi*math.pow(r,3) #pow=puissance 
#deux chiffres apres la virgule
print(f"le volume du sphere est:{v:.2f}")



