def ingresoShow():
    opciones = ["PC", "CONSOLA"]
    while True:
        try:
            show = input("Ingrese con que quiere jugar hoy PC o CONSOLA: ").upper()
            if show not in opciones:
                raise ValueError
        except ValueError:
            print("Opcion no valida, ingrese PC o CONSOLA")
        else:
            break
    return show

def ingresoNombre():
    while True:
        try:
            nombre = input("Ingrese su nombre: ").title()
            if not all(c.isalpha() or c.isspace() for c in nombre):
                raise ValueError
        except ValueError:
            print("Error: ingrese un nombre válido.")
        else:
            break
    return nombre

def ingresoNick():
    while True:
        try:
            nickname = input("Ingrese su nickname: ")
            if " " in nickname:
                raise ValueError
        except ValueError:
            print("Error: ingrese un nickname válido.")
        else:
            break
    return nickname

def deseaComida():
    while True:
        try:
            comida = input("Desea comida? SI o NO: ").upper()
            if comida != "SI" and comida != "NO":
                raise ValueError
        except ValueError:
            print("Error: ingrese SI o NO.")
        else:
            break
    return comida

def combo_validar(combo):
    while combo < 1 or combo > 3:
        print("Opcion no valida, ingrese 1, 2 o 3")
        combo = int(input("Ingrese el combo que desea: 1, 2 o 3: "))
    return combo

def seleccionar_horas():
    lista_horas = [1, 2, 3]
    print("Horas disponibles:", lista_horas)
    while True:
        try:
            horas = int(input("Seleccione la cantidad de horas (1-3): "))
            if horas not in lista_horas:
                raise ValueError
        except ValueError:
            print("Error. Ingrese la cantidad de horas entre 1 y 3.")
        else:
            break
    return horas

def seleccionar_cafeteria(lista_cafe):
    print("Opciones de cafetería:")
    print("1. Cafe + alfajor = $2500")
    print("2. Pancho + gaseosa = $4000")
    print("3. Hamburguesa + papas + gaseosa = $7000")
    opcion = int(input("Seleccione una opción de cafetería (1-3) o 0 para no elegir: "))
    if opcion == 0:
        return "NO", 0
    opcion = combo_validar(opcion)
    if opcion == 1:
        return "Cafe + alfajor", 2500
    elif opcion == 2:
        return "Pancho + gaseosa", 4000
    elif opcion == 3:
        return "Hamburguesa + papas + gaseosa", 7000

def descuento_validar(cuenta):
    descuento = 0
    if cuenta >= 8000 and cuenta < 11500:
        descuento = 2
        cuenta = cuenta - (cuenta * 0.02)
    elif cuenta >= 11500:
        descuento = 4
        cuenta = cuenta - (cuenta * 0.04)
    return descuento, cuenta

def calcular_precio_final(tiempo, comida_precio, turno):
    total = ({1:2500, 2:4000, 3:5550}[tiempo] * (lambda turno: 1.0 if turno=="MAÑANA" else 1.25 if turno=="TARDE" else 1.50)(turno)) + comida_precio
    return total

def ordenar_servicios_por_gasto(ganancias_por_servicio, etiquetas=("PC","CONSOLA","COMIDA")):
    matriz = [(etiquetas[i], gasto) for i, gasto in enumerate(ganancias_por_servicio)]
    matriz_ordenada = sorted(matriz, key=lambda x: x[1], reverse=True)
    print("Servicios ordenados por gasto (servicio, gasto):")
    for etq, gasto in matriz_ordenada:
        print(f"- {etq}: ${gasto:,.0f}".replace(",", "."))
    return matriz_ordenada
        
def ingresoTurno():
    turnos = ["MAÑANA", "TARDE", "NOCHE"]
    while True:
        try:
            turno = input("Ingrese turno: ").upper()
            if turno not in turnos:
                raise ValueError
        except ValueError:
            print("Turno inválido, ingrese MAÑANA, TARDE o NOCHE")
        else:
            break
    return turno

def ocuparMaquina(M):
    while True:
        try:
            pmaq = int(input("Ingrese fila (1-5): "))
            maq = int(input("Ingrese maquina (1-5): "))
            if pmaq < 1 or pmaq > 5:
                print("Fila no valida, ingrese fila entre 1 y 5")
                return ocuparMaquina(M)
            if maq < 1 or maq > 5:
                print("Maquina no valida, ingrese maquina entre 1 y 5")
                return ocuparMaquina(M)
            if M[pmaq-1][maq-1] == 1:
                print("La máquina ya se encuentra ocupada. Seleccione otra máquina a ocupar.")
                return ocuparMaquina(M)
        except ValueError:
            print("Error - No valido")
        else:
            M[pmaq-1][maq-1] = 1
            break
    return M
