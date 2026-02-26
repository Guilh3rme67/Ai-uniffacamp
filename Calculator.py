print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Raiz Quadrada")

opcao = input("Escolha uma opção: ")

if opcao == '1':
    a = int(input("Entre com o primeiro valor: "))
    b = int(input("Entre com o segundo valor: "))
    c = a + b
    print("\nResultado:", c)

elif opcao == '2':
    a = int(input("Entre com o primeiro valor: "))
    b = int(input("Entre com o segundo valor: "))
    c = a - b
    print("\nResultado:", c)

elif opcao == '3':
    a = int(input("Entre com o primeiro valor: "))
    b = int(input("Entre com o segundo valor: "))
    c = a * b
    print("\nResultado:", c)

elif opcao == '4':
    a = int(input("Entre com o primeiro valor: "))
    b = int(input("Entre com o segundo valor: "))
    
    if b == 0:
        print("\nErro: divisão por zero não é permitida!")
    else:
        c = a / b
        print("\nResultado:", c)

elif opcao == '5':
    a = int(input("Digite o valor: "))
    
    if a < 0:
        print("\nErro: não existe raiz real de número negativo!")
    else:
        c = a ** 0.5
        print("\nResultado:", c)

else:
    print("\nOpção inválida!")
