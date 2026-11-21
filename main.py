from client import ConversorCoin
from utils import formatar_moeda


client = ConversorCoin()

conversion = int(client.conversor_coin('BTC', 'BRL'))

print(f'{formatar_moeda(conversion)}')
