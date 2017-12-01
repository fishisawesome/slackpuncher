# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Punch(models.Model):
	token = models.CharField(max_length=255)
	team_id = models.CharField(db_index=True,max_length=255)
	team_domain = models.CharField(db_index=True,max_length=255)
	channel_id = models.CharField(db_index=True,max_length=255)
	channel_name = models.CharField(db_index=True,max_length=255)
	user_id = models.CharField(db_index=True,max_length=255)
	user_name = models.CharField(db_index=True,max_length=255)
	command = models.CharField(db_index=True,max_length=255)
	text = models.CharField(db_index=True,max_length=255)
	response_url = models.CharField(max_length=255)
	punch_type = models.CharField(db_index=True,max_length=10,default='list')
	created_at = models.DateTimeField(db_index=True,auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(db_index=True,auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.text

	def __str__(self):
		return self.text