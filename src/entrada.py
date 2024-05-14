def lerEntrada(nome):
    # Abre o arquivo para leitura
    file = open(nome, 'r')

    try:
        # Lê a primeira linha do arquivo, que contém os valores de n e m
        string_values = file.readline().split(' ')
        
        # Converte os valores de string para inteiros e os atribui a n e m
        (n, m) = tuple([int(i) for i in string_values])
    except:
        # Retorna um erro se houver um problema ao ler os valores de n e m
        return (False, 'Houve um erro ao ler os valores de n e m', None, None, None, None, None)

    try:
        # Lê a próxima linha do arquivo, que contém os coeficientes da função objetivo
        string_coeficientes = file.readline().split(' ')

        # Converte os coeficientes de string para inteiros e os atribui a lista c
        c = list([int(i) for i in string_coeficientes])

        # Verifica se o número de coeficientes é igual a n
        if len(c) != n:
            return (False, 'O número de coeficientes é diferente do número de variáveis de decisão', None, None, None, None, None)
    except:
        # Retorna um erro se não for possível encontrar a linha dos coeficientes
        return (False, 'Não foi encontrada a linha dos coeficientes', None, None, None, None, None)
        
    # Inicializa as listas para as restrições e os valores de b
    A = []
    b = []
    try:
        # Loop para ler as próximas m linhas, que contêm as restrições
        for j in range(m):
            # Lê uma linha que representa uma restrição
            string_restricao = file.readline().split(' ')

            # Converte os valores da restrição de string para inteiros
            restricao = list([int(i) for i in string_restricao])

            # O último valor na linha representa o valor de b
            b.append(restricao[-1])

            # Remove o valor de b da restrição
            restricao = restricao[:-1]

            # Verifica se o número de valores na restrição é igual a n
            if len(restricao) != n:
                return (False, 'O número de valores na restrição é diferente do número de variáveis de decisão', None, None, None, None, None)
            
            # Adiciona a restrição à lista A
            A.append(restricao)
    except:
        # Retorna um erro se não foram encontradas todas as linhas de restrições
        return (False, 'Não foi encontrada todas as linhas de restrições', None, None, None, None, None)
    
    # Retorna os dados lidos do arquivo de entrada
    return (True, '', n, m, c, A, b)
