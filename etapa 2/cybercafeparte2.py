import moduloCybercafe as cc
import random

# ======================
# Bitácora simple (.txt)
# ======================

def escribir_bitacora(evento, detalle):
    """Agrega una línea al archivo bitacora.txt"""
    with open("bitacora.txt", "a", encoding="utf-8") as f:
        f.write(f"{evento} - {detalle}\n")
    print(f"[LOG] {evento} - {detalle}")

# ======================
# Generación de ENTRADAS (.txt)
# ======================

def generar_archivos_entrada():
    escribir_bitacora("INICIO_GENERACION_ENTRADAS", "Comienza generación de archivos de entrada")

    nombres = ["Lautaro", "Victoria", "Lucas", "Sofía", "Martín",
               "Carla", "Nicolás", "Florencia", "Ezequiel", "Agustina"]
    nicks = ["Shadow", "Vortex", "Neo", "Pixel", "Ragnar", "Sky",
             "Mamba", "Turtle", "Ghost", "Zero"]
    servicios = ["PC", "CONSOLA"]
    turnos = ["MAÑANA", "TARDE", "NOCHE"]
    comidas = ["SI", "NO"]

    for n in range(1, 4):
        fname = f"entrada{n}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write("Nombre,Nickname,Turno,Servicio,Horas,Comida,Combo\n")
            for _ in range(1):
                nombre = random.choice(nombres)
                nickname = random.choice(nicks) + str(random.randint(1, 999))
                turno = random.choice(turnos)
                servicio = random.choice(servicios)
                horas = random.randint(1, 3)
                comida = random.choice(comidas)
                combo = random.randint(1, 3) if comida == "SI" else 0
                linea = f"{nombre},{nickname},{turno},{servicio},{horas},{comida},{combo}\n"
                f.write(linea)
        escribir_bitacora("ARCHIVO_ENTRADA_GENERADO", f"{fname} con 10 registros")

    escribir_bitacora("FIN_GENERACION_ENTRADAS", "Finalizó generación de archivos")

# ======================
# Utilidades
# ======================

def precio_combo(combo):
    if combo == 1:
        return 2500
    elif combo == 2:
        return 4000
    elif combo == 3:
        return 7000
    return 0

# ======================
# Procesamiento automático de archivos de entrada
# ======================

def procesar_archivos_automaticos(cibercafe, ganancias_por_servicio, lista_ganancias, comprobante):
    escribir_bitacora("INICIO_PROCESO_AUTOMATICO", "Procesando archivos de entrada para generar facturas automáticas")

    for n in range(1, 4):
        fname = f"entrada{n}.txt"
        try:
            with open(fname, "r", encoding="utf-8") as f:
                lineas = f.readlines()[1:]  # salta encabezado
        except:
            escribir_bitacora("ERROR_LECTURA", f"No se pudo leer {fname}")
            continue

        for linea in lineas:
            datos = linea.strip().split(",")
            if len(datos) < 7:
                continue

            nombre, nickname, turno, show, horas, comida_flag, combo = datos
            turno = cc.turno_validar(turno.upper())
            show = cc.show_validar(show.upper())
            horas = cc.tiempo_validar(int(horas))
            comida_flag = cc.comida_validar(comida_flag.upper())
            combo = int(combo)
            if comida_flag == "NO":
                combo = 0

            comida_precio = precio_combo(combo)
            cuenta = cc.calcular_precio_final(horas, comida_precio, turno)
            descuento, cuenta_final = cc.descuento_validar(cuenta)

            lista_ganancias.append(cuenta_final)
            if show == "PC":
                ganancias_por_servicio[0] += cuenta_final - comida_precio
            elif show == "CONSOLA":
                ganancias_por_servicio[1] += cuenta_final - comida_precio
            ganancias_por_servicio[2] += comida_precio

            # Crear factura automática
            fname_factura = f"Factura_{comprobante:04d}_{nombre}_{nickname}.txt"
            with open(fname_factura, "w", encoding="utf-8") as fc:
                fc.write("------------------------------------------------------------\n")
                fc.write(f"Factura {comprobante}\n")
                fc.write(f"Nombre: {cibercafe[1]}\n")
                fc.write(f"CUIT: {cibercafe[4]}\n")
                fc.write(f"Direccion: {cibercafe[2]}\n")
                fc.write(f"Telefono: {cibercafe[3]}\n\n")
                fc.write(f"Cliente: {nombre} ({nickname})\n")
                fc.write(f"Turno: {turno}\n")
                fc.write(f"Servicio: {show}\n")
                fc.write(f"Horas jugadas: {horas}\n")
                fc.write(f"Comida: {'Combo ' + str(combo) if comida_flag == 'SI' else 'NO'}\n")
                fc.write(f"Cuenta total: ${int(cuenta_final)}\n")
                fc.write(f"Descuento aplicado: {int(descuento)}%\n")
                fc.write("------------------------------------------------------------\n")

            escribir_bitacora("FACTURA_AUTOMATICA",
                              f"{fname_factura} | Servicio={show}, Turno={turno}, Total=${int(cuenta_final)}")

            comprobante += 1

    escribir_bitacora("FIN_PROCESO_AUTOMATICO", "Finalizó el proceso automático de facturas")
    return comprobante

# ======================
# Modo manual (con matrices)
# ======================

def modo_manual_con_matrices(cibercafe, lista_horas, lista_cafe,
                             ganancias_por_servicio, lista_ganancias,
                             M_MAÑANA, M_TARDE, M_NOCHE,
                             comprobante):
    """
    Permite ingresar facturas manualmente y ocupar una máquina real
    usando cc.ocuparMaquina(M).
    """
    continuar = 0
    while continuar != -1:
        nombre = input("Ingrese su nombre: ").title()
        nickname = input("Ingrese su nickname: ")
        turno = cc.turno_validar(input("Ingrese turno (MAÑANA/TARDE/NOCHE): ").upper())
        show = cc.show_validar(input("Ingrese con qué quiere jugar (PC/CONSOLA): ").upper())

        # Ocupación de máquina
        print(f"Seleccione una máquina para {show} en turno {turno} (matriz 5x5).")
        if turno == "MAÑANA":
            M_MAÑANA = cc.ocuparMaquina(M_MAÑANA)
        elif turno == "TARDE":
            M_TARDE = cc.ocuparMaquina(M_TARDE)
        else:
            M_NOCHE = cc.ocuparMaquina(M_NOCHE)

        horas = cc.seleccionar_horas(lista_horas)
        desea_comida = cc.comida_validar(input("Desea comida? SI o NO: ").upper())
        if desea_comida == "SI":
            combo = cc.combo_validar(int(input("Ingrese el combo (1, 2 o 3): ")))
        else:
            combo = 0

        comida_precio = precio_combo(combo)
        cuenta = cc.calcular_precio_final(horas, comida_precio, turno)
        descuento, cuenta_final = cc.descuento_validar(cuenta)

        # Sumar ganancias
        if show == "PC":
            ganancias_por_servicio[0] += cuenta_final - comida_precio
        elif show == "CONSOLA":
            ganancias_por_servicio[1] += cuenta_final - comida_precio
        ganancias_por_servicio[2] += comida_precio
        lista_ganancias.append(cuenta_final)

        # Crear e imprimir factura
        fname = f"Factura_{comprobante:04d}_{nombre}_{nickname}.txt"
        factura = [
            "------------------------------------------------------------",
            f"Factura {comprobante}",
            f"Nombre: {cibercafe[1]}",
            f"CUIT: {cibercafe[4]}",
            f"Direccion: {cibercafe[2]}",
            f"Telefono: {cibercafe[3]}",
            "",
            f"Cliente: {nombre} ({nickname})",
            f"Turno: {turno}",
            f"Servicio: {show}",
            f"Horas jugadas: {horas}",
            f"Comida: {'Combo ' + str(combo) if desea_comida == 'SI' else 'NO'}",
            f"Cuenta total: ${int(cuenta_final)}",
            f"Descuento aplicado: {int(descuento)}%",
            "------------------------------------------------------------"
        ]

        with open(fname, "w", encoding="utf-8") as fc:
            for linea in factura:
                fc.write(linea + "\n")

        print("\n".join(factura))

        escribir_bitacora("FACTURA_MANUAL",
                          f"{fname} | Servicio={show}, Turno={turno}, Total=${int(cuenta_final)}")

        comprobante += 1
        try:
            continuar = int(input("¿Desea cargar otra factura? (Ingrese -1 para salir): "))
        except:
            continuar = -1

    return comprobante, M_MAÑANA, M_TARDE, M_NOCHE

# ======================
# Programa principal
# ======================

def main():
    integrantes = ["Lautaro Giampaoli", "Victoria Eugenia Plaisant", "Navarro Lucas Sebastian"]
    print("Integrantes del grupo:", integrantes)

    cibercafe = ["Botas", "Cibercafe Botas", "Av Rivadavia 4567", "011-12345678", "20-12345678-9"]
    lista_horas = [1, 2, 3]
    lista_cafe = [1, 2, 3]
    ganancias_por_servicio = [0, 0, 0]  # [PC, CONSOLA, COMIDA]
    lista_ganancias = []

    M_MAÑANA = [[0]*5 for _ in range(5)]
    M_TARDE  = [[0]*5 for _ in range(5)]
    M_NOCHE  = [[0]*5 for _ in range(5)]

    # 1) Generar automáticamente los 3 archivos de entrada
    generar_archivos_entrada()

    # 2) Procesar esas entradas para generar facturas automáticas y sumar al total
    comprobante = 1
    comprobante = procesar_archivos_automaticos(cibercafe, ganancias_por_servicio, lista_ganancias, comprobante)

    # 3) Luego permitir cargar facturas manuales
    comprobante, M_MAÑANA, M_TARDE, M_NOCHE = modo_manual_con_matrices(
        cibercafe, lista_horas, lista_cafe,
        ganancias_por_servicio, lista_ganancias,
        M_MAÑANA, M_TARDE, M_NOCHE,
        comprobante
    )

    # 4) Reporte final
    total_recaudado = sum(ganancias_por_servicio)
    print("\n=== REPORTE FINAL ===")
    print("Total recaudado:", int(total_recaudado))
    cc.ordenar_servicios_por_gasto(ganancias_por_servicio)

    escribir_bitacora("REPORTE_FINAL",
                      f"Total=${int(total_recaudado)} | PC=${int(ganancias_por_servicio[0])}, "
                      f"CONSOLA=${int(ganancias_por_servicio[1])}, COMIDA=${int(ganancias_por_servicio[2])}")

if __name__ == "__main__":
    main()
