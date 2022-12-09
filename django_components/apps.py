from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    name = "django_components"

    def ready(self):
        self.module.autodiscover()
def medium(auto):
#     replace with above class
