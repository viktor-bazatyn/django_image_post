import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-+wz-ma9pdc%exs4xew@%4t1#)ge&a)xn8$yx5t-#yt)t4o*4+k"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "djangogramm",
    "users"
]


SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_REQUIRE_POST = True

AUTH_USER_MODEL = "users.CustomUser"
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = "base.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("POSTGRES_DB"),
#         "USER": os.environ.get("POSTGRES_USER"),
#         "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
#         "HOST": "bot_db",
#         "PORT": 5432,
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
MEDIA_ROOT = BASE_DIR / "media_files"
MEDIA_URL = "/media_files/"
STATIC_ROOT = BASE_DIR / "static"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    "social_core.backends.github.GithubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'users.pipeline.social_user',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

SOCIAL_AUTH_GITHUB_SCOPE = [
    'user:email',
    'read:user',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1038453178403-8voqut53r4hbqhn84uvatpvbfn6abhm0.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://127.0.0.1:8000/social-auth/complete/google-oauth2/'

SOCIAL_AUTH_GITHUB_KEY = "Ov23liILBiNdFY5iJB94"
SOCIAL_AUTH_GITHUB_SECRET = "2f9127abf169a7cbb7a903e76e944cf6edecf244"
SOCIAL_AUTH_GITHUB_REDIRECT_URI = 'http://127.0.0.1:8000/social-auth/complete/github/'