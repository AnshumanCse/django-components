from django.apps import AppConfig

# ********Main**code*********

class ComponentsConfig(AppConfig):
    name = "django_components"

    def ready(self):
        self.module.autodiscover()
