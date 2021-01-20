#Programa 4.6 - Distância percorrida

distância = float(input('Digite a distância a percorrer: '))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.45 * distância
print(f'Preço da passagem: R$ {passagem:7.2f}', '- Tá Caro né -?')
