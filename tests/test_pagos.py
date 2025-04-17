from unittest.mock import Mock
from src.pagos import procesar_pago


def test_pago_con_saldo_suficiente():
    mock_verificador = Mock(return_value=100.0)
    resultado = procesar_pago("usuario1", 50.0, mock_verificador)
    assert resultado is True


def test_pago_con_saldo_insuficiente():
    mock_verificador = Mock(return_value=20.0)
    resultado = procesar_pago("usuario1", 50.0, mock_verificador)
    assert resultado is False


def test_procesar_pago_llama_al_verificador():
    mock_verificador = Mock(return_value=100.0)
    procesar_pago("usuario2", 30.0, mock_verificador)
    mock_verificador.assert_called_once_with("usuario2")
