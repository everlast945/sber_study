from django.urls import reverse_lazy

from study.models import Subject
from study.tests.factories import SubjectFactory
from utils.tests import TestCaseBase


class SubjectViewTest(TestCaseBase):

    def setUp(self) -> None:
        super().setUp()

    def test_list(self):
        subject = SubjectFactory()
        url = reverse_lazy('study:subjects_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        rows = response.data['results']
        self.assertEqual([row['id'] for row in rows if row['id'] == subject.pk], [subject.pk])

    def test_retrieve(self):
        subject = SubjectFactory()
        url = reverse_lazy('study:subjects_manage', kwargs=dict(pk=subject.id))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], subject.name)

    def test_create(self):
        data = {
            'name': self.generate_uniq_code(),
            'min_score': 50,
        }
        url = reverse_lazy('study:subjects_list_create')
        response = self._post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])

    def test_update(self):
        subject = SubjectFactory()
        data = {
            'name': self.generate_uniq_code(),
            'min_score': 50,
        }
        url = reverse_lazy('study:subjects_manage', kwargs=dict(pk=subject.id))
        response = self._put(url, data)
        self.assertEqual(response.status_code, 200)
        updated_subject = Subject.objects.filter(id=subject.id).first()
        self.assertNotEqual(updated_subject.name, subject.name)
