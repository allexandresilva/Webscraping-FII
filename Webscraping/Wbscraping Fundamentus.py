import requests
from bs4 import BeautifulSoup
import locale
from tabulate import tabulate
from Modelos import FundoImobiliario, Estrategia

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def trata_porcentagem(porcentagem_str):
    return locale.atof(porcentagem_str.split('%')[0])

def trata_decimal(decimal_str):
    return locale.atof(decimal_str)


''' É acrescentado este parametro "headers" ao método requests, pois o servidor do site fundamentus está esperando que a 
requisição(a troca de dados) seja feita por um browser, aqui estamos emulando esta troca de dados usando um código python 
'''
headers = {'User-Agent': 'Mozilla/5.0'}# headers é um dicionário

#Aqui é feita a requisição ao site onde será feito o webscraping, essa requisição estará armazenada na variável resposta
resposta = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)

'''
Aqui é feito a quebra dos dados da página funsamentus para que fique "compatível" com a linguagem python para que asim a
gente consiga manipulá-los da melhor forma'''
soup = BeautifulSoup(resposta.text, 'html.parser')

'''
Aqui foi feito este print para verificar se o parser foi feito corretamente, é neste print que o código HTML é mostrado '''
#print(soup.prettify())

'''
Aqui a variável 'linas' armazena os dados das linhas da tabela, a tabela foi encontrada através do seu id 
em "soup.find(id=tabelaResultado)" logo em seguida eliminamos a linha de cabeçalho com mais um find, como o find serve 
para nos dar entregar um ítem especíco, para 'eliminar' a linha do cabeçalho entramos na tabela e dentro da tabela 
entramos apenas nas linhas contendo os dados em ".find()'tdody" e por último, para encontrar as linhas com os dados que 
queremos utilizamos o fild_all() em ".fild_all('tr')", assim conseguimos os dados de todas as linhas da tabela'''
linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

'''
Criado um for para percorrer linha a linha e deixar a saída das linhas visualente melhor, mais fácil e intuitiva
for linha in linhas:
    dados_fundo = linha.find_all('td')
    print(
        f"[{dados_fundo[0].text}]\n"
        f"\tCotação: {dados_fundo[2].text}\n"
        f"\tSetor: {dados_fundo[1].text}\n"
        f"\tDY: {dados_fundo[4].text}\n"
        f"\tP/VP: {dados_fundo[5].text}\n"
    )'''
resultado = []

estrategia = Estrategia(
    cotacao_atual_minima=50.0,
    dividend_yield_minimo=5,
    p_vp_minimo=0.70,
    valor_mercado_minimo=200000000,
    liquidez_minima=50000,
    qt_minima_imoveis=5,
    maxima_vacancia_media=10
)

for linha in linhas:
    dados_fundo = linha.find_all('td')
    codigo = dados_fundo[0].text
    segmento = dados_fundo[1].text
    cotacao = trata_decimal(dados_fundo[2].text)
    ffo_yield = trata_porcentagem(dados_fundo[3].text)
    dividend_yield = trata_porcentagem(dados_fundo[4].text)
    p_vp = trata_decimal(dados_fundo[5].text)
    valor_mercado = trata_decimal(dados_fundo[6].text)
    liquidez = trata_decimal(dados_fundo[7].text)
    qt_imoveis = int(dados_fundo[8].text)
    preco_m2 = trata_decimal(dados_fundo[9].text)
    aluguel_m2 = trata_decimal(dados_fundo[10].text)
    cap_rate = trata_porcentagem(dados_fundo[11].text)
    vacancia_media = trata_porcentagem(dados_fundo[12].text)

    fundo_imobiliario = FundoImobiliario(
        codigo, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado, liquidez, qt_imoveis, preco_m2,
        aluguel_m2, cap_rate, vacancia_media
    )

    if estrategia.aplica_estrategia(fundo_imobiliario):
        resultado.append(fundo_imobiliario)

cabecalho = ["CÓDIGO", "SEGMENTO", "COTAÇÃO ATUAL", "DIVIDEND YIELD"]

tabela = []

for elemento in resultado:
    tabela.append([
        elemento.codigo,
        elemento.segmento,
        locale.currency(elemento.cotacao_atual),
        f'{locale.str(elemento.dividend_yield)} %'
    ])

print(tabulate(tabela, headers=cabecalho, showindex='always', tablefmt='fancy_grid'))
