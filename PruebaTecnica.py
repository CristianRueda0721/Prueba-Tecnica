

def ordenar_pares_impares(numeros):
   
    pares = sorted([n for n in numeros if n % 2 == 0])
    
    impares = sorted([n for n in numeros if n % 2 != 0])
   
    return pares + impares


numeros = [5, 2, 7, 9, 10, 4, 3]

resultado = ordenar_pares_impares(numeros)

print(resultado)  

