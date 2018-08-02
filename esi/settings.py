from evepoker.settings import SERVER_PORT

ESI_URL = "https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility"
ESI_CONNECT_IMG_BAR = "https://images.contentful.com/idjq7aai9ylm/4fSjj56uD6CYwYyus4KmES/4f6385c91e6de56274d99496e6adebab/EVE_SSO_Login_Buttons_Large_Black.png?w=270&h=45"
ESI_CLIENT_ID = '2926603edc55498c9d6530a0f87f8bb5'
ESI_SECRET_KEY = 'AM5ParxVHSt2M8fqPlJv0F33gdGNhgrOMp8Sjl9k'
ESI_CALLBACK_URL = "http://localhost:"+str(SERVER_PORT)+"/users/oauth"
ESI_SCOPES = []