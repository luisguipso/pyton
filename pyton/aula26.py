print("Hello World")
#Este é um comentário
print("\nNo python nao utilizamos indicadores de fim de linha ")
#\nfunciona no phyton

"""
Esse é
um comentário em bloco
"""

'''
Esse
também
'''

#variaveis nao tem tipo especificado

num = 10
num = "Luis"
num = 10.5
#pro pyton está tudo certo

# uma das formas de apresentar dados
print("\nresultado: ", num, ", certo?")

# mas a virgula esta no luga errado

# formatar String
print("O resultado é {}, certo?".format(num))

nome = "Luis"

print("{} tem uma caneta que vale {}".format(nome, num))

#prioridade de operadores
# potencia **
# multiplicação * e divizão /
# soma + e subtração -


#calculando raiz

num = 9**1/2 # isso é 4,5
num = 9**(1/2) # isso é a raiz = 3
num = 256**(1/8) #raiz de grau 8


#Condicionais
if(num % 2 ==0): # o : delimita o fim da linha
    print("O numero {} é par".format(num))
    #coisas do if ficam identadas
    if(True):
        #Cuide da identação!
        print("True e False tem letra inicial maiuscula")
    #fim do IF interno
#fim do if externo
else:
    print("o numero {} é impar!".format(num))


#Toda entrada do input é String
num = input("Digite um numero: ") #retona Srings concatenadas exe: 10 1010 101010 10101010
print("\n")

#converter para int() ou float()
num = int(num)

i = 0
while(i<=10):
    res = i*num
    print("{} x {} = {}".format(num, i, res))
    # Nao existe i++ aqui
    i += 1 # mesma coisa = i = i+1
# the end of while

#listas, vetores, arrays

# Vetor vazio
vetor = []

#adicionar algo
vetor.append(10)
vetor.append(9)
vetor.append(8)

#crinado um vetor ja preenchido
vetor = [10,5,19,53,48,9]

#Cria vetor vazio com tamanho N

vetor = [""] * 10  #vetor de 10 posicoes
vetor[0] = 19
vetor[1] = 5
vetor [9] = 12


#Pedindo valores para o usuario
vetor = [""] * 4
i = 0

#len calcula o tamanho de algo
while(i<len(vetor)):
    #Pede um valor, converte pra int e armazena na posição i
    vetor[i] = int(input("Numero:"))

    #incremento da posicao
    i = i +1 # ou i += 1

# mostrando o vetores
print("vetor = {}".format(vetor))

#percorrendo vetor com FOREACH

for x in vetor:
    print("valor da posição do vetor: {}".format(x))
