# Desafio Técnico – Estágio Pessoa Desenvolvedora de Software

## Tecnologias Utilizadas
- Python 3.13.2
- SQLite
- Pytest

## Recurso Principal: Filmes
A aplicação gerencia principalmente o recurso Filme, que possui as seguintes propriedades:
| Propriedade | Tipo de Dados | Obrigatório | Descrição |
|-------------|-------------|-------------|-------------|
| id | INTEGER | Não |Identificador único do filme (gerado automaticamente pelo banco de dados).|
| nome | TEXT | Sim |Título do filme.
| duracao | INTEGER | Sim |Duração do filme em minutos
| data_lancamento | DATE | Sim |Data de lançamento do filme no formato YYYY-MM-DD.
| genero_id | INTEGER | Sim |ID do gênero ao qual o filme pertence (chave estrangeira para a tabela generos).
| avaliacao | REAL | Não |Avaliação do filme, um número real entre 0.5 e 5.0.
| sinopse | TEXT | Não |Breve descrição ou resumo do enredo do filme.

Além do recurso Filme, a aplicação também gerencia o recurso Gênero, que possui as seguintes propriedades:
| Propriedade | Tipo de Dados | Obrigatório | Descrição |
|-------------|-------------|-------------|-------------|
| id | INTEGER | Não |Identificador único do gênero (gerado automaticamente pelo banco de dados).|
| nome | TEXT | Sim |Nome do gênero.

## Configuração e Execução
1. Clonar o repositório
```bash
git clone https://github.com/guilhermeluizcosta/desafio_filmes.git
cd desafio_filmes
```
2. Instalar dependências
```bash
pip install -r requirements.txt
```
3. Executar a aplicação
```bash
python main.py
```
Ou
```bash
py main.py
```

## Funcionalidades
### Menu Principal
Ao iniciar a aplicação, você verá o seguinte menu:
```console
--- Menu Principal ---
1. Gerenciar Gêneros
2. Gerenciar Filmes
0. Sair
Escolha uma opção:
```
### Gerenciar Gêneros
Selecione a opção 1 no menu principal para acessar o menu de gerenciamento de gêneros:
```console
--- Gerenciar Gêneros ---
1. Listar Gêneros
2. Buscar Gênero por ID
3. Adicionar Gênero
4. Atualizar Gênero
5. Deletar Gênero
0. Voltar
Escolha uma opção: 
```
### Listar Gêneros
Selecione 1 para listar todos os gêneros cadastrados:
```console
[1] Ação
[2] Comédia
Pressione Enter para continuar...
```
### Buscar Gênero por ID
Selecione 2 e insira o ID do gênero para buscá-lo:
```console
ID do gênero: 1
[1] Ação
Pressione Enter para continuar...
```
### Adicionar Gênero
```console
[1] Ação
[2] Comédia
Pressione Enter para continuar...
```
### Atualizar Gênero
Selecione 4, insira o ID do gênero a ser atualizado e o novo nome:
```console
ID do gênero a atualizar: 3
Novo nome para 'Drama': Suspense
Atualizado com sucesso!
Pressione Enter para continuar...
```
### Deletar Gênero
Selecione 5 e insira o ID do gênero a ser deletado:
```console
ID do gênero a deletar: 3
Deletado com sucesso!
Pressione Enter para continuar...
```
### Gerenciar Filmes
Selecione a opção 2 no menu principal para acessar o menu de gerenciamento de filmes:
```console
--- Gerenciar Filmes ---
1. Listar Filmes
2. Buscar Filme por ID
3. Adicionar Filme
4. Atualizar Filme
5. Deletar Filme
0. Voltar
Escolha uma opção: 
```
### Listar Filmes
Selecione 1 para listar todos os filmes cadastrados:
```console
[1] O Poderoso Chefão - 175min - Lançamento: 1972-03-24 - Gênero: Drama - Avaliação: 4.9
[2] Pulp Fiction - 154min - Lançamento: 1994-10-14 - Gênero: Crime - Avaliação: 4.8
Pressione Enter para continuar...
```
### Buscar Filme por ID
Selecione 2 e insira o ID do filme para buscá-lo:
```console
ID do filme: 1
[1] O Poderoso Chefão - 175min - Lançamento: 1972-03-24 - Gênero: Drama - Avaliação: 4.9
Sinopse: A saga da família criminosa Corleone.
Pressione Enter para continuar...
```
### Adicionar Filme
Selecione 3 e insira os detalhes do novo filme. Campos como Avaliação e Sinopse são opcionais.
```console
Nome: O Senhor dos Anéis: A Sociedade do Anel
Duração (minutos): 178
Data de lançamento (YYYY-MM-DD): 2001-12-19
ID do gênero: 1 (Assumindo que 'Fantasia' tem ID 1)
Avaliação (0.5 a 5.0) [opcional]: 5.0
Sinopse [opcional]: Um jovem hobbit herda um anel mágico e embarca em uma jornada para destruí-lo.
Filme cadastrado com sucesso!
Pressione Enter para continuar...
```
### Atualizar Filme
Selecione 4, insira o ID do filme a ser atualizado e os novos detalhes. Você pode deixar os campos em branco para manter os valores existentes.
```console
ID do filme a atualizar: 3
Nome [O Senhor dos Anéis: A Sociedade do Anel]: O Senhor dos Anéis: As Duas Torres
Duração [178]: 179
Data de lançamento [2001-12-19]: 2002-12-18
ID do gênero [1]: 
Avaliação [5.0]: 4.9
Sinopse [Um jovem hobbit herda um anel mágico e embarca em uma jornada para destruí-lo.]: A jornada continua enquanto a Sociedade do Anel se divide.
Filme atualizado com sucesso!
Pressione Enter para continuar...
```
### Deletar Filme
Selecione 5 e insira o ID do filme a ser deletado:
```console
ID do filme a deletar: 3
Filme deletado com sucesso!
Pressione Enter para continuar...
```

## Testes
Para executar os testes da aplicação, utilize o pytest no diretório raiz do projeto:
```bash
pytest tests_app.py
```
## Cenários dos Testes Automatizados
Os testes automatizados garantem a funcionalidade e a integridade da aplicação. Abaixo estão os cenários de teste implementados:

### Testes de Gêneros

1. **Salvamento de Gênero**
- Dado que um novo objeto Genero é criado com um nome.
- Quando o método salvar() é chamado para este gênero.
- Então o gênero deve ser salvo no banco de dados e um ID deve ser atribuído a ele, e o gênero salvo deve ser recuperável pelo seu ID.

2. **Listagem de Gêneros**
- Dado que múltiplos gêneros foram salvos no banco de dados.
- Quando o método listar() da classe Genero é chamado.
- Então uma lista contendo todos os gêneros salvos deve ser retornada.

3. **Deleção de Gênero**
- Dado que um gênero existente está salvo no banco de dados.
- Quando o método deletar() é chamado para este gênero.
- Então o gênero deve ser removido do banco de dados e não deve ser mais recuperável pelo seu ID.

### Testes de Filmes

1. **Salvamento de Filme**
- Dado que um novo objeto Filme é criado com todos os detalhes, incluindo um genero_id válido.
- Quando o método salvar() é chamado para este filme.
- Então o filme deve ser salvo no banco de dados e um ID deve ser atribuído a ele, e o filme salvo deve ser recuperável pelo seu ID.

2. **Listagem de Filmes**
- Dado que múltiplos filmes foram salvos no banco de dados.
- Quando o método listar() da classe Filme é chamado.
- Então uma lista contendo todos os filmes salvos deve ser retornada.

3. **Deleção de Filme**
- Dado que um filme existente está salvo no banco de dados.
- Quando o método deletar() é chamado para este filme.
- Então o filme deve ser removido do banco de dados e não deve ser mais recuperável pelo seu ID.














