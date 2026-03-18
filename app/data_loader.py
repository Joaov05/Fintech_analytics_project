from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://postgres:0000@localhost:5432/fintech_analytics")

def load_data():
    users = pd.read_sql("SELECT * FROM users", engine)
    events = pd.read_sql("SELECT * FROM events", engine)
    transactions = pd.read_sql("SELECT * FROM transactions", engine)
    accounts = pd.read_sql("SELECT * FROM accounts", engine)
    
    return users, events, transactions, accounts