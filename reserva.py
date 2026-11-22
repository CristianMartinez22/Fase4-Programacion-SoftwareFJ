
# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: reserva.py
# Descripcion: Gestion y procesamiento de reservas.
# ============================================

# Importamos las excepciones personalizadas.
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


# ============================================
# CLASE RESERVA
# ============================================

class Reserva:
    """Representa una reserva realizada por un cliente."""

    # Estados posibles de una reserva.
    ESTADOS_VALIDOS = ["Pendiente", "Confirmada", "Cancelada"]

    def __init__(self, identificador, cliente, servicio, duracion):

        # Validamos el identificador.
        if not identificador:
            raise ReservaInvalidaError(
                "La reserva necesita un identificador."
            )

        # Validamos que exista un cliente.
        if cliente is None:
            raise ReservaInvalidaError(
                "Debe asignarse un cliente a la reserva."
            )

        # Validamos que exista un servicio.
        if servicio is None:
            raise ReservaInvalidaError(
                "Debe asignarse un servicio a la reserva."
            )

        # Validamos la duracion.
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaInvalidaError(
                "La duracion debe ser un numero positivo."
            )

        # Guardamos los datos de la reserva.
        self._identificador = identificador
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion

        # Inicializamos el estado de la reserva.
        self._estado = "Pendiente"

        # Inicializamos el costo.
        self._costo = 0

    # ========================================
    # PROPIEDADES
    # ========================================

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    # ========================================
    # PROCESAMIENTO DE LA RESERVA
    # ========================================

    def procesar(self, descuento=0, impuesto=0):

        # Solo se pueden procesar reservas pendientes.
        if self._estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar reservas pendientes."
            )

        # Calculamos el costo utilizando el servicio.
        self._costo = self._servicio.calcular_costo(
            self._duracion,
            descuento,
            impuesto
        )

        return self._costo

    # ========================================
    # CONFIRMACION DE LA RESERVA
    # ========================================

    def confirmar(self):

        if self._estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "La reserva no puede confirmarse en su estado actual."
            )

        # Comprobamos que el servicio este disponible.
        self._servicio.verificar_disponibilidad()

        # Procesamos el costo si todavia no existe.
        if self._costo <= 0:
            self.procesar()

        # Cambiamos el estado.
        self._estado = "Confirmada"

        return True

    # ========================================
    # CANCELACION DE LA RESERVA
    # ========================================

    def cancelar(self):

        if self._estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        # Cambiamos el estado de la reserva.
        self._estado = "Cancelada"

        return True

    # ========================================
    # MOSTRAR INFORMACION
    # ========================================

    def mostrar_reserva(self):

        return (
            f"\n===== INFORMACION DE LA RESERVA =====\n"
            f"Codigo: {self.identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duracion: {self.duracion} horas\n"
            f"Costo: ${self.costo}\n"
            f"Estado: {self.estado}\n"
            f"====================================="
        )

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
