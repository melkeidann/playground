import re
import sys

entrada = input('Digite o CPF que deseja validar: ')
# Apenas números de 0 a 9 serão aceitos, o resto será substitído por ''
cpf_recebido = re.sub(
    r'[^0-9]',
    '',
    entrada
)

# Verificação de 11 dígitos
if len(cpf_recebido) != 11:
    print('CPF inválido. Deve conter 11 dígitos numéricos.')
    sys.exit()
    
# Impedindo o erro do código de validar CPFs como "11111111111"
# Se a entrada for igual ao primeiro índice da entrada * o tamanho da entrada, invalida o cpf (str)
entrada_repetida = cpf_recebido == cpf_recebido[0] * len(cpf_recebido)
if entrada_repetida:
    print('CPF inválido. Todos os caracteres são iguais.')
    sys.exit()

# Penúltimo dígito do CPF
# O cáculo deve ser feito com os 9 primeiros dígitos
nove_digitos = cpf_recebido[:9]
contador1 = 10

# Transforma cada digito em int e multiplica pelo contador a começar de 10, somando cada resultado
# A cada "giro" o contador perde -1
resultado_digito1 = 0
for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador1
    contador1 -= 1

# Soma total * 10 e depois o resto dividido por 11
# Se o resto for menor ou igual a 9, mantém, se for maior, vira 0
digito1 = (resultado_digito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

# Calculando o último dígito do CPF
# O cáculo também deve ser feito com base nos 9 primeiros dígitos + digito 1
dez_digitos = nove_digitos + str(digito1)
contador2 = 11

resultado_digito2 = 0
for digito in dez_digitos:
    resultado_digito2 += int(digito) * contador2
    contador2 -= 1
digito2 = (resultado_digito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

# Unindo todas as partes, 9 primeiros dígitos, penúltimo dígito gerado e último dígito gerado
cpf_formado = f'{nove_digitos}{digito1}{digito2}'

if cpf_recebido == cpf_formado:
    print(f'O CPF: {cpf_recebido[:3]}.{cpf_recebido[3:6]}.{cpf_recebido[6:9]}-{cpf_recebido[9:]}, é válido.')
else:
    print('CPF inválido.')
