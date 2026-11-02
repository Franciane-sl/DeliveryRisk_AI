import sqlite3
from pathlib import Path


# Caminho para a raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]

# Diretório do banco de dados
DATABASE_DIR = BASE_DIR / "data"

# Caminho do arquivo SQLite
DATABASE_PATH = DATABASE_DIR / "delivery_risk.db"

# Função para criar e retornar uma conexão com o banco SQLite
def get_connection():
   
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection
