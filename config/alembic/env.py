from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from conectDb import create_engine_db
from models import metadata
engine =create_engine_db()

config = context.config

config.set_main_option('sqlalchemy.url', engine.url)

target_metadata = metadata

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)
    with connectable.connect() as connection:
        try:
            context.configure(connection=connection, target_metadata=None)

            with context.begin_transaction():
                context.run_migrations()
        except Exception as e:
            return e

