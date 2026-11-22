
# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: entidades.py
# Descripción: Entidades generales y gestión de clientes.
# ============================================

# Importamos herramientas para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos las excepciones personalizadas.
from excepciones import DatosFaltantesError, DatosInvalidosError


# ============================================
# CLASE ABSTRACTA GENERAL
# ============================================

class Entidad(ABC):
    """Clase abstracta que representa una entidad del sistema."""

    def __init__(self, identificador):
        # Validamos que el identificador no esté vacío.
        if not identificador:
            raise DatosFaltantesError("El identificador es obligatorio.")

        self._identificador = identificador

    # Propiedad para consultar el identificador.
    @property
    def identificador(self):
        return self._identificador

    # Método abstracto que deberán implementar las clases hijas.
    @abstractmethod
    def mostrar_informacion(self):
        pass


# ============================================
# CLASE CLIENTE
# ============================================

class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    def __init__(self, identificacion, nombre, correo, telefono):

        # Inicializamos la clase padre.
        super().__init__(identificacion)

        # Validamos que los datos obligatorios estén completos.
        if not nombre or not correo or not telefono:
            raise DatosFaltantesError(
                "Todos los datos del cliente son obligatorios."
            )

        # Validamos el nombre.
        if not nombre.replace(" ", "").isalpha():
            raise DatosInvalidosError(
                "El nombre solo debe contener letras."
            )

        # Validamos el correo electrónico.
        if "@" not in correo or "." not in correo:
            raise DatosInvalidosError(
                "El correo electrónico no tiene un formato válido."
            )

        # Validamos que el teléfono contenga únicamente números.
        if not telefono.isdigit() or len(telefono) < 7:
            raise DatosInvalidosError(
                "El teléfono debe contener al menos 7 números."
            )

        # Guardamos los datos mediante atributos protegidos.
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    # Propiedad para consultar el nombre.
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para consultar el correo.
    @property
    def correo(self):
        return self._correo

    # Propiedad para consultar el teléfono.
    @property
    def telefono(self):
        return self._telefono

    # Implementamos el método abstracto de la clase padre.
    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
