# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import user,blog2,blog1
from django.contrib import admin

# Register your models here.
admin.site.register(user)
admin.site.register(blog1)
admin.site.register(blog2)