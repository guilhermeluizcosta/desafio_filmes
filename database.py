import sqlite3

DATABASE_NAME = 'filmes.db'

def conectar():
    return sqlite3.connect(DATABASE_NAME)

def criar_tabelas():
    with conectar() as conn:
        cursor = conn.cursor()
        
    with open('script.sql','r') as file:
        script = file.read()

    cursor.executescript(script)
    conn.commit()
    conn.close()
    
def executar_query(query, params=(), fetch=False, fetchone=False):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query, params)
    resultado = None
    if fetch:
        resultado = cursor.fetchall()
    elif fetchone:
        resultado = cursor.fetchone()
    conn.commit()
    conn.close()
    return resultado

if __name__ == '__main__':
    criar_tabelas()