menu = """ 
[d] depositar
[s] sacar
[e] extrato
[q] salir
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcion = input(menu)

    if opcion == "d":
        valor = float(input("informe el valor del deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f} \n"

        else:
            print("Operacion fallo: el valor informado es invalido.")

    elif opcion == "s":
        valor = float(input("informe el valor de saque: "))
        excedio_saldo = valor > saldo
        excedio_limite = valor > limite
        excedio_saques = numero_saques >= LIMITE_SAQUES
        if excedio_saldo:
            print("opcion fallo, no tiene saldo suficiente")
        elif excedio_limite:
            print("opcion fallo, el valor del saque excede el limite")
        elif excedio_saques:
            print("opcion fallo, numero de saques excede el limite")
        elif excedio_saques:
            print("opcion fallo, numero de saques excede el limite")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.f2}\n"
            numero_saques += 1

        else:
            print("Operacion fallo, el valor informado es invalido")

    elif opcion == "e":
        print("\n============== EXTRATO =================")
        print("No fueron realizados ningunos movimiento" if not extrato else extrato)
        print(f"\n Saldo: R$ {valor:.2f}\n")
        print("\n========================================")
    elif opcion == "q":
        break
    else:
        print("opcion invalida")
