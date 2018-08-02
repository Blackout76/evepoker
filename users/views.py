from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import User, UserStats
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from esi.esi import esi_secure, esi_security, esi_verify

# get the profile
@login_required()
def profile(request):
	args = RequestContext(request)
	args['UserStats'] = get_object_or_404(UserStats, user=request.user)
	return render_to_response('profile.html', args)

# user login
def user_login(request):
	return HttpResponseRedirect(esi_secure)

# user oauth
def oauth(request):
	print (request)
	code = request.GET.get('code')
	token = esi_security.auth(code)
	request.session['token'] = token
	request.session['char'] = esi_verify()

	user = User(character_id=request.session['char']['CharacterID'])

	if user is None:
		# Create new user
		user = User()
		user.character_id = request.session['char']['CharacterID']
		user.character_name = request.session['char']['CharacterName']
		user.user_stats = UserStats()
		user.user_stats.balance = 0
		user.save()
	return HttpResponseRedirect('/tables/')


# user logout    
def user_logout(request):
	logout(request)
	return render_to_response('index.html',{})