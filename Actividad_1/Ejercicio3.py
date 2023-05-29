
diametro=float(input("Igrese el diametro: "))

def ejercicio_3(diametro):
    PI=3.1415
    area=round((diametro*PI),2)
    return area

area=ejercicio_3(diametro)
print(area)