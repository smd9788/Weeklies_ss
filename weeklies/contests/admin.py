from django.contrib import admin

from .models import Contest
admin.site.register(Contest)

from .models import SecurityPool
admin.site.register(SecurityPool)

from .models import Security
admin.site.register(Security)