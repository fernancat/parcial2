def superficie(base, altura):
    return float(base) *  float(altura)



def mayor_de_dos_superficies(superficie1, superficie2):
    if superficie1 > superficie2:
        return f" Superficie1: {superficie1} es mayor a Superficie2: {superficie2}"
    else:
        return f" Superficie2: {superficie2} es mayor a Superficie1: {superficie1}"

superficie_rectangulo1 = superficie(10,20)
superficie_rectangulo2 = superficie(30,40)


print(mayor_de_dos_superficies(superficie_rectangulo1, superficie_rectangulo2))