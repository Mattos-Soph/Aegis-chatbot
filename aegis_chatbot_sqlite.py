import subprocess
import sqlite3

def carregar_logs_do_banco(caminho_banco):
    try:
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()
        cursor.execute("SELECT usuario, evento, ip, data FROM logs")
        registros = cursor.fetchall()
        conn.close()

        logs_formatados = "\n".join(
            f"[{data}] Usuário: {usuario} | Evento: {evento} | IP: {ip}"
            for usuario, evento, ip, data in registros
        )
        return logs_formatados if logs_formatados else "Nenhum log registrado."
    except Exception as e:
        return f"Erro ao carregar logs do banco: {str(e)}"

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

    logs = carregar_logs_do_banco("logs.db")  # Caminho do banco de dados SQLite

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Aegis: Saindo... Até logo! 🛡️")
            break

        resposta = perguntar_ollama(pergunta, logs)
        print(f"Aegis: {resposta}\n")
