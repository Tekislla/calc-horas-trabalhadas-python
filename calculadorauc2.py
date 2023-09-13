from datetime import datetime


def calcular_horas_trabalhadas(entrada,
                               saida_almoco,
                               retorno_almoco,
                               saida,
                               intervalo=None):
  formato_hora = "%H:%M"

  try:
    entrada = datetime.strptime(entrada, formato_hora)
    saida_almoco = datetime.strptime(saida_almoco, formato_hora)
    retorno_almoco = datetime.strptime(retorno_almoco, formato_hora)
    saida = datetime.strptime(saida, formato_hora)
  except ValueError:
    raise ValueError("Erro: Os horários devem estar no formato HH:MM")

  if intervalo:
    try:
      intervalo = datetime.strptime(intervalo, formato_hora)
    except ValueError:
      raise ValueError(
          "Erro: O horário de intervalo deve estar no formato HH:MM")

    tempo_intervalo = intervalo - datetime.strptime("00:00", formato_hora)
    tempo_total_trabalhado = saida - entrada - (retorno_almoco -
                                                saida_almoco) - tempo_intervalo
  else:
    tempo_total_trabalhado = saida - entrada - (retorno_almoco - saida_almoco)

  horas_trabalhadas = tempo_total_trabalhado.total_seconds() / 3600.0

  return horas_trabalhadas
