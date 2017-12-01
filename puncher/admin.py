# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Punch

class PuncherAdmin(admin.ModelAdmin):
	list_display = ["text","user_name","channel_name","team_domain","created_at"]
	search_fields = ["text","user_name","channel_name","team_domain"]
	class Meta:
		model = Punch

admin.site.register(Punch, PuncherAdmin)