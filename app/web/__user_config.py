import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'fallback-secret-key'  # Clé secrète pour Flask
    SESSION_TYPE = 'filesystem'
    USERS = {
        'user': os.getenv('USER_PASSWORD_HASH') or 'fallback_password_hash',  # Mot de passe haché
    }
