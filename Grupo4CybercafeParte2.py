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

def calcular_precio_final(tiempo, comida_precio):
    if tiempo == 1:
        precio_hora = 2500
        total = precio_hora + comida_precio
    elif tiempo == 2:
        precio_hora = 4000
        total = precio_hora + comida_precio
    elif tiempo == 3:
        precio_hora = 5550
        total = precio_hora + comida_precio
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


integrantes = ["Lautaro Giampaoli", "Victoria Eugenia Plaisant", "Juliana Rivas", "Navarro Lucas Sebastian"]
print("Integrantes del grupo:", integrantes)

cibercafe = ["Botas", "Cibercafe Botas", "Av Rivadavia 4567", "011-12345678", "20-12345678-9"]
lista_horas = [1, 2, 3]
lista_cafe = [1, 2, 3]
ganancias_por_servicio = [0, 0, 0]
lista_ganancias = []

comprobante = 1
print("------------------------------------------------------------")
for i in range(3):
    cliente = []
    nombre = input("Ingrese su nombre: ").title()
    cliente.append(nombre)
    nickname = input("Ingrese su nickname: ")
    cliente.append(nickname)
    show = input("Ingrese con que quiere jugar PC o CONSOLA: ").upper()
    show = show_validar(show)
    cliente.append(show)
    tiempo = seleccionar_horas(lista_horas)
    cliente.append(tiempo)
    desea_comida = input("Desea comida? SI o NO: ").upper()
    desea_comida = comida_validar(desea_comida)
    if desea_comida == "SI":
        comida, comida_precio = seleccionar_cafeteria(lista_cafe)
    else:
        comida, comida_precio = "NO", 0
    cliente.append(comida)
    cuenta = calcular_precio_final(tiempo, comida_precio)
    descuento, cuenta_final = descuento_validar(cuenta)
    cliente.append(cuenta_final)
    lista_ganancias.append(cuenta_final)
    if show == "PC":
        ganancias_por_servicio[0] += cuenta_final - comida_precio
    elif show == "CONSOLA":
        ganancias_por_servicio[1] += cuenta_final - comida_precio
    ganancias_por_servicio[2] += comida_precio
    print("------------------------------------------------------------")
    print(f"Factura {comprobante}")
    print(f"Nombre: {cibercafe[1]}")
    print(f"CUIT: {cibercafe[4]}")
    print(f"Direccion: {cibercafe[2]}")
    print(f"Telefono: {cibercafe[3]}")
    print("")
    print(f"Nombre del cliente: {cliente[0]}")
    print(f"Nickname: {cliente[1]}")
    print(f"Servicio utilizado: {cliente[2]}")
    print(f"Tiempo jugado: {cliente[3]} horas")
    print(f"Comida: {cliente[4]}")
    print(f"Cuenta total: ${cuenta_final}")
    print(f"Descuento aplicado: {descuento}%")
    print("------------------------------------------------------------")
    comprobante += 1

print("Lista de ganancias por operación:", lista_ganancias)
total_recaudado = 0
for ganancia in ganancias_por_servicio:
    total_recaudado += ganancia

print("Total recaudado:", total_recaudado)
ordenar_servicios_por_gasto(ganancias_por_servicio)
