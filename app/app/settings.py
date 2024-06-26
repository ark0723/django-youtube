from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-te&g_=21!5hk)_ga#xzxsdm3r#!e653s#bgib!x%rtfz-c8*n9'
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "u2NvK8HoPX")


# JWT 사용이유: 일반 token은 서버에 저장 -> 서버 부하가 생김, jwt는 시크릿키만 갖고 있으면 해독가능하고, 서버에 저장되지 않음

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", 0)))

ALLOWED_HOSTS = ["ec2-3-35-193-76.ap-northeast-2.compute.amazonaws.com", "3.35.193.76"]


# Application definitionㄴ
DJANGO_SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]

CUSTOM_USER_APPS = [
    "daphne",  # 제일 상단에 있어야
    "users.apps.UsersConfig",
    "rest_framework",
    "drf_spectacular",
    "videos.apps.VideosConfig",
    "comments.apps.CommentsConfig",
    "subscriptions.apps.SubscriptionsConfig",
    "reactions.apps.ReactionsConfig",
    "channels",
    "chat.apps.ChatConfig",
]

# channel 사용위한 설정
ASGI_APPLICATION = "app.route.application"  # socket (비동기처리() + HTTP (동기처리)
WSGI_APPLICATION = "app.wsgi.application"  # HTTP base -REST API (동기처리)

# FAST - API : 동기/비동기 모두 가능
# 동기와 비동기
# 스벅: 직원 1명 (동기) -> 녹차프라프치노 만들어야 -> 그 다음 내 차레
# 직원이 2명 이상 (비동기) -> 아아먼저 나올수도 (순서가 보장되지 않음): cpu(멀티스레드) -> 여러프로그램을 동시에 띄우는게 가능
# SOCKET - ws://, hand shake 양방향 통신이 가능해짐, Low Overhaed, Frame(웹소켓에서 데이터를 나누는 단위)
# streaming - 영상, 음성 어떻게 보내지? TCP/UDP, 3 ways handshake


INSTALLED_APPS = CUSTOM_USER_APPS + DJANGO_SYSTEM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

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
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# os.enriton: docker-compose.yml 에서 environment 불러온다

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django의 custom usermodel - 기존 장고의 유저 인증 기능을 가져온다.
AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}

CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
