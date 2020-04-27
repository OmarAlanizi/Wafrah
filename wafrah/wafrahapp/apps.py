from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WafrahappConfig(AppConfig):
    name = 'wafrahapp'
    verbose_name = _('wafrahapp')
    
    # def ready(self):
    #     import wafrahapp.signals