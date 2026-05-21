def h(x):
    if x > 0:
        return 1
    elif x <= 0:
        return 0

def funcaoPesos(pesos, taxa, erro, vetorErro):
    with open('pesos.txt', 'a') as f:
        f.write("--- Atualização de Pesos ---\n")
        for i in range(len(pesos)):
            pesos[i] = pesos[i] + taxa * erro * vetorErro[i]
            f.write(f"O peso {i} agora é {pesos[i]}.\n")

# Função principal do perceptron.
def perceptron(matriz, pesos, taxa):
    breakpoint = False # Boolean que verifica se há necessidade de fazer outro ciclo.
    ciclo = 1 # Indica o primeiro ciclo.
    n_saida = len(matriz[0]) - 1 # Variável feita para rapidamente acessar o índice do vetor que indica o valor previsto de cada exemplo.

    # A função é um while pois irá se repetir até poder garantir que todos os pesos se encaixaem corretamente na matriz.
    while not breakpoint:
        print(f"CICLO {ciclo}")
        erro = False # Resetamos a verificação a cada início de ciclo

        for i in range(len(matriz)): # Aqui ele adentra a matriz, iniciando o ciclo. Este for percorre todos os exemplos.

            funcao = pesos[0] # O início da função h(theta0 * x0 + theta1 * x1 + ... + thetan * xn)

            for j in range(1, n_saida): # Este for percorre o vetor de cada exemplo, apenas até o penúltimo elemento, já que o último é o y.

                funcao += pesos[j] * matriz[i][j] # Esta linha adiciona cada termo na função h.

            if h(funcao) != matriz[i][n_saida]:
                print(f"Foi encontrado um erro no exemplo {i}.\n")
                erro = True

                # Foi encontrado um erro, que agora será sanado, os pesos serão mudados.
                # Primeiro, definimos a variável E(x), x indicando o exemplo onde o erro foi encontrado (no caso, matriz[i]).
                f_erro = matriz[i][n_saida] - h(funcao)
                funcaoPesos(pesos, taxa, f_erro, matriz[i])
        
        if not erro:
            breakpoint = True
            print("O Perceptron foi treinado com sucesso.\n")
     
        ciclo +=1
        if ciclo > 1000: # Uma trava de segurança para não rodar infinito se os dados não forem linearmente separáveis
            print("Limite de ciclos atingido (Dados podem não ser linearmente separáveis).")
            break

def preparador():

    n_exemplos = int(input("Insira aqui o número de exemplos: "))
    n_entradas_total = int(input("Insira o n° de atributos + o valor de Y (ex: 2 atributos + Y = 3): "))
    matriz = []
    for i in range(n_exemplos):
        numero_atributos = input("Insira aqui o número inteiro de cada vetor.\n(Por exemplo, se o vetor for [0, 1, 1], insira 011): ")
        while len(numero_atributos) != n_entradas_total:
            numero_atributos = input("O número inserido não corresponde com o número de atributos.\nInsira o número novamente: ")
            
        numero_vetor = [int(digit) for digit in str(numero_atributos)]
        numero_vetor.insert(0, 1) # insere-se o bias x0 = 1 (usado apenas no conserto dos thetas) no começo do vetor de atributos
        matriz.append(numero_vetor)

    numero_pesos = input(f"Insira o vetor de pesos (deve conter exatamente {n_entradas_total} dígitos): ")
    while len(numero_pesos) != n_entradas_total:
        numero_pesos = input("Tamanho incorreto. Insira novamente: ")
        
    vetor_pesos = [int(digit) for digit in str(numero_pesos)]
    taxa_aprendizagem = float(input("Insira aqui a taxa de aprendizagem: \n").replace(",", "."))

    print("Esta é a matriz dos exemplos (com o bias inserido na coluna 0): ")
    for linha in matriz:
        print(linha, end="\n")
    print(f"Este é o vetor dos pesos inicial:\n{vetor_pesos}.")
    print(f"Esta é a taxa de aprendizagem:\n{taxa_aprendizagem}\n")

    return(matriz, vetor_pesos, taxa_aprendizagem)

matriz, pesos, taxa = preparador()
perceptron(matriz, pesos, taxa)