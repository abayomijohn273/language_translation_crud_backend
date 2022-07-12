from django.contrib import admin
from translatorcrud.models import TranslationsModel

class TranslationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(TranslationsModel, TranslationsAdmin)
