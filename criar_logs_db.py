import sqlite3
from datetime import datetime

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

# Cria a tabela de logs
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    evento TEXT NOT NULL,
    ip TEXT NOT NULL,
    data TEXT NOT NULL
)
""")

# Dados fictícios para teste
logs_exemplo = [
    ("joao.silva", "Tentativa de login falha", "192.168.1.101", "2025-05-14 21:00:00"),
    ("joao.silva", "Tentativa de login falha", "192.168.1.101", "2025-05-14 21:01:00"),
    ("joao.silva", "Conta bloqueada", "192.168.1.101", "2025-05-14 21:02:00"),
    ("maria.oliveira", "Novo dispositivo detectado", "179.215.88.77", "2025-05-14 22:05:00"),
    ("admin", "Acesso autorizado ao painel", "127.0.0.1", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
]

# Insere os dados
cursor.executemany("INSERT INTO logs (usuario, evento, ip, data) VALUES (?, ?, ?, ?)", logs_exemplo)

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()

print("✅ Banco de dados 'logs.db' criado e populado com sucesso.")
