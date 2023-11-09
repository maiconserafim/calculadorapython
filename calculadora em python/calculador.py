def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Divisão por zero não é permitida"
    return x / y

while True:
    print("Opções:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Escolha a operação (1/2/3/4/5): ")

    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", adicao(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5).")
