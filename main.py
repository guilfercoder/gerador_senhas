import random
import string

print("========Gerador de Senhas do Guizão========")

while True:

    tamanho = int(input("Digite o tamanho da senha: "))

    qntd_letras =  int(input("Digite a quantidade de letras da senha: "))
    qntd_numeros = int(input("Digite a quantidade de numeros da senha: "))
    qntd_especiais = int(input("Digite a quantidade de especiais da senha: "))

    soma = qntd_letras + qntd_numeros + qntd_especiais

    if soma != tamanho:
        print(f"\n ERRO! A soma {soma}, não corresponde ao informado {tamanho}.")
        print("Por favor, tente novamente.")
    else:
        letras = random.choices(string.ascii_letters, k=qntd_letras)
        numeros = random.choices(string.digits, k=qntd_numeros)
        especiais = random.choices(string.ascii_letters, k=qntd_especiais)

        senha_lista = letras + numeros + especiais

        random.shuffle(senha_lista)

        senha = "".join(senha_lista)

        print(f"\n Sua senha gerada foi: {senha}")

    repetir = input("Deseja repetir? [S/N]: ").lower()
    if repetir == "n":
        print("Parabéns pela nova senha!")
    if repetir != "S":
        print("\n Parabéns pela senha!")

