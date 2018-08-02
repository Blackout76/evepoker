from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserStats
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from esi.esi import esi_app, esi_security, esi_verify

# get the profile
@login_required()
def profile(request):
	args = RequestContext(request)
	args['UserStats'] = get_object_or_404(UserStats, user=request.user)
	return render_to_response('profile.html', args)

"""
# register a new user 
@csrf_exempt 
def register(request):
	
	context = RequestContext(request)
	
	registered = False
	
	# we want to try and register a user
	if request.method == 'POST':
		
		# grab post data to user and stats forms
		user_form = UserForm(data=request.POST)
		stats_form = UserStatsForm(data = request.POST)
		
		if user_form.is_valid() and stats_form.is_valid():
		
			# save user
			user = user_form.save()
			
			# hash and save password
			user.set_password(user.password)
			user.save()
			
			# create associated user stats, commit after changes
			userstats = stats_form.save(commit=False)
			userstats.user = user
			userstats.balance = 100000
			
			if 'picture' in request.FILES:
				userstats.picture = request.FILES['picture']
			
			userstats.save()
			
			# we did it!
			registered = True
			
		# invalid form(s)
		else:
			print (user_form.errors)
			
	# not a POST, so just render the form
	else:
		user_form = UserForm()
		stats_form = UserStatsForm()
		
	# render template depending on context
	return render_to_response(
		'register.html',
		{'user_form': user_form, 'stats_form': stats_form, 'registered': registered},
		context)
		
# user login
@csrf_exempt 
def user_login(request):
	
	context = RequestContext(request)
	
	# theyre attempting to log in
	if request.method == 'POST':
	
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate
		(username=username, password=password)
		
		# we've got a user
		if user is not None:
		
			# is the account active (not banned)
			if user.is_active:
			
				login(request, user)
				return HttpResponseRedirect('/tables/')
			
			else:
				return HttpResponse("Your account is disabled")
			
		else:
			return HttpResponse("Invalid login details")
			
	# not post, so show form
	else:
		return render_to_response('login.html',{}, context)
"""
# user login
def user_login(request):
	"""
	if 'token' in request.session :
		esi_app, security, client, scopes = get_esi()
		try:
			security.update_token(request.session['token'])
		except APIException as err:
			print (err)
			secure = security.get_auth_uri(scopes=scopes)
			return HttpResponse("<a href='"+secure+"'><img src='" + ESI_CONNECT_IMG_BAR + "'></a>")
		try:
			verify = security.verify()
		except:
			secure = security.get_auth_uri(scopes=scopes)
			return HttpResponse("<a href='"+secure+"'><img src='" + ESI_CONNECT_IMG_BAR + "'></a>")
		request.session['char'] = verify
		return HttpResponseRedirect('/')
	else:
		secure = security.get_auth_uri(scopes=scopes)
		return HttpResponse("<a href='"+secure+"'><img src='" + ESI_CONNECT_IMG_BAR + "'></a>")
	"""
	return HttpResponseRedirect('/')

# user oauth
def oauth(request):
	print (request)
	code = request.GET.get('code')
	token = esi_security.auth(code)
	request.session['token'] = token
	request.session['char'] = esi_verify()

	"""
	user = UserStats.get_object(user_esi_id=id)
	
	# we've not got a user
	if user is None:
		# create associated user stats, commit after changes
		user = User(username="")
		userstats = UserStats()
		userstats.user = user
		userstats.balance = 0
		userstats.save()

	# is the account active (not banned)
	if not user.is_active:
		return HttpResponse("Your account is disabled")
	else:
	"""
	return HttpResponseRedirect('/tables/')


# user logout    
def user_logout(request):
	logout(request)
	return render_to_response('index.html',{})