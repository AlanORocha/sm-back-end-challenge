from rest_framework.test import APITestCase
from rest_framework import status
from contacts.models import Contato


class TestContatoViewSet(APITestCase):
    # Cria dois objetos com a informação relacionada ao modelo de Contatos da Versão 2.
    def setUp(self):
        self.contato1 = Contato.objects.create(
            name="Contato 1",
            cellular="+5511999999999",
            email="contato.1@teste.com",
            region="BR",
        )
        self.contato2 = Contato.objects.create(
            name="Contato 2",
            cellular="+5511988888888",
            email="contato.2@teste.com",
            region="BR",
        )

    # Verifica se os contatos estão sendo listados corretamente
    def test_list_contatosv1(self):
        # Obtém os contatos existentes
        response = self.client.get(f"/api/v1/contatos/")
        # Verifica se foi possível realizar a ação
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se apenas os itens criados no setUp existem atualmente no banco de testes
        self.assertEqual(len(response.data["results"]), 2)

    # Testa o filtro de nome
    def test_filter_by_name(self):
        # Obtém o contato especificado
        response = self.client.get(f"/api/v1/contatos/?name=Contato 1")
        # Verifica se foi possível realizar a ação
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se apenas o item especificado foi retornado
        self.assertEqual(len(response.data["results"]), 1)
        # Verifica se o que foi retornado foi o item pesquisado
        self.assertEqual(response.data["results"][0]["name"], "Contato 1")

    # Testa criar o contato - V1
    def test_create_contatov1(self):
        # Cria o JSON de contato
        data = {"name": "Contato Teste", "cellular": "+5511912345678"}
        # Cria o contato
        response = self.client.post(f"/api/v1/contatos/", data=data)
        # Verifica se foi possível realizar a ação
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verifica se existem três contatos no banco
        self.assertEqual(Contato.objects.count(), 3)

    # Testa criar o contato - V2
    def test_create_contatov2(self):
        # Cria o JSON de contato
        data = {
            "name": "Contato Teste",
            "cellular": "+5511912345678",
            "email": "contato.teste@teste.com",
            "region": "USA",
        }
        # Cria o contato
        response = self.client.post(f"/api/v2/contatos/", data=data)
        # Verifica se foi possível realizar a ação
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verifica se existem três contatos no banco
        self.assertEqual(Contato.objects.count(), 3)

    # Testa atualizar o contato
    def test_update_contato(self):
        # Pega o ID do contato 1
        args = str([self.contato1.id][0])
        # Cria o URL com o ID
        update_url = f"/api/v2/contatos/{args}/"
        # Cria a DATA para atualizar o contato
        data = {
            "name": "Contato Atualizado",
            "cellular": "+5511000000000",
            "email": "contato_atualizado@gmail.com",
            "region": "RU",
        }
        # Atualiza o Contato
        response = self.client.put(update_url, data)
        # Verifica se foi possível realizar a ação
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Atualiza o contato no Banco de dados
        self.contato1.refresh_from_db()
        # Certifica de que o nome do contato 1 tenha sido atualizado
        self.assertEqual(self.contato1.name, "Contato Atualizado")

    # Testa deletar o contato
    def test_delete_contato(self):
        # Pega o ID do contato 1
        args = str([self.contato1.id][0])
        # Cria o URL com o ID
        delete_url = f"/api/v2/contatos/{args}/"
        # Realiza a ação
        response = self.client.delete(delete_url)
        # Verifica se foi possível apagar o contato
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verifica se existe apenas 1 contato no banco
        self.assertEqual(Contato.objects.count(), 1)

    # Teste para testar a paginação
    def test_pagination(self):
        for i in range(15):
            Contato.objects.create(
                name=f"Contato {i}",
                cellular=f"+55119999999{i}",
                email=f"contato.{i}@teste.com",
                region="BR",
            )
        # Lista os contatos na segunda pagina
        response = self.client.get(f"/api/v2/contatos/?page=1")
        # Verifica se foi possível realizar a ação
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se "results" está dentro do response, verificando se foi aplicado corretamente o modelo de paginação
        self.assertIn("results", response.data)
        # Verifica se existem apenas 10 contatos na primeira página, dado que a paginação é suposta a ser apenas 10 objetos
        self.assertEqual(len(response.data["results"]), 10)
