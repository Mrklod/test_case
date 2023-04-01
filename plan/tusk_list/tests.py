from django.test import TestCase, Client
from django.utils import timezone

from .models import Tusk
from users.models import Users


class TestTusk(TestCase):

    def test_main(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_auth(self):
        c = Client()
        response = c.post('/login/', {'username': 'Sasha', 'password': '214356'})
        self.assertEqual(response.status_code, 200)


class TuskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя, который будет автором задачи
        user = Users.objects.create(username='testuser')
        user.set_password('testpass')
        user.phone = '33434'
        user.save()

        # Создаем задачу
        Tusk.objects.create(
            title='Test Tusk',
            text='Test Tusk Text',
            time_create=timezone.now(),
            author=user
        )

    def test_title_max_length(self):
        tusk = Tusk.objects.get(id=1)
        max_length = tusk._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_time_create_is_auto_now_add(self):
        tusk = Tusk.objects.get(id=1)
        self.assertIsNotNone(tusk.time_create)

    def test_author_is_foreign_key(self):
        tusk = Tusk.objects.get(id=1)
        author = tusk._meta.get_field('author')
        self.assertEquals(author.__class__.__name__, 'ForeignKey')
        self.assertEquals(author.related_model.__name__, 'Users')