# coding: utf-8
from django.contrib import admin
from accounts.admin import MoocUserAdmin
from django.contrib.auth import get_user_model
from .models import Campus

User = get_user_model()


class IfUserAdmin(MoocUserAdmin):
    model = User

    fieldsets = MoocUserAdmin.fieldsets + (
        (u'Informações dos IFs', {'fields': ('ifid', 'campus', 'city', 'course', 'klass', 'is_if_staff', 'cpf', 'siape',)}),
    )

admin.site.unregister(User)

admin.site.register(User, IfUserAdmin)
admin.site.register(Campus)
