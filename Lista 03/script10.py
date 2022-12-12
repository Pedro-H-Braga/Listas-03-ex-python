# para media
soma = quantidade = media = 0
# para maior numero
maior = menor = 0
# Media dos valores digitados
while True:
    entrada = int(input("Digite um número inteiro: "))
    # media
    soma += entrada
    quantidade += 1
    media = soma / quantidade
    # maior e menor
    if quantidade == 1:
        maior = menor = entrada
    else:
        if entrada > maior:
            maior = entrada
        if entrada < menor:
            menor = entrada

    # para sair do laço
    if entrada == 0:
        print("SAINDO DO PROGRAMA\n")
        break

# media
print(f"Quantidade de números digitados: {quantidade}",end='\n')
print(f"Soma: {soma}", end='\n')
print(f"Média: {media:10.2f}", end='\n')
# maior menor
print(f"O maior foi {maior} e o menor foi {menor}", end='\n')