import re
from datetime import datetime
from collections import defaultdict

def verificar_ataques_repetidos(arquivo):
    ataques = defaultdict(int)
    alertas = []

    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            print(f"Linha do log sendo processada: {linha.strip()}")
            
            match = re.match(r'\[([^\]]+)\] (SYSTEM ALERT|PASSWORD CHANGE): (.*)', linha.strip())
            if match:
                hora_str = match.group(1)
                tipo_ataque = match.group(2)
                descricao = match.group(3)

               
                try:
                    hora = datetime.strptime(hora_str, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Erro ao processar a hora: {hora_str}")
                    continue 

              
                ataques[(hora, tipo_ataque, descricao)] += 1
                if ataques[(hora, tipo_ataque, descricao)] > 1:
                    alertas.append(f"⚠️ ALERTA: Ataque repetido detectado - {descricao} ({hora})")

    return alertas

arquivo_log = 'C:/Users/Pichau/OneDrive/Imagens/ChatBotAegis/logs.txt'

alertas = verificar_ataques_repetidos(arquivo_log)

for alerta in alertas:
    print(alerta)
