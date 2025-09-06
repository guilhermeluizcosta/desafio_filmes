CREATE TABLE IF NOT EXISTS generos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    duracao INTEGER NOT NULL, 
    data_lancamento DATE NOT NULL,
    genero_id INTEGER NOT NULL,
    avaliacao REAL CHECK (avaliacao >= 0.5 AND avaliacao <= 5.0),
    sinopse TEXT,
    FOREIGN KEY (genero_id) REFERENCES generos(id)
);

PRAGMA foreign_keys = ON;
