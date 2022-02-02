from django.shortcuts import render

import requests

def main(request):
    base_url = 'https://sapi.coincarp.com/'
    route = 'api/v1/market/chain/holders'

    params = {
        'code': 'ethereum',
        'platform': '',
        'lang': 'en-US'
    }

    r = requests.get(base_url + route, params=params)

    h = r.json()['data']

    l = [holder['address'] for holder in h]
    d = [holder['quantity'] for holder in h]
    
    return render(request, 'ethparserapp/index.html', { 'labels': l, 'data': d }) 