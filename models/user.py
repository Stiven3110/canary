from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import INTEGER, String
from config.db import meta, engine

users = Table("users", meta, Column(
    "id", INTEGER, primary_key=True), 
    Column("name", String(255)), 
    Column("email", String(255)), 
    Column("password", String(255)))

