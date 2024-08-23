INSTALLED_APPS = [
    # Default Django apps...
    'rest_framework',
    'api',  # Add your API app here
]

# Allow requests from your frontend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
