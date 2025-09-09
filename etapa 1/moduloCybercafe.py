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
    if cuenta >= 8000 and cuenta < 10000:
        descuento = 2
        cuenta = cuenta - (cuenta * 0.02)
    elif cuenta >= 10000:
        descuento = 4
        cuenta = cuenta - (cuenta * 0.04)
    return descuento, cuenta

def calcular_precio_final(tiempo, comida_precio, turno):
    total = ({1:2500, 2:4000, 3:5550}[tiempo] * (lambda turno: 1.0 if turno=="MAÑANA" else 1.25 if turno=="TARDE" else 1.50)(turno)) + comida_precio
    return total


def ordenar_servicios_por_gasto(ganancias_por_servicio):
    matriz = []
    for i in range(len(ganancias_por_servicio)):
        matriz.append([i+1, ganancias_por_servicio[i]])
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if matriz[i][1] > matriz[j][1]:
                matriz[i], matriz[j] = matriz[j], matriz[i]
    print("Matriz de servicios ordenados por gasto (nro. de servicio, gasto):")
    for fila in matriz:
        print(fila)
        
def turno_validar(turno):
    while turno not in ["MAÑANA", "TARDE", "NOCHE"]:
        print("Turno inválido, ingrese MAÑANA, TARDE o NOCHE")
        turno = input("Ingrese turno: ").upper()
    return turno
