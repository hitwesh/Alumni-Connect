import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Default configuration
class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'dev-key-replace-in-production')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    SESSION_COOKIE_SECURE = FLASK_ENV == 'production'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size