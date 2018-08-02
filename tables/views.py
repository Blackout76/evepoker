from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from .models import Table, NewTableForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from users.models import User, UserStats
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decorators import esi_login_required

# display tables on home page
@esi_login_required
def tables(request):
	args = RequestContext(request)
	table_list = Table.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(table_list, 15)
	try:
		args['tables'] = paginator.page(page)
	except PageNotAnInteger:
		args['tables'] = paginator.page(1)
	except EmptyPage:
		args['tables'] = paginator.page(paginator.num_pages)

	return render_to_response('tables.html', args)

# Leave table REST interface
@csrf_exempt
def leaveTable(request):
	args = RequestContext(request)
	if request.method == 'POST':
	
		# Parse POST variables
		userid = request.POST['userid'];
		tableid = request.POST['tableid'];
		pot = request.POST['pot'];
		
		"""
		#update user balance
		user = UserStats.objects.get(user=userid)
		user.balance = user.balance+float(pot)
		user.save()
		"""
		
		#Change number of tables
		table = Table.objects.get(id=tableid)
		table.currentUsers = table.currentUsers-1
		table.save()
	return HttpResponse('UPDATED',status=200)
	
# join a table
@esi_login_required
def joinTable(request, tableID=1):
		
	#Update number of users
	table = Table.objects.get(id=tableID)
	table.currentUsers = table.currentUsers +1
	table.save()

	args = RequestContext(request)
	args['tables'] = table

	# Add User
	current_user = User.objects.get(character_id=request.session['char']['CharacterID'])

	args['table'] = table.id
	args['username'] = current_user.character_name
	args['id'] = current_user.character_id
	args['tableLimit'] = table.tableLimit
	args['tableBlind'] = table.tableBlind
	args['tableName'] = table.name
	args['tablePublic'] = table.public
	
	## Inject amount of player $$ into game
	args['amountPlay'] = table.tableBlind*25
	UserStats_t = current_user.user_stats
	UserStats_t.balance = UserStats_t.balance-args['amountPlay']
	UserStats_t.save()
	
	return render_to_response('game.html', args)


@esi_login_required
def newtable(request):
	if request.method == 'POST': # If the form has been submitted...
		# ContactForm was defined in the the previous section
		form = NewTableForm(request.POST) # A form bound to the POST data
		print (form.is_valid())
		print (form)
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...

			newTableEntry = Table(currentUsers=1, public=form.cleaned_data['public'], tableLimit=form.cleaned_data['tableLimit'], tableBlind=form.cleaned_data['tableBlind'], name=form.cleaned_data['name'] )
			newTableEntry.save()
			args = RequestContext(request)
			
			args['user'] = User(character_id=request.session['char']['CharacterID'])
			return redirect( '/tables/'+ str(newTableEntry.id));
	
	form = NewTableForm() # An unbound form
	return render(request, 'createTable.html', {'form': form})
	
	
