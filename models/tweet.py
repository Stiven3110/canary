from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import INTEGER, String
from config.db import meta, engine

tweets = Table("tweets", meta, Column(
    "id", INTEGER, primary_key=True),
    Column("write", String(255)))

meta.create_all(engine)