from common import *

{% if cookiecutter.use_celery == 'y' %}
########## CELERY
# In development, all tasks will be executed locally by blocking until the task returns
CELERY_ALWAYS_EAGER = True
########## END CELERY
{% endif %}
{% if cookiecutter.use_heroku == 'y' or cookiecutter.use_heroku == 'Y' %}
########## HEROKU
# Replace this with your heroku app url
ALLOWED_HOSTS = ['*']
########## END HEROKU
{% endif %}