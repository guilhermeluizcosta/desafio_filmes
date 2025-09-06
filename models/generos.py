from database import executar_query


class Genero:
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def listar(cls, conn=None):
        rows = executar_query("SELECT id, nome FROM generos", fetch=True, conn=conn)
        return [cls(id=row[0], nome=row[1]) for row in rows]

    @classmethod
    def buscar_por_id(cls, genero_id, conn=None):
        try:
            genero_id = int(genero_id)
            if genero_id <= 0:
                return None
        except ValueError:
            return None
        row = executar_query(
            "SELECT id, nome FROM generos WHERE id=?",
            (genero_id,),
            fetchone=True,
            conn=conn
        )
        return cls(id=row[0], nome=row[1]) if row else None

    @classmethod
    def buscar_por_nome(cls, nome, conn=None):
        row = executar_query(
            "SELECT id, nome FROM generos WHERE nome=?",
            (nome.strip(),),
            fetchone=True,
            conn=conn
        )
        return cls(id=row[0], nome=row[1]) if row else None

    def salvar(self, conn=None):
        if not self.nome or self.nome.strip() == "":
            raise ValueError("O nome do gênero não pode estar vazio.")

        existente = Genero.buscar_por_nome(self.nome, conn=conn)
        if existente and existente.id != self.id:
            raise ValueError("Já existe um gênero com esse nome.")

        if self.id:
            executar_query("UPDATE generos SET nome=? WHERE id=?",
                           (self.nome, self.id), conn=conn)
        else:
            self.id = executar_query(
                "INSERT INTO generos (nome) VALUES (?)", (self.nome,), lastrowid=True, conn=conn)


    def deletar(self, conn=None):
        if not self.id:
            raise ValueError("Não é possível deletar um gênero sem ID.")
        executar_query("DELETE FROM generos WHERE id=?", (self.id,), conn=conn)

