from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from esi.esi import esi_secure_url, esi_update_token, esi_verify
from esipy.exceptions import APIException

def home(request):
	args = RequestContext(request)

	if 'token' in request.session :
		try:
			esi_update_token(request)
		except APIException as err:
			print (err)
			args['esi'] = esi_secure_url
			return render_to_response('index.html', args)
		try:
			verify = esi_verify()
		except:
			args['esi'] = esi_secure_url
			return render_to_response('index.html', args)

		request.session['char'] = verify
		return render_to_response('index.html', args)
	else:
		args['esi'] = esi_secure_url

	return render_to_response('index.html', args)
	
def help(request):
	args = RequestContext(request)
	return render_to_response('help.html', args)
	