from django.core.exceptions import PermissionDenied
from esi.esi import esi_update_token, esi_verify
from esipy.exceptions import APIException

def esi_login_required(function):
	def wrap(request, *args, **kwargs):
		if 'token' in request.session:
			try:
				esi_update_token(request)
			except APIException as err:
				print (err)
				raise PermissionDenied
			try:
				verify = esi_verify()
			except:
				raise PermissionDenied

			request.session['char'] = verify
			print (request.session['char'])
			return function(request, *args, **kwargs)
		else:
			raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap