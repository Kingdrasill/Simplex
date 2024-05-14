import numpy as np  # Importa a biblioteca numpy
import time as tm  # Importa a biblioteca time

def Simplex(n,m,c,A,b):
    inicio = tm.time()  # Registra o tempo de início do algoritmo
    iteracao = 0  # Inicializa o contador de iterações

    c = np.array(c)  # Converte os coeficientes da função objetivo para um array numpy
    A = np.matrix(A)  # Converte a matriz de coeficientes das restrições para uma matriz numpy
    b = np.array(b)  # Converte os valores de b para um array numpy

    # Inicializa as listas de variáveis básicas e não básicas
    variaveis_basicas = list(range(n-m))
    variaveis_nao_basicas = list(range(n-m, n))

    while True:  # Loop principal do algoritmo Simplex
        iteracao += 1  # Incrementa o contador de iterações

        # Divide a matriz A em submatrizes N (variáveis não básicas) e B (variáveis básicas)
        N = A[np.ix_(range(m), variaveis_basicas)]
        B = A[np.ix_(range(m), variaveis_nao_basicas)]

        # Calcula a solução básica
        solucao_basica = np.zeros(n)
        solucao_temp = np.linalg.solve(B, b)
        for i in range(len(variaveis_nao_basicas)):
            solucao_basica[variaveis_nao_basicas[i]] = solucao_temp[i]

        # Calcula os coeficientes de dualidade (lambda)
        coeficientes_base = c[np.ix_(variaveis_nao_basicas)]
        lambda_temp = np.linalg.solve(np.transpose(B), coeficientes_base)

        # Calcula os custos reduzidos
        custos_reduzidos = []
        for i in variaveis_basicas:
            temp = c[i] - np.dot(lambda_temp, A[:, i])[0, 0]
            custos_reduzidos.append(temp)

        # Verifica se há custos reduzidos negativos
        if min(custos_reduzidos) < 0:
            # Escolhe a variável para entra na base (k)
            indicies = np.where(custos_reduzidos == min(custos_reduzidos))
            k = variaveis_basicas[indicies[0][0]] # Variável que vai entrar na base

            # Calcula os limites de troca
            y = np.array(np.linalg.solve(B, A[:, k])).flatten()
            limites = []
            for i in range(len(y)):
                if y[i] > 0:
                    temp = solucao_basica[variaveis_nao_basicas[i]] / y[i]
                    limites.append(temp)
                else:
                    limites.append(None)

            # Escolhe a variável para sair da base (l)
            limites_temp = [x for x in limites if x != None and x >= 0]
            indicies = np.where(limites == min(limites_temp))
            l = variaveis_nao_basicas[indicies[0][0]] # Variável que vai sair da base

            # Realiza a troca de variáveis
            if k in variaveis_basicas and l in variaveis_nao_basicas:
                indice_k = variaveis_basicas.index(k)
                indice_l = variaveis_nao_basicas.index(l)
                variaveis_basicas[indice_k], variaveis_nao_basicas[indice_l] = variaveis_nao_basicas[indice_l], variaveis_basicas[indice_k]

            # Calcula o tempo decorrido e o objetivo atual
            objetivo = np.dot(c, solucao_basica)
            fim = tm.time()
            tempo = fim - inicio

            # Imprime informações sobre a iteração atual
            print(f'Iteração: {iteracao}')
            print(f'Tempo(s): {tempo:.4f}')
            print(f'Objetivo: {objetivo:.4f}')
            print()
        
        else:  # Se não houver custos reduzidos negativos, o algoritmo termina
            objetivo = np.dot(c, solucao_basica)
            fim = tm.time()
            tempo = fim - inicio

            # Imprime informações sobre a solução final
            print(f'Iteração: {iteracao}')
            print(f'Tempo(s): {tempo:.4f}')
            print(f'Objetivo: {objetivo:.4f}')
            print()

            # Retorna o tempo decorrido, o valor objetivo e a solução básica
            resultado = (tempo, objetivo, solucao_basica)
            break

    return resultado  # Retorna o resultado da execução do algoritmo
