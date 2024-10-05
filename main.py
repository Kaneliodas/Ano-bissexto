#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = float(input("Me diga um ano: "))
confirma = ano % 4
if confirma == 0:
    print("Este ano é bissexto.")
else:
    print("Este ano não é bissexto")
