from django.test import TestCase
from contacts.models import ContatoSerializerv1, ContatoSerializerv2


class TestContatoSerializers(TestCase):
    # Cria as informações de contatos para Versão 1 e Versão 2
    def setUp(self):
        self.contato_data_v1 = {
            "name": "Teste v1",
            "cellular": "+5511999999999",
        }
        self.contato_data_v2 = {
            "name": "Teste v2",
            "cellular": "+5511999999999",
            "email": "contato.v2@teste.com",
            "region": "BR",
        }

    # # Verifica se o serializer v1 funciona corretamente com os dados fornecidos.
    # def test_contato_serializerv1_valid(self):
    #     # Cria o serializer com as informações criadas no passo anterior
    #     serializer = ContatoSerializerv1(data=self.contato_data_v1)
    #     # Testa para ver se o serializer foi criado Corretamente ou deu Erro.
    #     self.assertTrue(serializer.is_valid())

    # # Verifica se o serializer v2 funciona corretamente com os dados fornecidos.
    # def test_contato_serializerv2_valid(self):
    #     # Cria o serializer com as informações criadas no primeiro passo.
    #     serializer = ContatoSerializerv2(data=self.contato_data_v2)
    #     # Testa para ver se o serializer foi criado Corretamente ou deu Erro.
    #     self.assertTrue(serializer.is_valid())

    # # Verifica se o serializer v2 funciona corretamente com um campo não obrigatório faltante.
    # def test_contato_serializerv2_invalid_missing_field(self):
    #     # Duplica a data do json da segunda Versão para não alterar o campo original
    #     invalid_data = self.contato_data_v2.copy()
    #     # Remove o campo de email para testar obrigatoriedade
    #     del invalid_data["email"]
    #     # Cria o serializer com o campo email faltante e testa para ver se é possível.
    #     serializer = ContatoSerializerv2(data=invalid_data)
    #     self.assertTrue(serializer.is_valid())

    # Verifica se o serializer v2 funciona corretamente com um campo obrigatório faltante.
    def test_contato_serializerv2_invalid_missing_mandatory_field(self):
        # Duplica a data do json da segunda Versão para não alterar o campo original
        invalid_data = self.contato_data_v2.copy()
        # Remove o campo de email para testar obrigatoriedade
        del invalid_data["name"]
        # Cria o serializer com o campo email faltante e testa para ver se é possível.
        serializer = ContatoSerializerv2(data=invalid_data)
        self.assertFalse(serializer.is_valid())