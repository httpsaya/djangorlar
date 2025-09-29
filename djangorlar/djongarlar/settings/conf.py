#Project Modules
from decouple import config
# ----------------------------------------------
# Env id
#
ENV_POSSIBLE_OPTIONS = (
    "local",
    "prod",
)
ENV_ID = config("DJANGORLAR_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure-e12&pfehe6!xy(z^38n9n6qnoq=ub9+mme_o(l$p$_*u6$w3qp'
