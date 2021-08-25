from django.apps import AppConfig


class IpAddressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ip_address'
    verbose_name = 'Measurements between 2 locations'
