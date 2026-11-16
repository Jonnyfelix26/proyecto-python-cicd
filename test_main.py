import pytest

from main import calcular_area


def test_calcular_area():
    assert calcular_area(5, 3) == 15


def test_calcular_area_con_decimales():
    assert calcular_area(2.5, 4) == pytest.approx(10.0)


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-5, 3)


def test_altura_negativa():
    with pytest.raises(ValueError):
        calcular_area(5, -3)


def test_valor_cero():
    with pytest.raises(ValueError):
        calcular_area(0, 3)