from database import executar_query
from models.generos import Genero
from datetime import datetime


class Filme:
    def __init__(self, id=None, nome=None, duracao=None, data_lancamento=None, genero_id=None, avaliacao=None, sinopse=None):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.data_lancamento = data_lancamento
        self.genero_id = genero_id
        self.avaliacao = avaliacao
        self.sinopse = sinopse

    @classmethod
    def listar(cls, conn=None):
        rows = executar_query("""
        SELECT f.id, f.nome, f.duracao, f.data_lancamento, f.genero_id, g.nome, f.avaliacao, f.sinopse
        FROM filmes f
        JOIN generos g ON f.genero_id = g.id
        """, fetch=True, conn=conn)
        filmes = []
        for r in rows:
            f = cls(
                id=r[0],
                nome=r[1],
                duracao=r[2],
                data_lancamento=r[3],
                genero_id=r[4],
                avaliacao=r[6],
                sinopse=r[7]
            )
            f.genero_nome = r[5]
            filmes.append(f)
        return filmes

    @classmethod
    def buscar_por_id(cls, filme_id, conn=None):
        try:
            filme_id = int(filme_id)
            if filme_id <= 0:
                return None
        except ValueError:
            return None
        row = executar_query("""
            SELECT f.id, f.nome, f.duracao, f.data_lancamento, f.genero_id, g.nome, f.avaliacao, f.sinopse
            FROM filmes f
            JOIN generos g ON f.genero_id = g.id
            WHERE f.id=?
        """, (filme_id,), fetchone=True, conn=conn)
        if row:
            f = cls(
                id=row[0],
                nome=row[1],
                duracao=row[2],
                data_lancamento=row[3],
                genero_id=row[4],
                avaliacao=row[6],
                sinopse=row[7]
            )
            f.genero_nome = row[5]
            return f
        return None

    def salvar(self, conn=None):

        if not self.nome or self.nome.strip() == "":
            raise ValueError("O nome do filme não pode estar vazio.")
        if not isinstance(self.duracao, int) or self.duracao <= 0:
            raise ValueError("A duração deve ser um número positivo.")

        if not self.data_lancamento or self.data_lancamento.strip() == "":
            raise ValueError("A data de lançamento é obrigatória.")
        try:
            data_obj = datetime.strptime(
                self.data_lancamento, '%Y-%m-%d').date()
            if data_obj > datetime.now().date():
                raise ValueError("A data de lançamento não pode ser futura.")
        except ValueError:
            raise ValueError(
                "Formato de data de lançamento inválido. Use YYYY-MM-DD.")
        if not self.genero_id or not Genero.buscar_por_id(self.genero_id, conn=conn):
            raise ValueError("O gênero informado não existe.")
        if self.avaliacao is not None and (self.avaliacao < 0.5 or self.avaliacao > 5.0):
            raise ValueError("A avaliação deve estar entre 0.5 e 5.0.")

        if self.id:
            executar_query("""
                UPDATE filmes SET nome=?, duracao=?, data_lancamento=?, genero_id=?, avaliacao=?, sinopse=?
                WHERE id=?
            """, (self.nome, self.duracao, self.data_lancamento, self.genero_id, self.avaliacao, self.sinopse, self.id), conn=conn)
        else:
            self.id = executar_query("""
                INSERT INTO filmes (nome, duracao, data_lancamento, genero_id, avaliacao, sinopse)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.nome, self.duracao, self.data_lancamento, self.genero_id, self.avaliacao, self.sinopse), lastrowid=True, conn=conn)


    def deletar(self, conn=None):
        if not self.id:
            raise ValueError("Não é possível deletar um filme sem ID.")
        executar_query("DELETE FROM filmes WHERE id=?", (self.id,), conn=conn)

