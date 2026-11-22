
# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: servicios.py
# Descripcion: Gestion de los servicios de Software FJ.
# ============================================

# Importamos las herramientas para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos nuestras excepciones personalizadas.
from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


# ============================================
# CLASE ABSTRACTA SERVICIO
# ============================================

class Servicio(ABC):
    """Clase abstracta que representa un servicio de la empresa."""

    def __init__(self, nombre, tarifa, disponible=True):

        # Validamos el nombre del servicio.
        if not nombre or not isinstance(nombre, str):
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        # Validamos que la tarifa sea numerica y positiva.
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise DatosInvalidosError("La tarifa debe ser un numero.")

        if tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        # Guardamos los atributos del servicio.
        self._nombre = nombre
        self._tarifa = tarifa
        self._disponible = disponible

    # Propiedad para consultar el nombre.
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para consultar la tarifa.
    @property
    def tarifa(self):
        return self._tarifa

    # Propiedad para consultar la disponibilidad.
    @property
    def disponible(self):
        return self._disponible

    # Metodo para comprobar si el servicio esta disponible.
    def verificar_disponibilidad(self):

        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no esta disponible."
            )

        return True

    # Metodo abstracto para describir el servicio.
    @abstractmethod
    def describir_servicio(self):
        pass

    # Metodo abstracto para validar los parametros.
    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    # Metodo abstracto para calcular el costo.
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass


# ============================================
# CLASE RESERVA DE SALAS
# ============================================

class ReservaSalas(Servicio):
    """Servicio especializado en reservas de salas."""

    def __init__(self, nombre, tarifa, capacidad, disponible=True):

        # Inicializamos los atributos de la clase padre.
        super().__init__(nombre, tarifa, disponible)

        # Validamos la capacidad de la sala.
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError(
                "La capacidad debe ser un numero entero positivo."
            )

        self._capacidad = capacidad

    def describir_servicio(self):
        return (
            f"Reserva de salas: {self.nombre}. "
            f"Capacidad: {self._capacidad} personas. "
            f"Tarifa por hora: ${self.tarifa}"
        )

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion de la reserva debe ser positiva."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidosError(
                "Los porcentajes deben estar entre 0 y 100."
            )

        # Calculamos el precio inicial.
        subtotal = self.tarifa * duracion

        # Aplicamos el descuento.
        subtotal -= subtotal * (descuento / 100)

        # Aplicamos el impuesto.
        total = subtotal + (subtotal * (impuesto / 100))

        return round(total, 2)


# ============================================
# CLASE ALQUILER DE EQUIPOS
# ============================================

class AlquilerEquipos(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, nombre, tarifa, tipo_equipo, disponible=True):

        super().__init__(nombre, tarifa, disponible)

        if not tipo_equipo or not isinstance(tipo_equipo, str):
            raise DatosInvalidosError(
                "Debe especificar el tipo de equipo."
            )

        self._tipo_equipo = tipo_equipo

    def describir_servicio(self):
        return (
            f"Alquiler de equipos: {self.nombre}. "
            f"Tipo de equipo: {self._tipo_equipo}. "
            f"Tarifa por hora: ${self.tarifa}"
        )

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion del alquiler debe ser positiva."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidosError(
                "Los porcentajes deben estar entre 0 y 100."
            )

        subtotal = self.tarifa * duracion
        subtotal -= subtotal * (descuento / 100)
        total = subtotal + (subtotal * (impuesto / 100))

        return round(total, 2)


# ============================================
# CLASE ASESORIAS ESPECIALIZADAS
# ============================================

class AsesoriaEspecializada(Servicio):
    """Servicio especializado en asesorias profesionales."""

    def __init__(self, nombre, tarifa, especialidad, disponible=True):

        super().__init__(nombre, tarifa, disponible)

        if not especialidad or not isinstance(especialidad, str):
            raise DatosInvalidosError(
                "Debe especificar el area de especialidad."
            )

        self._especialidad = especialidad

    def describir_servicio(self):
        return (
            f"Asesoria especializada: {self.nombre}. "
            f"Especialidad: {self._especialidad}. "
            f"Tarifa por hora: ${self.tarifa}"
        )

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion de la asesoria debe ser positiva."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidosError(
                "Los porcentajes deben estar entre 0 y 100."
            )

        subtotal = self.tarifa * duracion
        subtotal -= subtotal * (descuento / 100)
        total = subtotal + (subtotal * (impuesto / 100))

        return round(total, 2)
