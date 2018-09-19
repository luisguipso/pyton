################### exe 01 #####################
#funcao
def somar():


numero = int(input("Digite um numero: "))
if(numero > 0):
    print("positivo")
elif(numero < 0):
    print("negativo")
else:
    print("numero neutro")

################## exe 02 ######################
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
if(numero1>numero2):
    print(numero1)
elif(numero1<numero2):
    print(numero2)


################# exe 07 ########################
notaProva  = int(input("Digite a nota da prova: "))
notaTrabalho = int(input("Digite a nota do trabalho: "))

if((notaProva+notaTrabalho)/2 >= 60):
    print("aprovado")
else:
    print("reprovado")

###################### exe 10 #######################


controle = 10
while(controle > 0):
    print("\n== Menu de Opções ==")
    print("1. Somar dois numeros")
    print("2. Potencia")
    print("3. Raiz")
    controle = int(input("Digite o numero da operação:"))
    if(controle == 1):
        somar()
    elif(contole == 2):
        potencia()
    elif(controle == 3):
        raiz()
    else:
        controle = 0
        break
