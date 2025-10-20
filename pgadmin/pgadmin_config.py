import os
data_dir = "/var/lib/pgladmin"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Configurações padrão
DEFAULT_SERVER = 'postgres'
DEFAULT_SERVER_PORT = 5432
DEFAULT_DATABASE = 'postgres'
DEFAULT_USERNAME = 'postgres'

# Habilitar salvamento de senhas
CONFIG_DATABASE_URI = f'sqlite:///{data_dir}/pgadmin4.db'
