
# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: excepciones.py
# Descripción: Excepciones personalizadas del sistema.
# ============================================


# Clase base para los errores propios del sistema.
class ErrorSistema(Exception):
    """Representa un error general dentro del sistema Software FJ."""
    pass


# Error cuando faltan datos obligatorios.
class DatosFaltantesError(ErrorSistema):
    """Se produce cuando no se ingresan todos los datos requeridos."""
    pass


# Error cuando los datos ingresados no cumplen las validaciones.
class DatosInvalidosError(ErrorSistema):
    """Se produce cuando un dato tiene un formato o valor incorrecto."""
    pass


# Error cuando un servicio no está disponible.
class ServicioNoDisponibleError(ErrorSistema):
    """Se produce cuando un servicio no puede ser utilizado."""
    pass


# Error cuando una reserva no cumple las condiciones necesarias.
class ReservaInvalidaError(ErrorSistema):
    """Se produce cuando una reserva contiene información incorrecta."""
    pass


# Error cuando se intenta realizar una operación no permitida.
class OperacionNoPermitidaError(ErrorSistema):
    """Se produce cuando se intenta ejecutar una acción no autorizada."""
    pass
