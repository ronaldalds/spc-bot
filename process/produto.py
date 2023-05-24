import time
# from driver.mk.coin.coin import Estoque
from driver.mk.aside.aside_estoque import EstoqueHome
# from driver.mk.mk_driver import Mk
import os


# def unidade(value) -> int:
#     if value == 'Bloco':
#         return 19


# def cadastroProduto(
#         descricao,
#         categoria,
#         und,
#         inativo,
#         trabalho,
#         serial,
#         mobile
# ):
#     isInativo: bool = True if inativo == 'Sim' else False
#     isTrabalho: bool = True if trabalho == 'Sim' else False
#     isSerial: bool = True if serial == 'Sim' else False
#     isMobile: bool = True if mobile == 'Sim' else False

#     instance = Mk(
#         username=os.getenv('USERNAME'),
#         password=os.getenv('PASSWORD'),
#         url=os.getenv('URL'),
#     )

#     estoque = Estoque()
#     estoqueHome = EstoqueHome()

#     instance.login()

#     instance.iframeCoin()
#     instance.click(estoque.xpath())

#     instance.minimizeChat()

#     instance.iframePainel(coin=estoque, aside=estoqueHome)
#     instance.click('//button[@title="Novo Produto"]')

#     instance.iframeForm()
#     instance.write(
#         xpath='//input[@title="Informe uma breve descrição para o produto"]',
#         text=descricao
#     )

#     instance.click(
#         '//div[@title="Informe a unidade de comercialização do produto"]/div/button')
#     instance.click(f'//option[text()="{und}"]')

#     instance.click(
#         '//div[@title="Informe a categoria do produto"]/div/button')
#     instance.click(f'//option[text()="{categoria}"]')

#     if isInativo:
#         instance.click('//div[@title="Inativar produto."]')

#     if isTrabalho:
#         instance.click(
#             '//div[@title="Informe se esse produto é um material restrito para uso interno da empresa. "]')

#     if isSerial:
#         instance.click('//div[@title="Marque essa opção para ativar o controle serial desse produto. Ao ativar essa opção as movimentações serão controladas por um código único informado no cadastro de Seriais/MAC."]')

#     if isMobile:
#         instance.click('//div[@title="Sincronizar com mobile."]')

#     print(descricao,
#           categoria,
#           und,
#           inativo,
#           trabalho,
#           serial,
#           mobile)

#     time.sleep(10)
#     instance.close()
#     return descricao

