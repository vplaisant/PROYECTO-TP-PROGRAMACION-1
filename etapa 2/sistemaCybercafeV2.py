import moduloCybercafeV2 as cc
import random

def escribir_bitacora(evento, detalle):
    with open("bitacora.txt", "a", encoding="utf-8") as f:
        f.write(f"{evento} - {detalle}\n")
    print(f"[LOG] {evento} - {detalle}")

def generar_archivos_entrada():
    nombres = ["Lautaro", "Victoria", "Lucas", "Sofía", "Martín", "Carla", "Nicolás", "Florencia", "Ezequiel", "Agustina"]
    nicks = ["Shadow", "Vortex", "Neo", "Pixel", "Ragnar", "Sky", "Mamba", "Turtle", "Ghost", "Zero"]
    servicios = ["PC", "CONSOLA"]
    turnos = ["MAÑANA", "TARDE", "NOCHE"]
    comidas = ["SI", "NO"]

    for n in range(1, 4):
        fname = f"entrada{n}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write("Nombre,Nickname,Turno,Servicio,Horas,Comida,Combo\n")
            for _ in range(5):
                nombre = random.choice(nombres)
                nickname = random.choice(nicks) + str(random.randint(1, 999))
                turno = random.choice(turnos)
                servicio = random.choice(servicios)
                horas = random.randint(1, 3)
                comida = random.choice(comidas)
                combo = random.randint(1, 3) if comida == "SI" else 0
                linea = f"{nombre},{nickname},{turno},{servicio},{horas},{comida},{combo}\n"
                f.write(linea)
        escribir_bitacora("ARCHIVO_ENTRADA_GENERADO", f"{fname} creado")

def main():
    integrantes = ["Lautaro Giampaoli", "Victoria Eugenia Plaisant", "Navarro Lucas Sebastian"]
    print("Integrantes del grupo:", integrantes)

    cibercafe = ["Botas", "Cibercafe Botas", "Av Rivadavia 4567", "011-12345678", "20-12345678-9"]
    lista_cafe = [1, 2, 3]
    ganancias_por_servicio = [0, 0, 0]
    lista_ganancias = []
    M_MAÑANA = [[0]*5 for _ in range(5)]
    M_TARDE = [[0]*5 for _ in range(5)]
    M_NOCHE = [[0]*5 for _ in range(5)]

    generar_archivos_entrada()
    comprobante = 1
    continuar = 0
    print("------------------------------------------------------------")
    while continuar != -1:
        cliente = []
        nombre = cc.ingresoNombre()
        nickname = cc.ingresoNick()
        turno = cc.ingresoTurno()
        show = cc.ingresoShow()
        print(f"Seleccione una máquina para {show}:")
        if turno == "MAÑANA":
            M_MAÑANA = cc.ocuparMaquina(M_MAÑANA)
        elif turno == "TARDE":
            M_TARDE = cc.ocuparMaquina(M_TARDE)
        else:
            M_NOCHE = cc.ocuparMaquina(M_NOCHE)
        tiempo = cc.seleccionar_horas()
        desea_comida = cc.deseaComida()
        if desea_comida == "SI":
            comida, comida_precio = cc.seleccionar_cafeteria(lista_cafe)
        else:
            comida, comida_precio = "NO", 0
        cuenta = cc.calcular_precio_final(tiempo, comida_precio, turno)
        descuento, cuenta_final = cc.descuento_validar(cuenta)

        lista_ganancias.append(cuenta_final)
        if show == "PC":
            ganancias_por_servicio[0] += cuenta_final - comida_precio
        elif show == "CONSOLA":
            ganancias_por_servicio[1] += cuenta_final - comida_precio
        ganancias_por_servicio[2] += comida_precio

        factura_nombre = f"Factura_{comprobante:04d}_{nombre}_{nickname}.txt"
        with open(factura_nombre, "w", encoding="utf-8") as f:
            f.write("------------------------------------------------------------\n")
            f.write(f"Factura {comprobante}\n")
            f.write(f"Nombre: {cibercafe[1]}\n")
            f.write(f"CUIT: {cibercafe[4]}\n")
            f.write(f"Direccion: {cibercafe[2]}\n")
            f.write(f"Telefono: {cibercafe[3]}\n\n")
            f.write(f"Cliente: {nombre} ({nickname})\n")
            f.write(f"Turno: {turno}\n")
            f.write(f"Servicio: {show}\n")
            f.write(f"Horas jugadas: {tiempo}\n")
            f.write(f"Comida: {comida}\n")
            f.write(f"Cuenta total: ${int(cuenta_final)}\n")
            f.write(f"Descuento aplicado: {int(descuento)}%\n")
            f.write("------------------------------------------------------------\n")

        escribir_bitacora("FACTURA_MANUAL", f"{factura_nombre} | Servicio={show}, Turno={turno}, Total=${int(cuenta_final)}")

        print(f"Factura generada: {factura_nombre}")
        comprobante += 1
        try:
            continuar = int(input("Ingrese cualquier numero para otra factura o -1 para salir: "))
        except:
            continuar = -1

    total_recaudado = sum(ganancias_por_servicio)
    print("\n=== REPORTE FINAL ===")
    print("Total recaudado:", total_recaudado)
    cc.ordenar_servicios_por_gasto(ganancias_por_servicio)
    escribir_bitacora("REPORTE_FINAL", f"Total=${int(total_recaudado)}")

if __name__ == "__main__":
    main()