# Defina a palavra secreta: Escolha uma palavra que será o objetivo do jogo.
# Permita a entrada de uma letra: O programa deve solicitar ao usuário que digite uma única letra.
# Verifique a presença da letra: Compare a letra digitada com cada uma das letras da palavra secreta.
# Exiba o resultado:
#   Se a letra digitada estiver presente na palavra secreta, mostre essa letra na sua respectiva posição dentro de uma representação
#     da palavra. As letras ainda não descobertas devem ser representadas por algum caractere como um asterisco (*).
#   Se a letra digitada não estiver na palavra secreta, exiba um asterisco (*).
# Conte as tentativas: Mantenha um registro do número de vezes que o usuário tentou adivinhar uma letra
# (adiconal: quero prever se letra digitada não for uma letra, quero prever se foi digitado só UMA letra e quero prever caixa alta)


palavra_secreta = 'palavrasecreta'
letras_ok = ''
tentativas = 0

while True:

    letra = input('Digite uma letra: ').lower() 
    tentativas += 1

    if len(letra) > 1 or not letra.isalpha():
        print('Você digitou mais de uma letra, ou algo que não era uma letra.')
        continue

    if letra in palavra_secreta:
        letras_ok += letra
    
    palavra_formada = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_ok:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra completa: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Fim, você acertou com', tentativas, 'tentativas.')
        print('A palavra era: ', palavra_secreta)
        break

