import pytest
from calculadorauc3 import calcular_horas_trabalhadas


def test_calculo_horas_trabalhadas_sem_intervalo():
  entrada = "21:00"
  saida_almoco = "12:00"
  retorno_almoco = "13:00"
  saida = "08:00"

  horas_trabalhadas = calcular_horas_trabalhadas(entrada, saida_almoco,
                                                 retorno_almoco, saida)

  assert horas_trabalhadas == 10


def test_calculo_horas_trabalhadas_com_intervalo():
  entrada = "21:00"
  saida_almoco = "12:00"
  retorno_almoco = "13:00"
  saida = "08:00"
  intervalo = "00:30"

  horas_trabalhadas = calcular_horas_trabalhadas(entrada, saida_almoco,
                                                 retorno_almoco, saida,
                                                 intervalo)

  assert horas_trabalhadas == 9.5
