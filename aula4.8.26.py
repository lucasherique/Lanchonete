#EXERCICIO LANCHONETE
erro = "Opção Inválida!"
resp = "s"
total = 0

while resp == "s":
    print("Bem vindo a lanchonete!\n")

    print('1. Lanches')
    print('2. Bebidas')
    print('3. Sobremesa')

    opc = int(input("Escolha uma opção: "))

    match opc:
        case 1:
            print("1. Cachorro-quente: R$15,00")
            print("2. Hamburguer: R$20,00")
            pedido = int(input("Escolha seu lanche: "))
            qt = int(input("Qual a quantidade? "))
            match pedido:
                case 1:
                    valor = qt * 15
                case 2:
                    valor = qt * 20
                case _:
                    print(erro)
        case 2:
            print("1. Refrigerante: R$ 5,00")
            print("2. Suco natural: R$ 10,00")
            pedido = int(input("Escolha a sua bebida: "))
            qt = int(input("Qual a quantidade? "))
            match pedido:
                case 1:
                    valor = qt * 5
                case 2:
                    valor = qt * 10
                case _:
                    print(erro)
        case 3:
            print("1. Sorvete: R$ 12,00")
            print("2. Açai: R$ 15,00")
            pedido = int(input("Escolha a sua sobremesa: "))
            qt = int(input("Qual a quantidade? "))
            match pedido:
                case 1:
                    valor = qt * 12
                case 2:
                    valor = qt * 15
                case _:
                    print(erro)
        case _:
            print(erro)
    if 1 <= opc <= 3 and 1 <= pedido <= 2:
        total += valor
        resp = input("Deseja continuar? (s ou n): ")

if total != 0:
    print(f"Seu pedido custa R${total:.2f}")





