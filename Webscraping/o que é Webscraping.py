'''
O QUE É WEBSCRAPING?

>> Processo de coleta de dados da internet de maneira automatizada
>> Atualmente tem enorme valor
>> Esses dados podem auxiliar na tomada de de cisção d empresas ou ser utilizado por você para construção de alguna
aplicação pessoal. Ex.: Se curte esportes, pode ser criado um webscraping para obter informações/notícias do seu time.
>> ALGUNS CASOS DE USO:
    * Monitoração de preços
    * Monitoração de notícias
    * Geração de Leads(Leads são potenciais clientes, baseados em informações das pessoas em suas redes sociais por
    exemplo)
    * Pesquisa de mercado(Uma empresa pretende desenvolver um produto, esta pode ir na internet para saber como esta o
    produto, se está sendo bem divulgado, a procura por este produto ... Pra assim tomar a decisão de implementar/melhorar
    ou retirar do mercado)

FUNDAMENTOS DE WEBSCRAPING

CPNCEITOS IMPORTANTES
    * CRAWLER:
    Navega na página web alvo mapeando todas as páginas, caminhos, links (intenos e externos), formulários, recursos
    para download, etc.
    É um processo automatizado que fará a descoberta de páginas web, navegando como se fosse um ser-humano nestas páginas,
    hoje um dos CRAWLER mais poderoso é o do GOOGLE.

    * PARSING:
    Análise sintática da página web, transformando o código HTML em uma representação mais fácil de ser processada.
    HTML é a estrutura de script que são construídas as páginas da web.

    * SCRAPER:
    Extrai os dados da página através de seletores CSS, tags HTML, expressões regulares, XPath ou uma combinação deles.
    Necessita conhecimento prévio da página. Existem métodos para se dificultar esse processo(ofuscação).

    * OFUSCAÇÃO:
    Técnica utilizada para "embaralhar" os dados da página, dificultando ou impossibilitando o processo de webscraping.

PASSO A PASSO PARA REALIZAR WEBSCRAPING

    1º - Aquisição da página HTML
    2º - Processamento de dados
    3º - Geração de informação

NOSSO PROJETO =====

    * Faremos scraping da página FUNDAMENTOS(https://fundamentos.com.br)
    * Nada que for dit odeve ser interpretado como recomendação de investimento, o intúito é desenvolver habilidades de
    programação.

Vamos utilizar as seguintes ferramentas: BIBLIOTECAS
    * Requests: Realiza requisições HTTP
    * BeautifulSoup: Biblioteca que facilita o parsing de páginas HTML
    * Tabulate: Biblioteca para formatar dados no Terminal

PÚBLICO ALVO

FUNDAMENTOS DA INTERNET
    A internet foi desenhada a partir de uma Arquitetura Cliente-Servidor.
    Essa Arquitetura possui dois Atores com responsabilidades bem definidas:

    * CLIENTE:
    Parte ATIVA da Arquitetura, é quem pede informações ao Servidor.

    * SERVIDOR:
    Parte PASSIVA da Arquitetura, é quem aguarda as requisições dos Clientes.

O QUE É HTML?
    * Sigla para HyperTextMarkupLanguage(Linguagem de Marcação de Hipertexto)
    * O HTML usa "MARCAÇÃO"(tags) para anotar texto, imagem e outros contúdos para exibição em um navegador da web.
    * Todas as páginas da web conversam páginas em HTML

    Estrutura básica de uma página HTML

    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UFT-8"/>
    <title>Document</title>
    </head>
    <body>
    <!-- Conteúdo -->
    <body>
    </html>

    * Juntamente com CSS e Javascript, formam a linguagem da internet

O QUE É CSS?
    * Sigla para Cascading Style Sheets
    * Adiciona estilo à páginas HTML
    * Muito importante para deixar sites atraentes
    * Para aplicar estilos, escrevemos classes CSS
    * Classes CSS são aplicadas à elementos da página através do atributo "class"
        <div class="center dinheiro">

    div.center.dinheiro {
        background: >url(../img/dinheiro.jpg) no-repeat right 200px;
    {
    div.center {
    widh: 1000px;
    margin:> 0 auto!important;
    position: relative;
    }

    * Utilizamos essas classes para buscar informações ao fazer Webscraping!

O QUE É JAVASCRIPT
    * Linguagem de programação leve utilizada para dinamicidade às páginas web.

COMO ANALISAR PÁGINAS WEB
    * Já sabemos que é necessário analisar a página-alvo antes de iniciar qualquier projeto de Webscraping
    * Uma das ferramentas mais utilizadas ára este fim são as "Ferramentas de Desenvolvedor" dos navegadores mais modernos

'''


