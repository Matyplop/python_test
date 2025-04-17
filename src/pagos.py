from typing import Callable


def verificar_saldo_en_banco(usuario: str) -> float:
    """
    Simula una consulta a un sistema externo (no se implementa).
    """
    raise NotImplementedError("Esta función simula un sistema externo.")


def procesar_pago(
    usuario: str,
    monto: float,
    verificador: Callable[[str], float]
) -> bool:
    saldo = verificador(usuario)
    return saldo >= monto
