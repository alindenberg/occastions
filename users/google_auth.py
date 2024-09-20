from google.oauth2 import id_token
from google.auth.transport import requests
from config import get_settings

settings = get_settings()


def verify_google_token(token: str):
    try:

        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        return idinfo
    except Exception as e:
        print("error is ", e)
        return None
    except ValueError:
        return None