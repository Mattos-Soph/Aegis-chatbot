import sqlite3

def criar_banco():
    conn = sqlite3.connect('aegis_logs.db')  # Cria o arquivo do banco na pasta atual
    cursor = conn.cursor()

    # Cria a tabela 'logs' se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            evento TEXT,
            usuario TEXT,
            ip TEXT
        )
    ''')

    # Insere alguns dados de exemplo
    cursor.execute('DELETE FROM logs')  # Limpa dados antigos para evitar duplicação
    cursor.execute('''
        INSERT INTO logs (timestamp, evento, usuario, ip) VALUES
        ('2025-05-15 10:12:00', 'Tentativa de login falhou', 'joao.silva', '192.168.1.101'),
        ('2025-05-15 10:15:23', 'Conta bloqueada após 5 tentativas', 'joao.silva', '192.168.1.101'),
        ('2025-05-15 11:05:42', 'Novo dispositivo conectado', 'maria.oliveira', 'IP desconhecido')
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados criado e dados inseridos com sucesso!")

if __name__ == "__main__":
    criar_banco()
