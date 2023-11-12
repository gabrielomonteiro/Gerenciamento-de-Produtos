from classes import Usuario, Produtos, Clientes, Vendas
import unittest
import os
import pandas as pd


class TestProdutos(unittest.TestCase):

  def setUp(self):
    # Inicializa o objeto Produtos para os testes
    self.produtos = Produtos()

  def test_criar_tabela(self):
    # Testa se criar uma tabela de produtos resulta na criação do arquivo
    self.produtos.criar_tabela()
    self.assertTrue(os.path.exists('produtos.xlsx'))

  def test_cadastrar_produto(self):
    # Testa se um novo produto é adicionado com sucesso à tabela
    self.produtos.cadastrar_produto('TestProduct', 10, '50.00')
    df = pd.read_excel('produtos.xlsx')
    self.assertTrue('TestProduct' in df['Nome'].values)


class TestClientes(unittest.TestCase):

  def setUp(self):
    # Inicializa o objeto Clientes para os testes
    self.clientes = Clientes()

  def test_criar_tabela(self):
    # Testa se criar uma tabela de clientes resulta na criação do arquivo
    self.clientes.criar_tabela()
    self.assertTrue(os.path.exists('clientes.xlsx'))

  def test_validar_nome_cliente(self):
    # Testa a validação do nome do cliente para entrada válida
    self.assertTrue(self.clientes.validar_nome_cliente('Lucas Oliveira'))

  def test_validar_nome_cliente_invalido(self):
    # Testa a validação do nome do cliente para entrada inválida (números)
    self.assertFalse(self.clientes.validar_nome_cliente('1234'))

  def test_validar_telefone(self):
    # Testa a validação do telefone para entrada válida
    self.assertTrue(self.clientes.validar_telefone('(12) 34567-8901'))

  def test_validar_telefone_invalido(self):
    # Testa a validação do telefone para entrada inválida
    self.assertFalse(self.clientes.validar_telefone('123.456.789-10'))



class TestVendas(unittest.TestCase):

  def setUp(self):
    # Inicializa o objeto Vendas para os testes
    self.vendas = Vendas()

  def test_criar_tabela(self):
    # Testa se criar uma tabela de vendas resulta na criação do arquivo
    self.vendas.criar_tabela()
    self.assertTrue(os.path.exists('vendas.xlsx'))

  def test_cadastrar_venda(self):
    # Testa se uma nova venda é adicionada com sucesso à tabela
    self.vendas.cadastrar_venda('TestClient', 'TestProduct', 5)
    df = pd.read_excel('vendas.xlsx')
    self.assertTrue('TestClient' in df['Cliente'].values)

  def test_atualizar_estoque(self):
    # Testa se o estoque é atualizado corretamente após uma venda
    self.vendas.cadastrar_venda('TestClient', 'TestProduct', 5)
    df_produtos = pd.read_excel('produtos.xlsx')
    self.assertEqual(int(df_produtos[df_produtos['Nome'] == 'TestProduct']['Quantidade']), 5)





if __name__ == '__main__':
    unittest.main()
