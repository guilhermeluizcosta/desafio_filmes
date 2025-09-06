import sqlite3

DATABASE_NAME = 'filmes.db'

def conectar():
    return sqlite3.connect(DATABASE_NAME)

def executar_query(query, params=(), fetch=False, fetchone=False, lastrowid=False, conn=None):
    if conn is None:
        conn = conectar()
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute(query, params)
    resultado = None
    if fetch:
        resultado = cursor.fetchall()
    elif fetchone:
        resultado = cursor.fetchone()
    if lastrowid:
        resultado = cursor.lastrowid
    conn.commit()
    if close_conn:
        conn.close()
    return resultado

def criar_tabelas(conn=None):
    if conn is None:
        conn = conectar()
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
        
    with open("script.sql","r") as file:
        script = file.read()

    cursor.executescript(script)
    conn.commit()
    if close_conn:
        conn.close()

if __name__ == '__main__':
    criar_tabelas()