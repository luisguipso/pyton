##################### exe 03 ########################
numero1 = int(input("digite o 1º numero: "))
numero1 += int(input("digite o 2º numero: "))
print(numero1)


##################### exe  10 ######################
farenheit = int(input("digite a temperatura em Farenheit: "))
celsius = (5*(farenheit-32))/9
print("graus em celsius: {:.2f}°".format(celsius))

#################### exe 14 #########################
salarioHora = int(input("Salario por hora: "))
horas = int(input("total de horas trabalhadas: "))
salariobruto = salarioHora*horas
print("\nSalarioBruto: ",salariobruto)
print("\nImposto de Renda: ",(salariobruto*7.5)/100)
print("\ninss: ",(salariobruto*8)/100)
print("\nSindicato: ",salariobruto/ 100)
print("\nSalario Liquido: ", salariobruto-(salariobruto*16.5)/100)
