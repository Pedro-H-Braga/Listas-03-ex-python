'''
Fazer um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário
--ATENÇÃO--: Deverá ser utilizada divisões inteiras para a solução

O QUE TENHO QUE FAZER? 
- minha saída tem que ser o binário daquele número 
- fatorar o numero e pegar a quantidade de vezes que ele será dividido para pegar o resto
- a fatoração em binario ocorre no range de números até 2
- pegar o resto do numero...
'''
entrada = int(input("Informe um valor inteiro: "))

guardaRestos = 0
guardaFatoracao = 0
guardaEntradaAnterior = 0

while entrada > 2:
    #se resto = 0 guarde 0 em guardaRestos já print
    if entrada % 2 == 0:
    #pega a fatoreção para usar na proxima divisao
        guardaEntradaAnterior = entrada
        guardaFatoracao = guardaEntradaAnterior / 2 
    #pega resto
        guardaRestos = 0
        print(guardaRestos)
    #senaose resto = 1 guarde 1 em guardaRestos e já print
    elif entrada % 2 == 1:
    #pega a fatoreção para usar na proxima divisao
        guardaEntradaAnterior = entrada
        guardaFatoracao = guardaEntradaAnterior / 2 
    #pega resto
        guardaRestos = 0
        print(guardaRestos)
    else: print("VALOR INVALIDO")
    

            
# vou precisar fazer um laço que calcule o resto desse numero até ele ser maior que 2
# vou precisar de um (operador auxiliar que guardará os restos das divisões de forma que vá os resto 
# diretamente) e um (operador que guardará a fatoração do numero até ele ser maior que 2)
