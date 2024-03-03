from django.contrib import admin
from .models import Subjects, Topics, Entries

# Register your models here.

admin.site.register(Subjects)
admin.site.register(Topics)
admin.site.register(Entries)

