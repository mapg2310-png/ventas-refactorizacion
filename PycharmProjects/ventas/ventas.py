# Módulo inicial de procesamiento de ventas
# Constantes de negocio
MONTO_ALTO = 1000
MONTO_VIP = 500
FACTOR_DESCUENTO = 0.9


def es_venta_valida(registro):
    """Comprobar si el registro es una venta válida."""
    return (
        registro['tipo'] == 'venta'
        and registro['monto'] > 0
        and registro['estado'] == 'completado'
    )


def es_devolucion_valida(registro):
    """Comprobar si el registro es una devolución válida."""
    return registro['tipo'] == 'devolucion' and registro['monto'] > 0


def calcular_monto_venta(registro):
    """Calcular el monto final de una venta aplicando los descuentos."""
    if registro['monto'] > MONTO_ALTO or (
        registro['cliente_tipo'] == 'VIP' and registro['monto'] > MONTO_VIP
    ):
        monto_final = registro['monto'] * FACTOR_DESCUENTO
    else:
        monto_final = registro['monto']
    return monto_final



def procesar_ventas(datos):
    # Esta función hace muchas cosas a la vez (código original refactorizado poco a poco)
    resultados = []
    for registro in datos:
        # Comprobar si es una venta válida
        if es_venta_valida(registro):
            # Aplicar descuento si el monto es alto o es cliente VIP
            monto_final = calcular_monto_venta(registro)

            # Formatear el resultado
            mensaje = "Cliente: " + registro['nombre'] + " - Total: " + str(monto_final)
            resultados.append(mensaje)

            # Imprimir log de auditoría (duplicado innecesario)
            print("Procesando registro de: " + registro['nombre'])
        elif es_devolucion_valida(registro):
            # Lógica de devoluciones mezclada
            monto_final = registro['monto'] * -1
            mensaje = "Cliente: " + registro['nombre'] + " - Retorno: " + str(monto_final)
            resultados.append(mensaje)
            print("Procesando registro de: " + registro['nombre'])

    return resultados


# Datos de prueba para verificar que funciona
datos_sucios = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(procesar_ventas(datos_sucios))
