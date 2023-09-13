from datetime import datetime, timedelta

def calcular_horas_trabalhadas(entrada, saida_almoco, retorno_almoco, saida, intervalo=None):
    formato_hora = "%H:%M"
    
    if len(entrada) == 4:
        entrada = f"{entrada[:2]}:{entrada[2:]}"
    if len(saida_almoco) == 4:
        saida_almoco = f"{saida_almoco[:2]}:{saida_almoco[2:]}"
    if len(retorno_almoco) == 4:
        retorno_almoco = f"{retorno_almoco[:2]}:{retorno_almoco[2:]}"
    if len(saida) == 4:
        saida = f"{saida[:2]}:{saida[2:]}"

    try:
        entrada = datetime.strptime(entrada, formato_hora)
        saida_almoco = datetime.strptime(saida_almoco, formato_hora)
        retorno_almoco = datetime.strptime(retorno_almoco, formato_hora)
        saida = datetime.strptime(saida, formato_hora)
    except ValueError:
        raise ValueError("Erro: Os horários devem estar no formato HH:MM ou hhmm")

    if entrada > saida:
        saida += timedelta(days=1)

    if intervalo:
        try:
            if len(intervalo) == 4:
                intervalo = f"{intervalo[:2]}:{intervalo[2:]}"
            
            intervalo = datetime.strptime(intervalo, formato_hora)
        except ValueError:
            raise ValueError("Erro: O horário de intervalo deve estar no formato HH:MM ou hhmm")

        tempo_intervalo = intervalo - datetime.strptime("00:00", formato_hora)
        tempo_total_trabalhado = saida - entrada - (retorno_almoco - saida_almoco) - tempo_intervalo
    else:
        tempo_total_trabalhado = saida - entrada - (retorno_almoco - saida_almoco)

    horas_trabalhadas = tempo_total_trabalhado.total_seconds() / 3600.0

    return horas_trabalhadas
