import subprocess
import os

def carregar_logs(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Nenhum log foi encontrado."
    except Exception as e:
        return f"Erro ao ler logs: {str(e)}"

def perguntar_ollama(pergunta, logs):
    try:
        prompt = (
            "Você é o Aegis, um especialista em cibersegurança. "
            "Seu trabalho é analisar os registros de log e ajudar o usuário com base neles. "
            "Aqui estão os registros do sistema:\n\n"
            f"{logs}\n\n"
            "Agora responda à seguinte pergunta com base nessas informações:\n"
            f"{pergunta}"
        )

        processo = subprocess.Popen(
            ['ollama', 'run', 'llama3'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )

        stdout, stderr = processo.communicate(input=prompt)

        if processo.returncode == 0:
            return stdout.strip()
        else:
            return f"Erro: {stderr.strip()}"

    except Exception as e:
        return f"Erro ao chamar o Ollama: {str(e)}"

if __name__ == "__main__":
    print("\n🛡️ Chatbot de Cibersegurança - Aegis")
    print("Digite sua dúvida com base em atividades suspeitas. Escreva 'sair' para encerrar.\n")

    logs = carregar_logs("logs.txt")  # Atualizar se o caminho for diferente

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Aegis: Saindo... Até logo! 🛡️")
            break

        resposta = perguntar_ollama(pergunta, logs)
        print(f"Aegis: {resposta}\n")
