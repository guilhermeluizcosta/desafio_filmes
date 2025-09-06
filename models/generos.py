from database import executar_query


class Genero:
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def listar(cls):
        rows = executar_query("SELECT id, nome FROM generos", fetch=True)
        return [cls(id=row[0], nome=row[1]) for row in rows]

    @classmethod
    def buscar_por_id(cls, genero_id):
        try:
            genero_id = int(genero_id)
            if genero_id <= 0:
                return None
        except ValueError:
            return None
        row = executar_query(
            "SELECT id, nome FROM generos WHERE id=?",
            (genero_id,),
            fetchone=True
        )
        return cls(id=row[0], nome=row[1]) if row else None

    @classmethod
    def buscar_por_nome(cls, nome):
        row = executar_query(
            "SELECT id, nome FROM generos WHERE nome=?",
            (nome.strip(),),
            fetchone=True
        )
        return cls(id=row[0], nome=row[1]) if row else None

    def salvar(self):
        if not self.nome or self.nome.strip() == "":
            raise ValueError("O nome do gênero não pode estar vazio.")

        existente = Genero.buscar_por_nome(self.nome)
        if existente and existente.id != self.id:
            raise ValueError("Já existe um gênero com esse nome.")

        if self.id:
            executar_query("UPDATE generos SET nome=? WHERE id=?",
                           (self.nome, self.id))
        else:
            executar_query(
                "INSERT INTO generos (nome) VALUES (?)", (self.nome,))

    def deletar(self):
        if not self.id:
            raise ValueError("Não é possível deletar um gênero sem ID.")
        executar_query("DELETE FROM generos WHERE id=?", (self.id,))
