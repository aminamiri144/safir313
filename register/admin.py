from django.contrib import admin
from .models import Kid
# Register your models here.
class KidAdmin(admin.ModelAdmin):
    list_display = ('codmeli', 'name', 'lastname', 'age', 'gender', 'phone')


admin.site.register(Kid, KidAdmin)