# PostgreSQL + PostGIS + pgAdmin Docker Setup

Este projeto configura um ambiente completo de PostgreSQL com extensão PostGIS e interface pgAdmin usando Docker Compose.

## 🚀 Recursos

- **PostgreSQL 17** com extensão PostGIS 3.5
- **pgAdmin 4** com configuração automática de servidores
- **Backup automático** dos bancos de dados
- **Rede Docker** isolada para comunicação entre containers
- **Volumes persistentes** para dados e configurações

## 📋 Pré-requisitos

- Docker
- Docker Compose
- Git

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone https://github.com/vitfera/postgres_docker.git
cd postgres_docker
```

2. Crie o arquivo `.env` baseado no exemplo:
```bash
cp .env.example .env
```

3. Ajuste as configurações no arquivo `.env`:
```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGLADMIN_DEFAULT_PASSWORD=admin
```

## 🚀 Como usar

### Iniciar os serviços
```bash
docker compose up -d
```

### Parar os serviços
```bash
docker compose down
```

### Ver logs
```bash
docker compose logs -f
```

## 🌐 Acesso aos serviços

### PostgreSQL
- **Host:** `localhost`
- **Porta:** `40010`
- **Usuário:** `postgres`
- **Senha:** `postgres`
- **Banco:** `postgres`

### pgAdmin
- **URL:** http://localhost:40012
- **Email:** `admin@example.com`
- **Senha:** `admin`

## 📊 Conectando no pgAdmin

1. Acesse http://localhost:40012
2. Faça login com as credenciais configuradas
3. Os servidores PostgreSQL são registrados automaticamente
4. Para conexão manual:
   - Host: `postgres`
   - Porta: `5432`
   - Usuário: `postgres`
   - Senha: `postgres`

## 📁 Estrutura do projeto

```
.
├── docker-compose.yml          # Configuração dos containers
├── .env                        # Variáveis de ambiente
├── initdb/                     # Scripts de inicialização do banco
│   └── 001_schema.sql         # Schema inicial
├── pgadmin/                    # Configurações do pgAdmin
│   ├── servers.json           # Servidores pré-configurados
│   └── pgpass                 # Arquivo de senhas
└── README.md                  # Este arquivo
```

## 🔧 Importar dumps

Para importar um dump SQL:

```bash
# Copie o dump para o container
docker cp seu_dump.sql postgres_postgis:/tmp/

# Execute o dump
docker exec postgres_postgis su - postgres -c "psql < /tmp/seu_dump.sql"
```

## 📦 Volumes

- `pg_data`: Dados do PostgreSQL
- `pgadmin_data`: Configurações do pgAdmin

## 🛠️ Troubleshooting

### Erro de autenticação
Se houver problemas de conexão, redefina a senha:
```bash
docker exec postgres_postgis su - postgres -c "psql -c \"ALTER USER postgres PASSWORD 'postgres';\""
```

### Resetar dados
Para começar com dados limpos:
```bash
docker compose down
docker volume rm postgres_pg_data postgres_pgadmin_data
docker compose up -d
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.