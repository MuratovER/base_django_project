"""
For any new app, we need co config it.

~apps/example/apps.py
from django.apps import AppConfig

class ExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.example'

where "example" is your app name
"""