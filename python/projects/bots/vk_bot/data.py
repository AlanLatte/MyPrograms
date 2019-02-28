import requests
def data_get(URL, method, function, access_token, version, user_ids):
    url = URL+method+function+user_ids+access_token+version
    print(requests.get(url).text)
    print(url)
