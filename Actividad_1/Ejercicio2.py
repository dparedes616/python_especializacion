
precio=float(input("Igrese el precio del articulo: "))


def ejercicio_2(precio):
    IVA=0.21
    precio_total=round(((precio*IVA)+precio),2)
    return precio_total

precio_total=ejercicio_2(precio)
print(precio_total)

