from django.contrib import admin

# Register your models here .
from minister import models
from asset import admin as asset_admin
admin.site.register(models.coreauth.UserProfile)
