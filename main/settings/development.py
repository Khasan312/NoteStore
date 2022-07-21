from .base import *

AUTH_USER_MODEL = 'account.User'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notebook_db',
        'USER': 'khasan',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hasan.ucuturkiye@gmail.com'
EMAIL_HOST_PASSWORD = 'dczxnmnunzbcqbxn'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


import moneyed

BOB = moneyed.add_currency(
    code='SOM',
    numeric='068',
    name='Kyrgyz Money',
    countries=('Kyrgyzstan', )
)

CURRENCIES = ('USD', 'SOM')
CURRENCY_CHOICES = [('USD', 'USD $'), ('SOM', 'SOM €')]