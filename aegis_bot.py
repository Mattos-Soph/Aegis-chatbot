import random
from aegis_analyst_bot import verificar_ataques_repetidos  # Importa a função de análise de ataques

# Função para obter uma resposta aleatória sobre segurança
def resposta_aleatoria():
    respostas = [
        "Lembre-se de sempre usar senhas fortes e únicas!",
        "Manter seus sistemas atualizados é uma das melhores formas de se proteger.",
        "Cuidado com links desconhecidos, eles podem ser phishing.",
        "Verifique frequentemente suas configurações de segurança.",
        "A autenticação de dois fatores pode aumentar sua segurança online!"
    ]
    return random.choice(respostas)

# Função do chatbot para interagir com o usuário
def chatbot():
    print("Olá! Sou o Aegis, seu assistente de segurança digital.")
    
    while True:
        comando = input("Como posso ajudar? (Digite 'sair' para encerrar) ")
        
        if comando.lower() == "sair":
            print("Até logo! Fique seguro!")
            break
        
        elif "ataques repetidos" in comando.lower():
            arquivo_log = "caminho/do/seu/arquivo/de/log.txt"
            alertas = verificar_ataques_repetidos(arquivo_log)
            if alertas:
                for alerta in alertas:
                    print(alerta)  # Exibe as análises de ataques repetidos
            else:
                print("Não foram encontrados ataques repetidos.")
        
        elif "dicas de segurança" in comando.lower():
            print(resposta_aleatoria())  # Retorna uma dica aleatória de segurança
            
        elif "ajuda" in comando.lower():
            print("Eu posso te ajudar com os seguintes comandos:")
            print("- 'ataques repetidos' para verificar possíveis ataques repetidos no log.")
            print("- 'dicas de segurança' para receber uma dica de segurança aleatória.")
            print("- 'sair' para encerrar o chat.")
        
        else:
            print("Desculpe, não entendi o comando. Tente novamente ou digite 'ajuda' para ver o que posso fazer.")
            
# Executar o chatbot
if __name__ == "__main__":
    chatbot()
