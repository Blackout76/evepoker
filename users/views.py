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
	args = {}
	#args['UserStats'] = get_object_or_404(UserStats, user=request.user)
	return render_to_response('profile.html', args)

# user login
def user_login(request):
	return HttpResponseRedirect(esi_secure)

# user oauth
def oauth(request):
	code = request.GET.get('code')
	token = esi_security.auth(code)
	request.session['token'] = token
	request.session['char'] = esi_verify()

	user = User.objects.filter(character_id=request.session['char']['CharacterID']).first()

	if user is None:
		# Create new user
		user = User()
		user.character_id = request.session['char']['CharacterID']
		user.character_name = request.session['char']['CharacterName']
		user_stats = UserStats(balance=59879896.56)
		user_stats.save()
		user.user_stats = user_stats
		user.save()

	request.session['userinfo'] = user.getInfo()

	return HttpResponseRedirect('/tables/')

def userCleanSession(request):
	for key in request.session.keys():
		del request.session[key]

# user logout    
def user_logout(request):
	for key in request.session.keys():
		del request.session[key]
	return HttpResponseRedirect('/',{})