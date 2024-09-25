# Documentação de Instalação do Projeto Django

Este documento fornece instruções para instalar e executar o projeto Django usando Docker e também sem Docker.

## Instalação com Docker

### Pré-requisitos
- Docker
- Docker Compose


### Passos

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
   ```

2. Construa e inicie os containers:
   ```
   docker-compose up --build
   ```

3. Acesse o projeto em `http://localhost:8000`

## Instalação sem Docker

### Pré-requisitos
- Python 3.8+
- pip
- virtualenv (recomendado)

### Passos

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
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

4. Execute as migrações:
   ```
   python manage.py migrate
   ```
  4.1: c

5. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```

6. Acesse o projeto em `http://localhost:8000`

]

Lembre-se de configurar as variáveis de ambiente necessárias, como chaves secretas e configurações de banco de dados, conforme especificado no arquivo de configuração do seu projeto.
