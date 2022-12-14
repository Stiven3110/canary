from sqlite3 import connect
from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///sql_app.db', connect_args={'check_same_thread': False})

meta = MetaData()

conn = engine.connect()