from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator

db_url = 'postgresql://user:senha@localhost:15432/northwind'
engine = create_engine(db_url)
metadata = MetaData(bind=engine)

schema = 'northwind'
metadata.reflect(engine, schema=schema)

generator = CodeGenerator(metadata)
with open('models/northwind_models.py', 'w', encoding='utf-8') as f:
    generator.render(f)
