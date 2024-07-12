# Exercicio 001: Crie um programa que imprima "Olá, mundo!" na tela.

'''
print("Olá, mundo!")
'''

# Exercicio 002: Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

'''
nome = input("Qual é seu nome? ")
print(f"Olá {nome}, seja bem-vindo(a) ao Python!")
'''

# Exercicio 003: Crie um programa que leia dois números e mostre a soma entre eles.

'''
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

soma = numero1 + numero2

print(f"A soma entre {numero1} e {numero2} é {soma}")
'''

# Exercicio 004: Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

'''
palavra = (input("Digite uma palavra: "))
print(f"O tipo de {palavra} é {type(palavra)}")
print(f"Só tem espaços? {palavra.isspace()}")
print(f"É um número? {palavra.isnumeric()}")
print(f"É alfabetico? {palavra.isalpha()}")
print(f"É alfanúmerico? {palavra.isalnum()}")
print(f"Esta em maiúsculas? {palavra.isupper()}")
print(f"Esta em minúsculas? {palavra.islower()}")
print(f"Esta capitalizada? {palavra.istitle()}")
'''

# Exercicio 005: Crie um programa que leia um número e mostre na tela seu antecessor e sucessor.

'''
numero = int(input("Digite um número: "))

print(f"O antecessor de {numero} é {numero - 1} e o sucessor {numero + 1}")
'''

# Exercicio 006: Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.

'''
numero = int(input("Digite um número: "))

print(f"O dobro de {numero} é {numero * 2}")
print(f"O triplo de {numero} é {numero * 3}")
print(f"A raiz quadrada de {numero} é {numero ** (1/2)}")
'''

# Exercicio 007: Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

'''
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A sua media é {media}")
'''

# Exercicio 008: Crie um programa que converte metros em centímetros e milimetros.

'''
valor = float(input("Digite um valor em metros: "))

print(f"O valor em centímetros é {valor * 100} cm")
print(f"O valor em milimetros é {valor * 1000} mm")
''' 

# Exercicio 009: Crie um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

'''
numero = int(input("Digite um número: "))

print(f"O {numero} multiplicado por 1 é {numero * 1}")
print(f"O {numero} multiplicado por 2 é {numero * 2}")
print(f"O {numero} multiplicado por 3 é {numero * 3}")
print(f"O {numero} multiplicado por 4 é {numero * 4}")
print(f"O {numero} multiplicado por 5 é {numero * 5}")
print(f"O {numero} multiplicado por 6 é {numero * 6}")
print(f"O {numero} multiplicado por 7 é {numero * 7}")
print(f"O {numero} multiplicado por 8 é {numero * 8}")
print(f"O {numero} multiplicado por 9 é {numero * 9}")
print(f"O {numero} multiplicado por 10 é {numero * 10}")
'''

# Exercicio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

'''
valor = float(input("Quanto dinheiro você tem na carteira?\n"))
cotacao = float(input("Qual é a cotação do dolar?\n"))

dolar = valor / cotacao

print(f"Com {valor} reais, você pode comprar {dolar} dólares")
'''

# Exercicio 011: Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2.

'''
largura = float(input("Qual é a largura da parede?\n"))
altura = float(input("Qual é a altura da parede?\n"))

area = largura * altura
tinta = area / 2

print(f"Para pintar a parede de {area} m2, você precisará de {tinta} litros de tinta")
'''

# Exercicio 012: Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

'''
preco = float(input("Qual é o valor do produto?\n"))

desconto = preco * 0.05
novoPreco = preco - desconto

print(f"O valor do produto com desconto de 5% é {novoPreco}")
'''

# Exercicio 013: Crie um programa que leia um salario e mostre seu novo, com 15% de aumento.

'''
salario = float(input("Qual é o valor do seu salaário?\n"))

aumento = salario * 0.15
novoSalario = salario + aumento

print(f"O valor do seu novo salaário com aumento de 15% é {novoSalario}")
'''

# Exercicio 014: Crie um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

'''
celcius = float(input("Qual é a temperatura em graus Celsius?\n"))

fahrenheit = ((celcius * 9) / 5) + 32

print(f"A temperatura em graus Fahrenheit é {fahrenheit}")
'''

# Exercicio 015: Crie um programa que pergunta a quantidade de km percorridos por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

'''
km = float(input("Quantos km foram percorridos?\n"))
dias = int(input("Por quantos dias o veículo ficou alugado?\n"))

preco = (km * 0.15) + (dias * 60)

print(f"O valor total a ser pago é de {preco}")

'''

# Exercicio 016: Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.

'''
numero = float(input("Digite um número real: "))

porcao = int(numero)

print(f"A porção inteira de {numero} é {porcao}")
'''

# Exercicio 017: Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.

'''
catetoOposto = float(input("Qual é o valor do cateto oposto?\n"))
catetoAdjacente = float(input("Qual é o valor do cateto adjacente?\n"))

hipotenusa = (catetoOposto ** 2) + (catetoAdjacente ** 2)

hipotenusa = hipotenusa ** 0.5

print(f"O valor da hipotenusa é {hipotenusa}")
'''

# Exercicio 018: Crie um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

'''
import math

angulo = float(input("Qual é o angulo que deseja saber?\n"))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O valor do seno, cosseno e tangente de {angulo} sao {seno}, {cosseno} e {tangente}")
'''

# Exercicio 019: Crie um programa para um professor que sorteia um dos quatros alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''
import random

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])

print(f"O aluno que irá apagar o quadro é {escolhido}")
'''

# Exercicio 020: Crie um programa para o mesmo professor mas que sorteie a ordem de apresentação de trabalhos. Faca um programa que leie o nome dos 4 alunos e mostre a ordem sorteada.

'''
import random

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

escolhido = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(escolhido)

print(f"Ordem de apresentação: {escolhido}")
'''

# Exercicio 021: Crie um programa que abra e reproduza o audio de um arquivo MP3.

'''
import pygame

pygame.init()
pygame.mixer.music.load('nomeDoArquivo.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
'''

# Exercicio 022: Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas; o nome com todas as letras minúsculas; quantas letras ao todo(sem considerar os espacos); quantas letras no primeiro nome.

'''
nome = input("Qual é o seu nome completo?\n")

print(f"Seu nome em letras maiúsculas é {nome.upper()}")
print(f"Seu nome em letras minúsculas é {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")
'''

# Exercicio 023: Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

'''

numero = int(input("Digite um número de 0 a 9999:\n"))

numero = str(numero)

print("Analisando o seu número...")
print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")
'''