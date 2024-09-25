# Documentação de Instalação do Projeto Django

Este documento fornece instruções para instalar e executar o projeto Django usando Docker e também sem Docker.
Projeto foi codado no MacOS, Utilizando Postgres, docker, dockercompose e desenvolvido na IDE PyCharm.

## Instruções de Instalação e Configuração

### Pré-requisitos

- Python 3.11+
- Docker e Docker Compose (para configuração com Docker)
- PostgreSQL (para configuração sem Docker)

### Configuração do Banco de Dados

#### Com Docker

Ao usar Docker, o banco de dados será configurado automaticamente de acordo com as definições no `docker-compose.yml`. Não é necessário criar manualmente o banco de dados.

#### Sem Docker

1. Instale o PostgreSQL se ainda não estiver instalado.

2. Crie o banco de dados e o usuário:
   ```
   sudo -u postgres psql
   CREATE DATABASE "vcx-teste";
   CREATE USER teste WITH PASSWORD 'teste';
   GRANT ALL PRIVILEGES ON DATABASE "vcx-teste" TO teste;
   \q
   ```

3. Certifique-se de que o PostgreSQL está configurado para aceitar conexões do host `vcx-db-1`. Isso pode exigir ajustes no arquivo `pg_hba.conf` do PostgreSQL.

### Configuração com Docker

1. Clone o repositório:
   ```
   git clone https://github.com/artschur/work-at-vc-x-solutions.git
   cd work-at-vc-x-solutions
   ```

2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   DEBUG=True
   SECRET_KEY=sua_chave_secreta
   DATABASE_URL=postgres://teste:teste@vcx-db-1:5432/vcx-teste
   ```

3. Construa e inicie os containers:
   ```
   docker-compose up --build
   ```

4. Em outro terminal, execute as migrações:
   ```
   docker-compose exec web python manage.py migrate
   ```

6. Acesse a API em `http://localhost:8000/api/`

### Configuração sem Docker

1. Clone o repositório:
   ```
   git clone https://github.com/artschur/work-at-vc-x-solutions.git
   cd work-at-vc-x-solutions
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   DEBUG=True
   SECRET_KEY=sua_chave_secreta
   DATABASE_URL=postgres://teste:teste@localhost:5432/vcx-teste
   ```

5. Ajuste o arquivo `settings.py` para usar as configurações do banco de dados local:
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "vcx-teste",
           "USER": "teste",
           "PASSWORD": "teste",
           "HOST": "localhost",  # Mude para localhost quando não estiver usando Docker
           "PORT": "5432",
       }
   }
   ```

6. Execute as migrações:
   ```
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```

8. Acesse a API em `http://localhost:8000/api/`


