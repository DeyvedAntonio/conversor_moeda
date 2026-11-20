import requests


def conversor(coin_origin, coin_target):
    response = requests.get(
        url=f'https://economia.awesomeapi.com.br/last/{coin_origin}-{coin_target}'
    )

    if response.status_code == 404:
        return response.json().get('message')

    return response.json()[f'{coin_origin}{coin_target}']['bid']


print(conversor('BTC', 'BRL'))
