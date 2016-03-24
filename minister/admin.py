from django.contrib import admin

# Register your models here.
from minister import models
admin.site.register(models.coreauth.UserProfile)