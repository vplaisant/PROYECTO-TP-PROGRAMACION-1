comprobante = 1
for i in range(3):
    nombre = input("Ingrese su nombre: ")
    nickname = input("Ingrese su nickname: ")
    show = input("Ingrese con que quiere jugar PC o CONSOLA : ")
    show = show.upper()
    descuento = 0
    combosi = False
    while show != "PC" and show != "CONSOLA":
        print("Opcion no valida, ingrese PC o CONSOLA")
        show = input("Ingrese con que quiere jugar hoy PC o CONSOLA: ")
        show = show.upper()
    tiempo = int(input("Ingrese cuantas horas quiere jugar de 1 a 3: "))
    while tiempo < 1 or tiempo > 3:
        tiempo = ("Opcion no valida, ingrese de 1 a 3 horas")
    if tiempo == 1:
        cuenta = 2500
    elif tiempo == 2:
        cuenta = 4000
    elif tiempo == 3:
        cuenta = 5550
    comida = input("Desea comida? SI o NO: ")
    comida = comida.upper()
    while comida != "SI" and comida != "NO":
        print("Opcion no valida, ingrese SI o NO")
        comida = input("Desea comida? SI o NO: ")
        comida = comida.upper()
    if comida == "SI":
        combosi = True
        print("COMBO 1: Cafe + alfajor = $2500")
        print("")
        print("COMBO 2: Pancho + gaseosa = $4000")
        print("")
        print("COMBO 3: Hamburguesa + papas + gaseosa = $7000")
        combo = int(input("Ingrese el combo que desea: 1, 2 o 3: "))
        while combo < 1 or combo > 3:
            print("Opcion no valida, ingrese 1, 2 o 3")
            combo = int(input("Ingrese el combo que desea: 1, 2 o 3: "))
        if combo == 1:
            cuenta = cuenta + 2500
        elif combo == 2:
            cuenta = cuenta + 4000
        elif combo == 3:
            cuenta = cuenta + 7000
    if cuenta >= 8000 and cuenta < 10000:
        print("Descuento del 2% por ser gastar mas de $8000")
        descuento = 2
        cuenta = cuenta - (cuenta * 0.02)
    if cuenta >= 10000:
        print("Descuento del 4% por ser gastar mas de $10000")
        descuento = 4
        cuenta = cuenta - (cuenta * 0.04)
    print("------------------------------------------------------------")
    print("FACTURA",comprobante)
    print("Nombre: Cibercafe", )
    print("CUIT: 20-12345678-9")
    print("Direccion: av rivadavia 4567 ", )
    print("Telefono: 011-12345678")
    print("")
    print("Nombre del cliente: ", nombre)
    print("Nickname: ", nickname)
    print("servicio utilizado: ", show)
    print("Tiempo utilizado: ", tiempo, "horas")
    print("Total a pagar: $", cuenta)
    if combosi == True:
        print("Combo elegido: ", combo)
    if descuento > 0:
        print("Descuento aplicado: ", descuento, "%")
    print("")
    print("Gracias por su visita, vuelva pronto")
    print("------------------------------------------------------------")
    print("")
    comprobante = comprobante + 1