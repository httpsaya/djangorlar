from decouple import config 

ENV_POSSIBLE_PTIONS = (
    'local',
    'prod',
)
ENV_ID = config("PRACTICE_6_ENV_ID", default= 'local')
SECRET_KEY = config('PRACTICE_SECRET_KEY')