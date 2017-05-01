from django.contrib import admin

from .models import Player, User, Ban, Appeal, Report
# Register your models here.

admin.site.register(Player)
admin.site.register(Ban)
admin.site.register(Appeal)
admin.site.register(Report)