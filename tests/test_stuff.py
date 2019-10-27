import unittest
import pytest
import pandas as pd
import datetime
from src.stuff import get_operations_dataframe, calcula_precos_medio_de_compra


class TestStuff(unittest.TestCase):

    def test_calcula_precos_medios_do_dropbox(self):
        from src.dropbox_files import download_dropbox_file
        download_dropbox_file()

        df = get_operations_dataframe()

        precos_medios_de_compra = calcula_precos_medio_de_compra(df)
        assert type(precos_medios_de_compra) is dict

    def test_calcula_precos_medios_quando_um_ciclo(self):
        data = [{'ticker': 'gcgs', 'qtd': 100, 'data': datetime.date(2019, 4, 20), 'preco': 100},
                {'ticker': 'gcgs', 'qtd': 200, 'data': datetime.date(2019, 4, 13), 'preco': 200}]

        df = pd.DataFrame(data)

        precos_medio_de_compra = calcula_precos_medio_de_compra(df)

        assert precos_medio_de_compra['gcgs'] == pytest.approx(166.66, 0.01)

    def test_calcula_precos_medios_quando_varios_ciclo(self):
        data = [{'ticker': 'gcgs', 'qtd': 100, 'data': datetime.date(2019, 4, 11), 'preco': 100},
                {'ticker': 'gcgs', 'qtd': -100, 'data': datetime.date(2019, 4, 12), 'preco': 200},
                {'ticker': 'gcgs', 'qtd': 100, 'data': datetime.date(2019, 4, 13), 'preco': 300},
                {'ticker': 'gcgs', 'qtd': 100, 'data': datetime.date(2019, 4, 14), 'preco': 400},
                {'ticker': 'gcgs', 'qtd': -200, 'data': datetime.date(2019, 4, 15), 'preco': 500},
                {'ticker': 'gcgs', 'qtd': 2, 'data': datetime.date(2019, 4, 15), 'preco': 5},
                {'ticker': 'gcgs', 'qtd': -1, 'data': datetime.date(2019, 4, 15), 'preco': 1},
                {'ticker': 'gcgs', 'qtd': 3, 'data': datetime.date(2019, 4, 15), 'preco': 2},
                {'ticker': 'gcgs', 'qtd': 1, 'data': datetime.date(2019, 4, 16), 'preco': 2}]

        df = pd.DataFrame(data)

        precos_medio_de_compra = calcula_precos_medio_de_compra(df)

        assert precos_medio_de_compra['gcgs'] == pytest.approx(3, 0.001)