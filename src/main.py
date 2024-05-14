# -*- coding: utf-8 -*-
import entrada  # Importa o módulo entrada, que contém a função lerEntrada para ler o arquivo de entrada
import simplex  # Importa o módulo simplex, que contém a função Simplex para resolver o problema de programação linear

# Solicita ao usuário o nome do arquivo de entrada e lê o nome digitado
print('Digite o nome do arquivo de entrada: ', end='')
nome = input()
print()

# Chama a função lerEntrada do módulo entrada para ler o arquivo de entrada e obter os dados do problema
(status, msg, n, m, c, A, b) = entrada.lerEntrada(nome)

# Verifica se a leitura do arquivo de entrada foi bem-sucedida
if status:
    # Chama a função Simplex do módulo simplex para resolver o problema de programação linear
    resultado = simplex.Simplex(n, m, c, A, b)
    
    # Imprime informações sobre a solução ótima encontrada
    print(f'Solução ótima encontrada em {resultado[0]:.4f} segundos!')
    print(f'Função objetivo é {resultado[1]:.4f}.')
    print()

    # Imprime os valores das variáveis na solução ótima
    for i in range(len(resultado[2])):
        print(f'x[{i+1}] = {resultado[2][i]:.4f}')
else:
    # Imprime a mensagem de erro se houver algum problema ao ler o arquivo de entrada
    print(msg)
