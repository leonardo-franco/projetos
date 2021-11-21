from time import sleep


def linha():
    print("\033[1;34m=\033[m" * 40)


def obrigado():
    print("\033[1;33mOBRIGADO POR UTILIZAR NOSSA CALCULADORA\033[m")


linha()
print("\033[1;33mBOAS VINDAS A CALCULADORA FEITA TOTALMENTE EM PYTHON\033[m")

while True:
    linha()
    print(" Para iniciar selecione a operação desejada: \n"
          " [ 0 ] Para sair \n"
          " [ 1 ] Para realizar uma adição \n"
          " [ 2 ] Para realizar uma subtração \n"
          " [ 3 ] Para realizar uma multiplicação \n"
          " [ 4 ] Para realizar uma divisão \n")
    resposta = int(input("Digite aqui sua resposta: "))
    linha()
    if resposta == 0:
        obrigado()
        sleep(2)
        break
    elif resposta == 1:
        vezes = int(input("Você quer realizar a soma de quantos números? "))
        linha()
        soma = 0
        for c in range(0, vezes):
            n = int(input(f"Digite o {c + 1}° número: "))
            linha()
            soma = soma + n
        print("Calculando...")
        sleep(2)
        print(f"A soma de todos os {vezes} números apresentados é de: {soma} ")
        linha()
        resposta2 = str(input("Você quer continuar o programa? [S/N]: "))
        if resposta2 in "Nn" or resposta2 in "naonotnãoNAONOTNÃO":
            linha()
            obrigado()
            break
    elif resposta == 2:
        n1 = int(input("Digite o 1° número: "))
        linha()
        n2 = int(input("Digite o 2° número: "))
        sub = n1 - n2
        linha()
        print("Calculando...")
        sleep(2)
        print(f"A subtração de {n1} - {n2} é de {sub}. ")
        resposta3 = str(input("Você quer continuar o programa? [S/N]: "))
        if resposta3 in "Nn" or resposta3 in "naonotnãoNAONOTNÃO":
            linha()
            obrigado()
            break
    elif resposta == 3:
        vezes = int(input("Você deseja realizar a multiplicação de quantos números? "))
        linha()
        mul = 1
        for c in range(0, vezes):
            n = int(input(f"Digite o {c + 1}° número: "))
            linha()
            mul = mul * n
        print("Calculando...")
        sleep(2)
        print(f"A multiplicação de todos os números apresentados é de {mul}")
        resposta5 = str(input("Você quer continuar o programa? [S/N]: "))
        if resposta5 in "Nn" or resposta5 in "naonotnãoNAONOTNÃO":
            linha()
            obrigado()
            break
    elif resposta == 4:
        n1 = int(input("Digite o 1° número: "))
        linha()
        n2 = int(input("Digite o 2° número: "))
        linha()
        div = n1 / n2
        print("Calculando...")
        sleep(2)
        print(f"A divisão entre {n1} e {n2} é de {div}. ")
        resposta6 = str(input("Você quer continuar o programa? [S/N]: "))
        if resposta6 in "Nn" or resposta6 in "naonotnãoNAONOTNÃO":
            linha()
            obrigado()
            break
    else:
        print("	\033[1;31mPOR FAVOR DIGITE UM VALOR VÁLIDO\033[m")
        sleep(1)
