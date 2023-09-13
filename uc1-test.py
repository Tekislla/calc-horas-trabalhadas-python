import pytest
from calculadorauc1 import calcular_horas_trabalhadas


def test_calculo_horas_trabalhadas():
  entrada = "09:00"
  saida_almoco = "12:00"
  retorno_almoco = "13:00"
  saida = "18:00"

  horas_trabalhadas = calcular_horas_trabalhadas(entrada, saida_almoco,
                                                 retorno_almoco, saida)

  assert horas_trabalhadas == 8
