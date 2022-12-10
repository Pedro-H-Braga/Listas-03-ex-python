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

guardaFatoracao = guardaEntradaAnterior / 2 

# talves eu precise de um contador que a cada vez que ele mudar 
# fazer uma operação até o número ser maior que 2, se menor que 2 saia do loop

guardaEntradaAnterior = entrada

while entrada > 2:

    
        #se resto = 0 guarde 0 em guardaRestos já print
        
        if guardaEntradaAnterior % 2 == 0:
            
            #pega resto
            guardaRestos = 0        
            print(guardaRestos)

            #pega a fatoração para usar na proxima divisao
            guardaFatoracao = guardaEntradaAnterior / 2 

            guardaEntradaAnterior = guardaFatoracao 

            entrada = guardaEntradaAnterior
            #senaose resto = 1 guarde 1 em guardaRestos e já print
        elif guardaEntradaAnterior % 2 == 1:

            #pega resto
            guardaRestos = 1
            print(guardaRestos)
        
            #pega a fatoração para usar na proxima divisao
            guardaFatoracao = guardaEntradaAnterior / 2 

            guardaEntradaAnterior = guardaFatoracao 
            
            entrada = guardaEntradaAnterior
            
        else: 
            print("VALOR INVALIDO")
            guardaEntradaAnterior = 0
    
    
        

            
# vou precisar fazer um laço que calcule o resto desse numero até ele ser maior que 2
# vou precisar de um (operador auxiliar que guardará os restos das divisões de forma que vá os resto 
# diretamente) e um (operador que guardará a fatoração do numero até ele ser maior que 2)
