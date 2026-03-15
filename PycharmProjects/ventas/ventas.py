# Módulo inicial de procesamiento de ventas

# Constantes de negocio
MONTO_ALTO = 1000
MONTO_VIP = 500
FACTOR_DESCUENTO = 0.9


def es_venta_valida(registro):
    """
    Comprobar si el registro es una venta válida.

    Args:
        registro: Diccionario con los datos de una operación.

    Returns:
        True si es una venta con monto positivo y estado completado, False en caso contrario.
    """
    return (
        registro['tipo'] == 'venta'
        and registro['monto'] > 0
        and registro['estado'] == 'completado'
    )


def es_devolucion_valida(registro):
    """
    Comprobar si el registro es una devolución válida.

    Args:
        registro: Diccionario con los datos de una operación.

    Returns:
        True si es una devolución con monto positivo, False en caso contrario.
    """
    return registro['tipo'] == 'devolucion' and registro['monto'] > 0


def calcular_monto_venta(registro):
    """
    Calcular el monto final de una venta aplicando los descuentos de negocio.

    Se aplica descuento a ventas de importe alto o a clientes VIP con importe suficiente.

    Args:
        registro: Diccionario con los datos de la venta.

    Returns:
        Importe final de la venta tras aplicar, si corresponde, el descuento.
    """
    # Descuento especial para ventas de importe alto o clientes VIP
    if registro['monto'] > MONTO_ALTO or (
        registro['cliente_tipo'] == 'VIP' and registro['monto'] > MONTO_VIP
    ):
        monto_final = registro['monto'] * FACTOR_DESCUENTO
    else:
        monto_final = registro['monto']
    return monto_final


def procesar_ventas(datos):
    """
    Procesar una lista de registros de ventas y devoluciones.

    Args:
        datos: Lista de diccionarios con operaciones de venta y devolución.

    Returns:
        Lista de cadenas formateadas con el resultado de cada operación válida.
    """
    resultados = []
    for registro in datos:
        if es_venta_valida(registro):
            monto_final = calcular_monto_venta(registro)
            mensaje = "Cliente: " + registro['nombre'] + " - Total: " + str(monto_final)
            resultados.append(mensaje)
            # Log de auditoría: se registra cada operación procesada
            print("Procesando registro de: " + registro['nombre'])
        elif es_devolucion_valida(registro):
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
