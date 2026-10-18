import shutil
import tempfile

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Perfil


class PerfilViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carlos', email='carlos@example.com', password='secret123'
        )
        self.perfil, _ = Perfil.objects.get_or_create(user=self.user)
        self.perfil.apellido_paterno = 'Perez'
        self.perfil.apellido_materno = 'Lopez'
        self.perfil.save()
        self.client.force_login(self.user)

    def test_perfil_requiere_login(self):
        self.client.logout()
        response = self.client.get(reverse('home:perfil'))
        self.assertRedirects(
            response,
            f"{reverse('home:login')}?next={reverse('home:perfil')}",
        )

    def test_perfil_muestra_sidebar_y_datos(self):
        response = self.client.get(reverse('home:perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/sidebar_base.html')
        self.assertTemplateUsed(response, 'partials/sidebar.html')
        self.assertContains(response, 'panel-sidebar')
        self.assertContains(response, 'carlos')
        self.assertContains(response, 'Perez')
        self.assertContains(response, 'Lopez')
        self.assertContains(response, 'carlos@example.com')
        self.assertContains(response, reverse('home:crud_perfil'))
        self.assertContains(response, 'uploads/profile-default.jpg')

    def test_crud_perfil_get_muestra_formulario(self):
        response = self.client.get(reverse('home:crud_perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/crud_perfil.html')
        self.assertContains(response, 'enctype="multipart/form-data"')
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="first_name"')
        self.assertContains(response, 'name="apellido_paterno"')
        self.assertContains(response, 'name="apellido_materno"')
        self.assertContains(response, 'type="file"', count=1)
        self.assertContains(response, reverse('home:perfil'))

    def test_crud_perfil_guarda_cambios(self):
        response = self.client.post(
            reverse('home:crud_perfil'),
            {
                'username': 'carlos2',
                'email': 'nuevo@example.com',
                'first_name': 'Carlos Eduardo',
                'apellido_paterno': 'Garcia',
                'apellido_materno': 'Mendez',
            },
        )
        self.assertRedirects(response, reverse('home:perfil'))
        self.user.refresh_from_db()
        self.perfil.refresh_from_db()
        self.assertEqual(self.user.username, 'carlos2')
        self.assertEqual(self.user.email, 'nuevo@example.com')
        self.assertEqual(self.user.first_name, 'Carlos Eduardo')
        self.assertEqual(self.perfil.apellido_paterno, 'Garcia')
        self.assertEqual(self.perfil.apellido_materno, 'Mendez')

    def test_crud_perfil_username_invalido_redirige_con_error(self):
        response = self.client.post(
            reverse('home:crud_perfil'),
            {'username': '   ', 'email': '', 'first_name': ''},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home:crud_perfil'))
        self.assertContains(
            self.client.get(reverse('home:crud_perfil')),
            'El usuario es obligatorio.',
        )

    def test_crud_perfil_username_duplicado_redirige_con_error(self):
        User.objects.create_user(username='ocupado', password='x')
        response = self.client.post(
            reverse('home:crud_perfil'),
            {'username': 'ocupado', 'email': '', 'first_name': ''},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home:crud_perfil'))
        self.assertContains(
            self.client.get(reverse('home:crud_perfil')),
            'ya está en uso',
        )

    def test_header_enlaza_a_perfil(self):
        response = self.client.get(reverse('home:index'))
        self.assertContains(response, reverse('home:perfil'))

    def test_logout_cierra_sesion_y_redirige_a_login(self):
        response = self.client.post(reverse('home:logout'))
        self.assertRedirects(response, reverse('home:login'))
        self.assertNotIn('_auth_user_id', self.client.session)


class FotoPerfilTests(TestCase):
    def setUp(self):
        self.media_root = tempfile.mkdtemp(prefix='canaco-test-media-')
        self.settings_override = override_settings(MEDIA_ROOT=self.media_root)
        self.settings_override.enable()
        self.user = User.objects.create_user(username='fotos', password='x')
        self.perfil, _ = Perfil.objects.get_or_create(user=self.user)
        self.client.force_login(self.user)

    def tearDown(self):
        self.settings_override.disable()
        shutil.rmtree(self.media_root, ignore_errors=True)

    def test_subir_foto_actualiza_perfil(self):
        foto = SimpleUploadedFile(
            'avatar.jpg', b'\xff\xd8\xff\xe0fakejpeg', content_type='image/jpeg'
        )
        response = self.client.post(
            reverse('home:crud_perfil'),
            {
                'username': 'fotos',
                'email': '',
                'first_name': '',
                'apellido_paterno': '',
                'apellido_materno': '',
                'foto': foto,
            },
        )
        self.assertRedirects(response, reverse('home:perfil'))
        self.perfil.refresh_from_db()
        self.assertIsNotNone(self.perfil.foto_perfil)
        self.assertTrue(self.perfil.foto_perfil.display_url)
        self.assertNotEqual(self.perfil.foto_perfil.display_url, '')

        response = self.client.get(reverse('home:perfil'))
        self.assertContains(response, self.perfil.foto_perfil.display_url)
