
numero = int(input("Ingresa un número decimal: "))


if numero == 0:
    print("Binario: 0")
else:
    binario = ""   
    n = numero      

    
    while n > 0:
        residuo = n % 2       
        binario = str(residuo) + binario   
        n = n // 2            


    print(f"Binario: {binario}")
    