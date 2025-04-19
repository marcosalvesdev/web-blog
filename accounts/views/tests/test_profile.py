from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile


class UpdateProfileViewTests(TestCase):
    def setUp(self):
        # CriaAdicione aqui testes unitários us
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.profile = Profile.objects.create(user=self.user, bio="Test bio")
        self.client.login(username="testuser", password="password123")
        self.url = reverse(
            f"accounts:profile_update {self.user.username}"
        )  # Substitua pelo nome correto da URL

    def test_update_profile_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_profile_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(
            response, "accounts/profile_update.html"
        )  # Substitua pelo nome correto do template

    def test_update_profile_successful(self):
        data = {
            "bio": "Updated bio",
        }
        response = self.client.post(self.url, data)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, "Updated bio")
        self.assertRedirects(
            response, reverse("accounts:profile_detail")
        )  # Substitua pelo nome correto da URL de redirecionamento

    def test_update_profile_invalid_data(self):
        data = {
            "bio": "",  # Supondo que o campo bio não pode ser vazio
        }
        response = self.client.post(self.url, data)
        self.profile.refresh_from_db()
        self.assertNotEqual(self.profile.bio, "")  # O valor não deve ser atualizado
        self.assertEqual(
            response.status_code, 200
        )  # Deve retornar a página com errosando o sistema de testes do Django para a view accounts.views.profile.UpdateProfileView. um usuário e um perfil associado
