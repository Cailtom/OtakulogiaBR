from .environment import BASE_DIR

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'global_static',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / "staticfiles"
