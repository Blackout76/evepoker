from esipy import App, EsiClient, EsiSecurity
from esipy.exceptions import APIException
from .settings import ESI_URL, ESI_CONNECT_IMG_BAR, ESI_CLIENT_ID, ESI_SECRET_KEY, ESI_CALLBACK_URL, ESI_SCOPES

esi_app = App.create(ESI_URL)
esi_security = EsiSecurity(
	app = esi_app,
	redirect_uri = ESI_CALLBACK_URL,
	client_id = ESI_CLIENT_ID,
	secret_key = ESI_SECRET_KEY
	)
esi_client = EsiClient(security=esi_security)
esi_scopes = ESI_SCOPES

esi_secure = esi_security.get_auth_uri(scopes=esi_scopes)
esi_secure_url = "<a href='"+esi_secure+"'><img src='" + ESI_CONNECT_IMG_BAR + "'></a>"

def esi_update_token(request):
	esi_security.update_token(request.session['token'])

def esi_refresh_verify(request):
	esi_security.update_token(request.session['token'])
	esi_security.refresh()
	return esi_security.verify()

def esi_verify():
	return esi_security.verify()