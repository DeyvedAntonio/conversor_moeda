import requests


class ConversorCoin:

    def __init__(self) -> None:
        self.__base_url = 'https://economia.awesomeapi.com.br/last/'

    def conversor_coin(self, coin_origin, coin_target):
        response = requests.get(
            f'{self.__base_url}{coin_origin}-{coin_target}'
        )

        if response.status_code == 404:
            return response.json().get('message')

        return response.json()[f'{coin_origin}{coin_target}']['bid']
