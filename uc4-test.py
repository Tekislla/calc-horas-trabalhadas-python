import pytest
from calculadorauc4 import calcular_horas_trabalhadas


def test_calculo_horas_trabalhadas_sem_intervalo():
  entrada = "2100"
  saida_almoco = "12:00"
  retorno_almoco = "13:00"
  saida = "0800"

  horas_trabalhadas = calcular_horas_trabalhadas(entrada, saida_almoco,
                                                 retorno_almoco, saida)

  assert horas_trabalhadas == 10


def test_calculo_horas_trabalhadas_com_intervalo():
  entrada = "2100"
  saida_almoco = "1200"
  retorno_almoco = "13:00"
  saida = "08:00"
  intervalo = "0030"

  horas_trabalhadas = calcular_horas_trabalhadas(entrada, saida_almoco,
                                                 retorno_almoco, saida,
                                                 intervalo)

  assert horas_trabalhadas == 9.5
