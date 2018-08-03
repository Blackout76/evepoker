from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from esi.esi import esi_secure_url, esi_update_token, esi_verify
from esipy.exceptions import APIException
from django.views.generic import TemplateView
from users.views import userCleanSession

def home(request):
	args = {}
	if 'token' in request.session :
		try:
			esi_update_token(request)
		except APIException as err:
			print (err)
			args['esi'] = esi_secure_url
			userCleanSession(request)
			return render(request, 'index.html', args)
		try:
			verify = esi_verify()
		except:
			args['esi'] = esi_secure_url
			userCleanSession(request)
			return render(request, 'index.html', args)

		request.session['char'] = verify
		return render(request, 'index.html', args)
	else:
		args['esi'] = esi_secure_url
		userCleanSession(request)
		return render(request, 'index.html', args)
	
def help(request):
	args = {}
	return render(request, 'help.html', args)
	