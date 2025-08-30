"""Leia duas variáveis inteiras chamada numero1 e outra chamada numero2. Realize a
soma, subtração, multiplicação e divisão entre esses números e atribua os resultados
a variáveis correspondentes."""

numero1 = int(input('Insira o 1° número: '))
numero2 = int(input('Insira o 2° número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f'Números: {numero1}, {numero2}')
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')