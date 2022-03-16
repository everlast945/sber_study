import json

from django.test import override_settings
from django.utils.timezone import now as tz_now

from rest_framework.test import APITestCase
from users.models import User


@override_settings(SQL_DEBUG=False)
class TestCaseBase(APITestCase):
    CONTENT_TYPE_JSON = 'application/json'

    @classmethod
    def setUpClass(cls):
        cls.user_pass = 'admin'
        user, is_create = User.objects.get_or_create(username='admin')
        if is_create:
            user.set_password(cls.user_pass)
            user.save()
        cls.user = user
        super().setUpClass()

    def setUp(self) -> None:
        self.auth_user(self.user)
        super().setUp()

    def auth_user(self, user):
        self.client.login(username=user.username, password=self.user_pass)

    def generate_uniq_code(self):
        return str(tz_now().timestamp()).replace('.', '')

    def _post(self, url, data):
        return self.client.post(url, data=json.dumps(data), content_type=self.CONTENT_TYPE_JSON)

    def _put(self, url, data):
        return self.client.put(url, data=json.dumps(data), content_type=self.CONTENT_TYPE_JSON)

    def _test_list(self, url, object_):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response.data)
        rows = response.data['results']
        self.assertEqual([row['id'] for row in rows if row['id'] == object_.pk], [object_.pk])

    def _test_retrive(self, url, object_, check_name):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data[check_name], getattr(object_, check_name))

    def _test_destroy(self, url, object_):
        qs = type(object_).objects.filter(id=object_.id)
        self.assertTrue(qs.exists())
        self.client.delete(url)
        self.assertFalse(qs.exists())
