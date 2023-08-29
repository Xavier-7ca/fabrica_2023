#EXERCICIO Nº1 IDADE E CNH

idade = input("Digite a sua idade e veja se consegue tirar a carteira de motorista: ")
try:
    idade = int(idade)
    if idade >= 18:
        print("A sua idade é {} e você já pode tirar a carteira de motorista".format(idade))
    else:
        print("A sua idade é {} e você ainda é menor de idade e não pode tiar a sua carta".format(idade))
except:
    print("Insira um número")

#EXERCÍCIO Nº 2 VELOCIDADE E MULTA

velocidade = (input("Qual a velocidade do veículo?"))
try:
    velocidade = int(velocidade)
    multa = ((velocidade -80) * 7)
    if velocidade < 81:
        print("A velocidade foi de: {} e você não recebeu nenhuma multa".format(velocidade))
    elif:
        velocidade >= 81:
        print("A velocidade foi de: {} e o veículo receberá uma multa de: {}".format(velocidade, multa))
except:
    print("Digite uma velocidade válida")
