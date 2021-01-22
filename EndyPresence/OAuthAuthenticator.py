import requests

class Oauth(object):
  client_id = '799634564875681792'
  client_secret = 'NLNhwnpsbkUjPgSAWheugxlNP0WA-FYb'
  scope = 'identify'
  redirect_uri = 'http://127.0.0.1:5000/login'
  discord_login_url = f'https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}'
  discord_token_url = f'https://discord.com/api/oauth2/token'
  discord_api_url = f'https://discord.com/api/'

  @staticmethod
  def get_access_token(code):
    data = {
      'client_id': Oauth.client_id,
      'client_secret': Oauth.client_secret,
      'grant_type': 'authorization_code',
      'code': code,
      'redirect_uri': Oauth.redirect_uri,
      'scope': Oauth.scope
    }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    access_token = requests.post(url = Oauth.discord_token_url, data = data, headers = headers)
    json = access_token.json()
    return json.get('access_token')

  @staticmethod
  def get_user_json(access_token):
    url = Oauth.discord_api_url + '/users/@me'

    headers = {
      "Authorization": f"Bearer {access_token}"
    }

    user_object = requests.get(url = url, headers = headers)
    user_json = user_object.json()
    return user_json
  
  @staticmethod
  def refresh_token(refresh_token):
    url = Oauth.discord_api_url + '/oauth2/token'

    data = {
      'client_id': Oauth.client_id,
      'client_secret': Oauth.client_secret,
      'grant_type': 'refresh_token',
      'refresh_token': refresh_token,
      'redirect_uri': Oauth.redirect_uri,
      'scope': 'identify'
    }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    refresh = requests.post(url = url, data = data, headers = headers)
    json = refresh.json()
    return json