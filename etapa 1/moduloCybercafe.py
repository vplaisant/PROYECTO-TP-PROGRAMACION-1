def show_validar(show):
    while show != "PC" and show != "CONSOLA":
        print("Opcion no valida, ingrese PC o CONSOLA")
        show = input("Ingrese con que quiere jugar hoy PC o CONSOLA: ").upper()
    return show

def tiempo_validar(tiempo):
    while tiempo < 1 or tiempo > 3:
        print("Opcion no valida, ingrese de 1 a 3 horas")
        tiempo = int(input("Ingrese cuantas horas quiere jugar de 1 a 3: "))
    return tiempo

def comida_validar(comida):
    while comida != "SI" and comida != "NO":
        print("Opcion no valida, ingrese SI o NO")
        comida = input("Desea comida? SI o NO: ").upper()
    return comida

def combo_validar(combo):
    while combo < 1 or combo > 3:
        print("Opcion no valida, ingrese 1, 2 o 3")
        combo = int(input("Ingrese el combo que desea: 1, 2 o 3: "))
    return combo

def seleccionar_horas(lista_horas):
    print("Horas disponibles:", lista_horas)
    horas = int(input("Seleccione la cantidad de horas (1-3): "))
    horas = tiempo_validar(horas)
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


"""def liberarMaquina(M):
    pmaq = int(input("Ingrese fila: "))
    maq = int(input("Ingrese maquina: "))
    while M[pmaq-1][maq-1] == 0:
        print("La máquina no está ocupada. Seleccione una maquina ocupada para liberarla.")
        pmaq = int(input("Ingrese fila: "))
        maq = int(input("Ingrese maquina: "))
    M[pmaq-1][maq-1] = 0
    return M"""
