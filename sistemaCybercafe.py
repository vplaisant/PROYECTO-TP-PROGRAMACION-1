import moduloCybercafe as cc

integrantes = ["Lautaro Giampaoli", "Victoria Eugenia Plaisant", "Navarro Lucas Sebastian"]
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
    show = cc.show_validar(show)
    cliente.append(show)
    tiempo = cc.seleccionar_horas(lista_horas)
    cliente.append(tiempo)
    desea_comida = input("Desea comida? SI o NO: ").upper()
    desea_comida = cc.comida_validar(desea_comida)
    if desea_comida == "SI":
        comida, comida_precio = cc.seleccionar_cafeteria(lista_cafe)
    else:
        comida, comida_precio = "NO", 0
    cliente.append(comida)
    cuenta = cc.calcular_precio_final(tiempo, comida_precio)
    descuento, cuenta_final = cc.descuento_validar(cuenta)
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
cc.ordenar_servicios_por_gasto(ganancias_por_servicio)
