# my_project/tests/test_pagos.py

from src.pagos import procesar_pago
from unittest.mock import Mock

def test_pago_aprobado():
    mock_verificador = Mock(return_value=1000.0)
    assert procesar_pago("juan", 500.0, mock_verificador) is True

def test_pago_rechazado():
    mock_verificador = Mock(return_value=100.0)
    assert procesar_pago("juan", 200.0, mock_verificador) is False
