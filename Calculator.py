print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Raiz Quadrada")

opcao = input("Escolha uma opção: ")
if opcao == '1':
    a = input("entre com o primeiro valor: ")
    a = int(a)
    b = input("entre com o segundo valor: ")
    b = int(b)
    c = a + b
    print("\nresultado: ",c)
elif opcao == '2':
    a = input("entre com o primeiro valor: ")
    a = int(a)
    b = input("entre com o segundo valor: ")
    b = int(b)
    c = a - b
    print("\nresultado: ",c)
elif opcao == '3':
    a = input("entre com o primeiro valor: ")
    a = int(a)
    b = input("entre com o segundo valor: ")
    b = int(b)
    c = a * b
    print("\nresultado: ",c) 
elif opcao == '4':
    a = input("entre com o primeiro valor: ")
    a = int(a)
    b = input("entre com o segundo valor: ")
    b = int(b)
    c = a / b
    print("\nresultado: ",c)

elif opcao == '5':
        a = input("Digite o valor: ")
        a = int(a)
        c = a ** 0.5
    
        print("\nresultado: ",c)
        
