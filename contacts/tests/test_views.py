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
        response = self.client.get(f"/api/v1/contatos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_filter_by_name(self):
        response = self.client.get(f"{self.list_url}?name=João", HTTP_API_VERSION="v1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "João Silva")

    # def test_create_contato(self):
    #     data = {
    #         "name": "Carlos Pereira",
    #         "cellular": "+5511912345678",
    #         "email": "carlos.pereira@example.com",
    #         "region": "SP",
    #     }
    #     response = self.client.post(self.list_url, data, HTTP_API_VERSION="v2")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Contato.objects.count(), 3)

    # def test_update_contato(self):
    #     update_url = reverse("contato-detail", args=[self.contato1.id])
    #     data = {
    #         "name": "João Silva Atualizado",
    #         "cellular": "+5511999999999",
    #         "email": "joao.silva@example.com",
    #         "region": "BR",
    #     }
    #     response = self.client.put(update_url, data, HTTP_API_VERSION="v2")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.contato1.refresh_from_db()
    #     self.assertEqual(self.contato1.name, "João Silva Atualizado")

    # def test_delete_contato(self):
    #     delete_url = reverse("contato-detail", args=[self.contato1.id])
    #     response = self.client.delete(delete_url, HTTP_API_VERSION="v1")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Contato.objects.count(), 1)

    # def test_pagination(self):
    #     for i in range(15):
    #         Contato.objects.create(
    #             name=f"Contato {i}",
    #             cellular=f"+55119999999{i}",
    #             email=f"contato{i}@example.com",
    #             region="BR",
    #         )
    #     response = self.client.get(f"{self.list_url}?page=2", HTTP_API_VERSION="v2")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn("results", response.data)
    #     self.assertEqual(len(response.data["results"]), 10)  # Supondo PAGE_SIZE=10
