# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone, formats

from .models import Punch

def index(request):
	return render(request,'punch/index.html')

def json(request):

	response = {}
	if request.method == 'POST':

		if request.POST.get('token') == 'EtxPklXPqHJt0QVs9QV8HKFM':

			commands = request.POST.get('text','').split(" ")
			commands = map(lambda x:x.lower(),commands)
			
			valid_commands = ['in','out','list','help']

			puncher_data = {
							'token' : request.POST.get('token',''),
							'team_id' : request.POST.get('team_id',''),
							'team_domain' : request.POST.get('team_domain',''),
							'channel_id' : request.POST.get('channel_id',''),
							'channel_name' : request.POST.get('channel_name',''),
							'user_id' : request.POST.get('user_id',''),
							'user_name' : request.POST.get('user_name',''),
							'command' : request.POST.get('command',''),
							'text' : request.POST.get('text',''),
							'response_url' : request.POST.get('response_url',''),
							}

			response['username'] = 'SlackPunch'
			if not commands[0] in valid_commands:
				response['text'] = 'That is not a valid argument. Type /punch help for instructions on how to use.'
			else:
				punch_type = commands[0]
				puncher = Punch(
								punch_type = punch_type,
								**puncher_data
								)
				puncher.save()

				if commands[0] == 'help':
					output_text = "Here is a list of arguments you can use:\n"

					output_text += "*/punch in* Records the time that you have logged in.\n"
					output_text += "*/punch out* Records the time that you have logged out.\n"
					output_text += "*/punch list <username>* Lists the last 10 logs for the user provided. *Replace <username> with the user you want to check.*"

					response['text'] = output_text

				elif commands[0] == 'in':

					response['response_type'] = "in_channel"
					response['text'] = "You've successfully punched in, {}".format(request.POST.get('user_name','brah'))

				elif commands[0] == 'out':
					
					response['response_type'] = "in_channel"
					response['text'] = "Til next time, {}".format(request.POST.get('user_name','brah'))

				else:
					if len(commands) >= 2:

						user_lookup = commands[1]
						output_text = ''
						punches = Punch.objects.filter(user_name = user_lookup).exclude(punch_type='list').exclude(punch_type='help').order_by('-created_at')[:10]

						counter = 1
						if len(punches) > 0:
							output_text += 'These are the last {0} logs for *{1}*'.format(len(punches), user_lookup)
							for punch in punches:
								formatted_date = formats.date_format(timezone.localtime(punch.created_at), 'Y-m-d g:i a')

								output_text += "\n"
								output_text += "{2}. Checked {0} at {1}".format(punch.punch_type, formatted_date, counter)
								counter += 1

							response['text'] = output_text

						else:
							response['text'] = 'No records found for {}'.format(user_lookup)

					else:
						response['text'] = "Please provide the username you'd like to check."

		else:
			response['text'] = 'Incorrect Team Token'

	return JsonResponse(response)