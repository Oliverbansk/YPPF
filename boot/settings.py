import os
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from boot import base_get_setting

# LOGIN_URL，未登录时重定向到的 URL
LOGIN_URL = base_get_setting('url/login_url')
# LOGIN_URL = local_dict["url"]["login_url"]
# LOGIN_URL = 'http:localhost:8000/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k+8az5x&aq_!*@%v17(ptpeo@gp2$u-uc30^fze3u_+rqhb#@9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_apscheduler",
    "generic",
    "app",
    "Appointment",
    'dm',
    "scheduler",
    "yp_library",
]

AUTH_USER_MODEL = 'generic.User'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "boot.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "boot.wsgi.application"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.AllowAllUsersModelBackend"]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    # 使用自己的数据库的时候请修改这里的配置
    # 注意underground数据库需要事先创建
    # mysql -u root -p
    # create database underground charset='utf8mb4';
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": base_get_setting('database/NAME'), # local_dict["database"]["NAME"],
        "HOST": base_get_setting('database/HOST', default='127.0.0.1', raise_exception=False),
        "PORT": 3306,
        "USER": base_get_setting('database/USER'), # local_dict["database"]["USER"],
        "PASSWORD": base_get_setting('database/PASSWORD'), # local_dict["database"]["PASSWORD"],
        'OPTIONS': {
            'charset': 'utf8mb4',
        #     "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# 加快测试时的数据导入速度，降低加密算法的迭代次数
# 正式上线时要去掉这里！如果先导入数据再修改hasher可能会出现账号无法登录！
# if DEBUG:
#     PASSWORD_HASHERS = [
#         "utils.hasher.MyPBKDF2PasswordHasher",
#     ]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'


LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

# 是否启用数据的本地化格式，如果开启将会导致django以他认为的本地格式显示后台数据
# 主要表现为时间的呈现形式变为年/月/日 小时:分钟 关闭时则为yyyy-mm-dd HH:MM:SS
# 关闭后，后台才能正常显示秒并进行修改
# 本地化有其他副作用，比如其他前端呈现的兼容
# 不想关闭可以调整django/conf/locale/zh_Hans/format.py中的TIME_INPUT_FORMATS顺序
# 而该文件中的其它变量被证明对后台呈现无效
# https://docs.djangoproject.com/zh-hans/3.1/ref/settings/#use-i18n
USE_L10N = True

# USE_TZ限制了Datetime等时间Field被存入数据库时是否必须包含时区信息
# 这导致定时任务和常用的datetime.now()等无时区时间在存入时被强制-8h转化为UTC时间
# 从而使数据库可读性差，存储前需要强制增加时区信息，且发送消息容易出错
# 从数据库取出的数据将是有时区信息的，几乎与datetime.now()不可比
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
MY_STATIC_DIR = os.getenv("YPPF_STATIC_DIR", BASE_DIR)
MY_TMP_DIR = os.getenv("YPPF_TMP_DIR", BASE_DIR)
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(MY_STATIC_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(MY_STATIC_DIR, "media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 标识环境、相关的端口和日志设置
MY_ENV = os.getenv("YPPF_ENV", "")

# port
MY_RPC_PORT = os.getenv("YPPF_SCHEDULER_PORT", 6666)
# MY_LIB_RPC_PORT = os.getenv("YPPF_SCHEDULER_PORT", 6699)
MY_INNER_PORT = os.getenv("YPPF_INNER_PORT", 80)

# LOG
MY_LOG_DIR = os.getenv("YPPF_LOG_DIR", BASE_DIR)
MY_LOG_LEVEL = logging.DEBUG if os.getenv("YPPF_LOG_DEBUG", "") else logging.INFO
MY_SCHEDULER_LOG = os.getenv("YPPF_SCHEDULER_LOG_FILE", "scheduler.log")

if MY_ENV in ["PRODUCT", "TEST"]:
    # Set cookie session domain to allow two sites share the session
    SESSION_COOKIE_DOMAIN = os.environ["YPPF_SESSION_COOKIE_DOMAIN"]
    if MY_ENV == "PRODUCT":
        SECRET_KEY = os.environ["YPPF_SECRET_KEY"]

if MY_ENV == "SCHEDULER":
    assert MY_SCHEDULER_LOG != "scheduler.log"

if MY_ENV == "INNER":
    pass

'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
'''