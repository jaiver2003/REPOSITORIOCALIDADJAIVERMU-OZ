
binario = input("Ingresa un número binario: ")

decimal = 0     
posicion = 0    


for digito in reversed(binario):
    decimal += int(digito) * (2 ** posicion)   
    posicion += 1                              

print(f"Decimal: {decimal}")