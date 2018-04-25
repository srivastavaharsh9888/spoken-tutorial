from __future__ import unicode_literals

from django.contrib import admin
from .models import foss,user,tutorial_detail,payment

admin.site.register(user)
admin.site.register(foss)
admin.site.register(tutorial_detail)
admin.site.register(payment)

