# Exemplo de modificação para o desafio:
pontos = 100
while tentativas > 0:
    chute = int(input("Chute um número: "))
    if chute == numero_secreto:
        print(f"Acertou! Pontuação: {pontos}")
    else:
        pontos -= 10
