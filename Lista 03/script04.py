'''
Faça um programa que verifique e mostre os números entre 1.000 
e 2.000 (inclusive) que, quando divididos por 11, produzam resto igual a 5
'''
# verificar numeros entre 1000 e 2000 (<= | >=)
contador = 1000
rangeMaximo = 2000
# quando numero entre 1000 e 2000 % 11 == 5, exiba
while (contador > rangeMinimo) and (contador < rangeMaximo):
    contador += 1
    if contador % 11 == 5: # Verifica se dividido por 11 da resto 5
        print(contador, end=' - ')