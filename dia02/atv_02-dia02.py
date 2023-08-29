#EXERCÍCIO Nº 2 VELOCIDADE E MULTA

velocidade = (input("Qual a velocidade do veículo? "))
try:
    velocidade = int(velocidade)
    multa = ((velocidade -80) * 7)
    if velocidade < 80:
        print("A velocidade foi de: {} km/h e você não recebeu nenhuma multa".format(velocidade))
    elif velocidade == 80:
        print("CUIDADO! Velocidade no limite permitido!")
    else:
        velocidade >= 80
        print("A velocidade foi de: {} km/h e o veículo receberá uma multa de: R${} reais".format(velocidade, multa))
except:
    print("Digite uma velocidade válida")