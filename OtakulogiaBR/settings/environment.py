from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = bool(os.getenv('DEBUG'))
ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = 'OtakulogiaBR.urls'
WSGI_APPLICATION = 'OtakulogiaBR.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
