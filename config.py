import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    MONGO_URI = 'mongodb://localhost:27017/governance_db'
