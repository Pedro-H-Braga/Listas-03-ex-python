''' 
FaΓ§a um programa que leia um nΓΊmero e imprima o seu fatorial.

π! = π β (π β 1) β (π β 2) β β¦ β 1

πΈπ₯πππππ:
6! = 6 β 5 β 4 β 3 β 2 β 1
6! = 720

Lembrando ainda que:
0! = 1
'''

entrada = int(input("Informe um valor: "))
fatorial = 1
contador = 1

while contador <= entrada:

    if entrada == 0:
        fatorial = 1
        break
    else:      
        fatorial *= contador
        contador += 1

print(f"Fatorial de {entrada} e: {fatorial}")