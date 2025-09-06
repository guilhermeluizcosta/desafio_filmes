import pytest
import sqlite3
from unittest.mock import patch
from models.filmes import Filme
from models.generos import Genero

@pytest.fixture
def mock_conectar():
    with patch('database.conectar') as mock_conn:
        conn = sqlite3.connect(":memory:")
        mock_conn.return_value = conn
        yield conn
        conn.close()

@pytest.fixture
def setup_database(mock_conectar):
    conn = mock_conectar
    cursor = conn.cursor()
    with open("script.sql", "r") as f:
        script = f.read()
    cursor.executescript(script)
    conn.commit()
    yield

def test_salvar_genero(setup_database, mock_conectar):
    genero = Genero(nome='Ação')
    genero.salvar(conn=mock_conectar)
    assert genero.id is not None
    genero_salvo = Genero.buscar_por_id(genero.id, conn=mock_conectar)
    assert genero_salvo.nome == 'Ação'

def test_listar_generos(setup_database, mock_conectar):
    Genero(nome='Comédia').salvar(conn=mock_conectar)
    Genero(nome='Drama').salvar(conn=mock_conectar)
    generos = Genero.listar(conn=mock_conectar)
    assert len(generos) == 2
    assert any(g.nome == 'Comédia' for g in generos)
    assert any(g.nome == 'Drama' for g in generos)
def test_deletar_genero(setup_database, mock_conectar):
    genero = Genero(nome='Terror')
    genero.salvar(conn=mock_conectar)
    genero_id = genero.id
    genero.deletar(conn=mock_conectar)
    genero_deletado = Genero.buscar_por_id(genero_id, conn=mock_conectar)
    assert genero_deletado is None

def test_salvar_filme(setup_database, mock_conectar):
    genero = Genero(nome='Ficção Científica')
    genero.salvar(conn=mock_conectar)
    filme = Filme(nome='Interestelar', duracao=169, data_lancamento='2014-11-06', genero_id=genero.id, avaliacao=4.8, sinopse='Viagem espacial')
    filme.salvar(conn=mock_conectar)
    assert filme.id is not None
    filme_salvo = Filme.buscar_por_id(filme.id, conn=mock_conectar)
    assert filme_salvo.nome == 'Interestelar'

def test_listar_filmes(setup_database, mock_conectar):
    genero1 = Genero(nome='Aventura')
    genero1.salvar(conn=mock_conectar)
    genero2 = Genero(nome='Animação')
    genero2.salvar(conn=mock_conectar)
    Filme(nome='Indiana Jones', duracao=115, data_lancamento='1981-06-12', genero_id=genero1.id).salvar(conn=mock_conectar)
    Filme(nome='Toy Story', duracao=81, data_lancamento='1995-11-22', genero_id=genero2.id).salvar(conn=mock_conectar)
    filmes = Filme.listar(conn=mock_conectar)
    assert len(filmes) == 2
    assert any(f.nome == 'Indiana Jones' for f in filmes)
    assert any(f.nome == 'Toy Story' for f in filmes)

def test_deletar_filme(setup_database, mock_conectar):
    genero = Genero(nome='Suspense')
    genero.salvar(conn=mock_conectar)
    filme = Filme(nome='O Silêncio dos Inocentes', duracao=118, data_lancamento='1991-02-14', genero_id=genero.id)
    filme.salvar(conn=mock_conectar)
    filme_id = filme.id
    filme.deletar(conn=mock_conectar)
    filme_deletado = Filme.buscar_por_id(filme_id, conn=mock_conectar)
    assert filme_deletado is None



