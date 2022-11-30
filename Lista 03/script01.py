'''
Fazer um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário
--ATENÇÃO--: Deverá ser utilizada divisões inteiras para a solução

O QUE TENHO QUE FAZER? 
- minha saída tem que ser o binário daquele número 
- fatorar o numero e pegar a quantidade de vezes que ele será dividido para pegar o resto
- a fatoração em binario ocorre no range de números até 2
- pegar o resto do numero...
'''
a = True
while a == True:
    entrada = int(input("Informe um valor inteiro: "))
    # receber numero int positivo
    if entrada > 0:
        n_bin = bin(entrada)
        print(f"({n_bin}) e o binario de ({entrada})")
# vou precisar fazer um laço que calcule o resto desse numero até ele ser maior que 2
# vou precisar de um (operador auxiliar que guardará os restos das divisões de forma que vá somando os seus resto) e um (operador que guardará a fatoração do numero até ele ser maior que 2)
