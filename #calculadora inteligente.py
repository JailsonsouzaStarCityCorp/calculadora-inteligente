#calculadora inteligente

while True:
    print("=== Calculadora inteligente (Jailson) ===")

    # Entrada de dados do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Menu de operações
    print("\nEscolha a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    opcao = input("Digite o número da operação desejada: ")

    # Condicionais para realizar a operação
    if opcao == "1":
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
    elif opcao == "2":
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")
    elif opcao == "3":
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")
    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("\nErro: divisão por zero não é permitida!")
    else:
        print("\nOpção inválida!")

    # Perguntar se deseja continuar
    repetir = input("\nDeseja realizar outra operação? (s/n): ")
    if repetir.lower() != "s":
        print("Encerrando a calculadora... Obrigado por ultilizar nosso serviço!")
        break