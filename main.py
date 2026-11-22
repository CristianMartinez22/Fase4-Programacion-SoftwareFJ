
# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: main.py
# Descripcion: Programa principal del sistema.
# ============================================

import logging

from entidades import Cliente
from servicios import (
    ReservaSalas,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from reserva import Reserva

from excepciones import (
    ErrorSistema,
    DatosFaltantesError,
    DatosInvalidosError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


# ============================================
# CONFIGURACION DEL REGISTRO DE EVENTOS
# ============================================

logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)


# ============================================
# LISTAS INTERNAS DEL SISTEMA
# ============================================

clientes = []
servicios = []
reservas = []

# ============================================
# REGISTRO DE CLIENTES
# ============================================

def registrar_cliente(identificacion, nombre, correo, telefono):
    try:
        cliente = Cliente(
            identificacion,
            nombre,
            correo,
            telefono
        )

        clientes.append(cliente)

        logger.info(
            "Cliente registrado correctamente: %s",
            cliente.nombre
        )

        print(f"Cliente {nombre} registrado exitosamente.")
        return cliente

    except ErrorSistema as error:
        logger.error("Error al registrar cliente: %s", error)
        print(f"No fue posible registrar el cliente: {error}")
        return None

# ============================================
# REGISTRO DE SERVICIOS
# ============================================

def registrar_servicio(servicio):
    try:
        # Verificamos que el servicio este disponible.
        servicio.verificar_disponibilidad()

        # Guardamos el servicio en la lista.
        servicios.append(servicio)

        logger.info(
            "Servicio registrado correctamente: %s",
            servicio.nombre
        )

        print(
            f"Servicio {servicio.nombre} registrado exitosamente."
        )

        return servicio

    except ErrorSistema as error:
        logger.error("Error al registrar servicio: %s", error)
        print(f"No fue posible registrar el servicio: {error}")
        return None

# ============================================
# CREACION DE RESERVAS
# ============================================

def crear_reserva(identificador, cliente, servicio, duracion):
    try:
        # Creamos el objeto reserva.
        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion
        )

        # Procesamos el costo de la reserva.
        reserva.procesar(descuento=0, impuesto=19)

        # Guardamos la reserva en nuestra lista.
        reservas.append(reserva)

        logger.info(
            "Reserva creada correctamente: %s",
            reserva.identificador
        )

        print(
            f"Reserva {identificador} creada exitosamente."
        )

        return reserva

    except ErrorSistema as error:
        logger.error("Error al crear reserva: %s", error)
        print(f"No fue posible crear la reserva: {error}")
        return None

# ============================================
# CONFIRMAR RESERVAS
# ============================================

def confirmar_reserva(reserva):
    try:
        reserva.confirmar()

        logger.info(
            "Reserva confirmada: %s",
            reserva.identificador
        )

        print(
            f"Reserva {reserva.identificador} confirmada exitosamente."
        )

        return True

    except ErrorSistema as error:
        logger.error("Error al confirmar reserva: %s", error)
        print(f"No fue posible confirmar la reserva: {error}")
        return False


# ============================================
# CANCELAR RESERVAS
# ============================================

def cancelar_reserva(reserva):
    try:
        reserva.cancelar()

        logger.info(
            "Reserva cancelada: %s",
            reserva.identificador
        )

        print(
            f"Reserva {reserva.identificador} cancelada exitosamente."
        )

        return True

    except ErrorSistema as error:
        logger.error("Error al cancelar reserva: %s", error)
        print(f"No fue posible cancelar la reserva: {error}")
        return False

# ============================================
# CONSULTAR RESERVAS
# ============================================

def mostrar_reservas():
    try:
        if not reservas:
            raise ReservaInvalidaError(
                "No existen reservas registradas."
            )

        print("\n========== LISTA DE RESERVAS ==========")

        for reserva in reservas:
            print(reserva.mostrar_reserva())

        print("=======================================")

        logger.info("Se consultaron las reservas registradas.")

    except ReservaInvalidaError as error:
        logger.warning("Consulta de reservas: %s", error)
        print(error)

# ============================================
# VALIDACION DE DURACIONES
# ============================================

def convertir_duracion(valor):
    try:
        duracion = float(valor)

        if duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero."
            )

        return duracion

    except (ValueError, TypeError) as error:
        raise DatosInvalidosError(
            "La duracion ingresada no es un numero valido."
        ) from error

# ============================================
# PRUEBAS DE FUNCIONAMIENTO DEL SISTEMA
# ============================================

def ejecutar_pruebas():

    print("\n========================================")
    print(" INICIANDO PRUEBAS DEL SISTEMA SOFTWARE FJ")
    print("========================================\n")

    # PRUEBA 1: REGISTRO DE CLIENTE VALIDO
    try:
        cliente1 = registrar_cliente(
            "100123456",
            "Carlos Perez",
            "carlos@gmail.com",
            "3124567890"
        )

        if cliente1 is None:
            raise ErrorSistema("No se pudo registrar el cliente.")

    except ErrorSistema as error:
        print(f"Error en la prueba 1: {error}")

    else:
        print("Prueba 1 superada: cliente registrado.")

    finally:
        print("Finalizada la prueba 1.\n")

    # PRUEBA 2: REGISTRO DE CLIENTE CON CORREO INVALIDO
    cliente_invalido = registrar_cliente(
        "100987654",
        "Maria Lopez",
        "correo_incorrecto",
        "3109876543"
    )

    if cliente_invalido is None:
        print("Prueba 2 superada: se rechazo el correo invalido.\n")

    # PRUEBA 3: REGISTRO DE UNA SALA
    sala = ReservaSalas("Sala principal", 50000, 20)
    registrar_servicio(sala)

    # PRUEBA 4: REGISTRO DE EQUIPOS
    equipo = AlquilerEquipos(
        "Computador portatil",
        15000,
        "Portatil"
    )
    registrar_servicio(equipo)

    # PRUEBA 5: REGISTRO DE ASESORIA
    asesoria = AsesoriaEspecializada(
        "Asesoria informatica",
        80000,
        "Informatica"
    )
    registrar_servicio(asesoria)

    # PRUEBA 6: REGISTRO DE SERVICIO NO DISPONIBLE
    sala_no_disponible = ReservaSalas(
        "Sala temporal",
        30000,
        10,
        disponible=False
    )

    resultado = registrar_servicio(sala_no_disponible)

    if resultado is None:
        print("Prueba 6 superada: se rechazo el servicio no disponible.\n")

    # PRUEBA 7: CONVERSION DE DURACION VALIDA
    duracion = convertir_duracion("3")
    print(f"Prueba 7 superada: duracion convertida: {duracion} horas.\n")

    # PRUEBA 8: CONVERSION DE DURACION INVALIDA
    try:
        convertir_duracion("tres")

    except DatosInvalidosError as error:
        print(f"Prueba 8 superada: {error}")
        print(f"Error original: {error.__cause__}\n")

    # PRUEBA 9: CREACION DE UNA RESERVA
    reserva1 = crear_reserva(
        "R001",
        cliente1,
        sala,
        duracion
    )

    # PRUEBA 10: CONFIRMACION DE RESERVA
    if reserva1 is not None:
        confirmar_reserva(reserva1)

    # PRUEBA 11: INTENTO DE CONFIRMAR UNA RESERVA DOS VECES
    if reserva1 is not None:
        confirmar_reserva(reserva1)

    # PRUEBA 12: CREACION DE UNA SEGUNDA RESERVA
    reserva2 = crear_reserva(
        "R002",
        cliente1,
        equipo,
        2
    )

    # PRUEBA 13: CANCELACION DE UNA RESERVA
    if reserva2 is not None:
        cancelar_reserva(reserva2)

    # PRUEBA 14: CONSULTA DE RESERVAS
    mostrar_reservas()

    logger.info("Finalizaron las pruebas del sistema.")

    print("\n========================================")
    print(" PRUEBAS DEL SISTEMA FINALIZADAS")
    print("========================================")

# ============================================
# INICIO DEL PROGRAMA
# ============================================

if __name__ == "__main__":
    ejecutar_pruebas()
