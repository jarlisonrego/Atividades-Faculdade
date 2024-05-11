# EXERCÍCIOS ALGORITMO


# Verificador de maioridade.
def verificador():

    idade = int(input("Digite sua idade:"))
    if idade < 18:
        print("Você é menor de idade!")
    else:
        print("Você é maior de idade!")

if __name__ == "__main__":
    verificador()


# Calculadora de bônus.
def calculadora_bônus():

    valor = int(input("Digite o valor:"))
    bonus = 10 / 100 * valor
    if valor < 2000:
        print("Seu bônus é de:", bonus)
    else:
        print("Não tem direito de bônus")

if __name__ == "__main__":
    calculadora_bônus()


# Calculadora de Média.
def calcular_media():

    nota1 = float(input("Digite sua nota"))
    nota2 = float(input("Digite sua nota"))
    nota3 = float(input("Digite sua nota"))
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")

if __name__ == "__main__":
    calcular_media()


# Calculadora de valor de fatura.
def calcular_fatura():

    minutos = int(input("Digite quantos km de distância:"))
    valor1 = minutos * 0.20
    valor2 = minutos * 0.18
    valor3 = minutos * 0.15

    if minutos < 200:
        print("Você vai pagar: R$", valor1)

    elif 200 <= minutos <= 400:
        print("Você vai pagar: R$", valor2)

    else:
        print("Você vai pagar: R$", valor3)

if __name__ == "__main__":
    calcular_fatura()


# Consulta de preço de produto.
def consulta_preço():

    produto = int(input("Digite a categoria do produto"))

    if produto == 1:
        print("O preço do produto é: R$ 10.00")
    elif produto == 2:
        print("O preço do produto é: R$ 18.00")
    elif produto == 3:
        print("O preço do produto é: R$ 23.00")
    elif produto == 4:
        print("O preço do produto é: R$ 31.00")
    else:
        print("O produto não existe")

if __name__ == "__main__":
    consulta_preço()


# Operações matemática.
def matemática():

    numero1 = float(input("Digite o primeiro número:"))
    numero2 = float(input("Digite o segundo número:"))
    operação = input("Escola uma operação: +, -, * , / ")

    if operação == "+":
        adi = numero1 + numero2
        print("A soma é:", int(adi))

    elif operação == "-":
        sub = numero1 - numero2
        print("A subtração é:", int(sub))

    elif operação == "*":
        multi = numero1 * numero2
        print("A multiplicação é:", int(multi))

    elif operação == "/":
        if numero2 != 0:
            div = numero1 / numero2
            print("A divisão é:", (div))
        else:
            print("Não é possível dividir por 0")

    else:
        print("Operação inválida")

if __name__ == "__main__":
    matemática()

# Como limitar casa decimal.
valor = 123.456789
print(f"O valor formatado é: {valor:.3f}")


# Calculadora de resto de divisão.
def main():
    numero = int(input("Digite um número inteiro entre 100 e 1000"))
    resto = numero % 5

    if numero > 100 and numero < 1000:
        print(f"O resto da divisão de {numero} por 5 é {resto}.")

    else:
        print("Por favor, insira um número inteiro positivo entre 100 e 1000.")

if __name__ == "__main__":
    main()


# Conversor de temperatura.
def main():
    c = input("Digite a temperatura:")

    c_float = float(c)
    Far = 9 / 5 * c_float + 32
    print(f"A temperatura em Fahrenheit é: {Far:.2f}")

if __name__ == "__main__":
    main()


# Número em bits.
def main():
    numero = int(input("Digite um número inteiro entre 10 e 20:"))

    if numero >= 10 and numero <= 20:
        numero_binário = bin(numero)[2:]
        list_bits = [f"{bit}" for bit in numero_binário]
        print(list_bits)

    else:
        print("O número inserido não está dentro do intervalo permitido.")

if __name__ == "__main__":
    main()


# Autenticador.
def autenticador():
    usuário = input("Digite usuário e senha").split()
    # dicionário
    usuarios_senhas = { "usuario1": "senha123", "usuario2": "abc456","usuario3": "123456"}
    login = usuário[0]
    senha = usuário[1]
    key = usuarios_senhas.get(login)

    if senha == key:
        print(f"Login bem-sucedido! Bem-vindo, {login}.")

    else:
        print("Acesso negado. Credenciais inválidas.")

if __name__ == "__main__":
    autenticador()


# Localizador de coordenadas.
def coordenadas():
    coordenadas = input("Digite as coordenadas")
    # coordenadas
    dado = coordenadas.split()
    x_min = dado[0]
    y_min = dado[1]
    x_max = dado[2]
    y_max = dado[3]
    x = dado[4]
    y = dado[5]

    if x_min < x < x_max and y_min < y < y_max:
        print("O ponto está dentro do retângulo.")
    elif x_min <= x <= x_max and y_min <= y <= y_max:
        print("O ponto está tocando a borda do retângulo.")
    else:
        print("O ponto está fora do retângulo.")

if __name__ == "__main__":
    coordenadas()


# Calculadora de empréstimo.
def empréstimo():
    valor = float(input("Digite o Valor do imóvel:"))
    salario = float(input("Digite o valor do salário:"))
    anos = float(input("Digite a quantidade de anos:"))
    prest = valor / (anos * 12)

    if prest <= (30 / 100 * salario):
        print("Empréstimo aprovado!")

    else:
        print("Empréstimo não aprovado!")

if __name__ == "__main__":
    empréstimo()



############## COMANDO WHILE ###############


#Exercício 1: Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
def lancadorFoguete():
    x=10
    while x>=0:
        print(x)
        x = x-1
    print("Fogo!")

if __name__ == "__main__":
    lancadorFoguete()



#Exercício 2: Implemente um programa que, ao solicitar ao usuário inserir um número, calcule e imprima o fatorial desse número. O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio número.
def fatorial():
    numero=int(input("Digite um número:"))
    fatorial=1
    while numero>0:
        fatorial=fatorial*numero
        numero=numero-1
    print(fatorial)

if __name__ == "__main__":
    fatorial()


#Exercício 3: Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
def juros():
    valor=float(input("Digite o valor:"))
    taxa=float(input("Digite a taxa de juros mensal:"))
    n=0
    while n <24:
        mes= valor + (valor *(taxa/100))
        n= n+1
        valor= mes
        print(f"{n}º Mês: {mes:.2f}")
    
    print(f"O total ganho com juros é:{(mes):.2f}")

if __name__=="__main__":
    juros()


#Exercício 4: Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
def primo():
    numero=int(input("Digite um número:"))
    n=2

    if numero==1 or numero==0:
        print("O número",numero,"não é primo")
    if numero==2:
        print("O número",numero,"é primo")
    while n<numero:
        resto=numero%n
        n=n+1
        if resto==0:
            print("O número não é primo")
            break
        else:
            print("O número é primo")
            break

if __name__=="__main__":
    primo()



############# COMANDO FOR #############


#Exercício 1: Analise o desempenho de uma turma de 10 alunos em uma disciplina de linguagem de programação. Seu programa deve receber como entrada 10 números entre 0 e 10, representando as médias finais de cada aluno. Para cada média na lista, o programa deve:
# Adicionar a média à soma total das médias (para posterior cálculo da média da turma).
# Verificar se a média é maior ou igual a 5. Se for, incrementar o contador de alunos aprovados.
# Se a média for menor que 5, incrementar o contador de alunos reprovados.

def AlunosAprovadoReprovado():
    aprovados=0
    reprovados=0
    soma=0
    for media in range(10):
        media=int(input("Digite a nota final do aluno:"))
        soma= soma+media
        if media>=5:
            aprovados= aprovados+1
        else:
            reprovados=reprovados+1

    print("A média da turma é:",(soma/10))
    print(aprovados,"alunos aprovados")
    print(reprovados,"alunos reprovados")
if __name__=="__main__":
    AlunosAprovadoReprovado()


#Exercício 2: Desenvolva um programa que recebe 7 idades de usuários na entrada. Para cada idade, o programa deve imprimir a categoria correspondente de acordo com a seguinte escala: 
#Menor de idade	Menos de 13 anos
#Adolescente	De 13 a 17 anos
#Maior de idade	De 18 a 59 anos
#Idoso	60 anos ou mais

def FaixaEtaria():

    for idade in range(7):
        idade=int(input("Digite a idade:"))

        if idade < 13 :
            print("Menor de idade")
        elif 13 <= idade <= 17:
            print("Adolescente")
        elif 18 <= idade <= 59:
            print("Maior de idade")
        else:
            print("Idoso")

if __name__=="__main__":
    FaixaEtaria()


#Exercício 3: Faça um programa que receba 10 idades, pesos e alturas, calcule e mostre: a média das idades das 10 pessoas, a quantidade de pessoas com peso superior a 90kg e altura inferior a 1,50m, e a porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90m.

def IMC():
    soma=0
    pesoAlt=0
    idadeAlt=0
    for imc in range(10):
        idade=int(input("Digite a idade"))
        altura=float(input("Digite a altura"))
        peso=int(input("Digite o peso"))
#calcular a média de idade.
        soma=soma+idade
        media=soma/10
#verificar pessoas com mais de 90kg e menos 1.5m.
        while peso >90 and altura < 1.50:
            pesoAlt=pesoAlt+1
            break
#verificar pessoas entre 10 e 30 anos com mais de 1.90m.
        while 10<= idade <=30 and altura > 1.9:
            idadeAlt=idadeAlt+1
            cent=idadeAlt*(100/10)
            break
    print("A media de idade das pessoas é",media)
    print(pesoAlt,"pessoas pesam mais de 90kg e tem medem menos de 1,50m")
    print(cent, "% das pessoas entre 10 e 30 anos medem mais de 1,90m")

if __name__=="__main__":
    IMC()


#Exercício 4: Faça um programa que receba um número, calcule e mostre a tabuada desse número.

def tabuada():
    numero=int(input("Digite um número:"))
    n=0
    for n in range(11):
        print(f"{numero} x {n} = {numero*n}")
        n=n+1

if __name__=="__main__":
    tabuada()