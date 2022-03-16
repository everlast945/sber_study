from django.urls import reverse_lazy

from study.models import Subject
from study.tests.factories import SubjectFactory, DirectionFactory, InternFactory
from utils.tests import TestCaseBase


class SubjectViewTest(TestCaseBase):

    def setUp(self) -> None:
        super().setUp()

    def test_list(self):
        subject = SubjectFactory()
        url = reverse_lazy('study:subjects_list_create')
        self._test_list(url, subject)

    def test_retrieve(self):
        subject = SubjectFactory()
        url = reverse_lazy('study:subjects_manage', kwargs=dict(pk=subject.id))
        self._test_retrive(url, subject, 'name')

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


class InternViewTest(TestCaseBase):
    def test_list(self):
        intern = InternFactory()
        url = reverse_lazy('study:interns_list_create')
        self._test_list(url, intern)

    def test_retrieve(self):
        intern = InternFactory()
        url = reverse_lazy('study:interns_manage', kwargs=dict(pk=intern.id))
        self._test_retrive(url, intern, 'fio')


class DirectionViewTest(TestCaseBase):
    def test_list(self):
        direction = DirectionFactory()
        url = reverse_lazy('study:directions_list_create')
        self._test_list(url, direction)

    def test_retrieve(self):
        direction = DirectionFactory()
        url = reverse_lazy('study:directions_manage', kwargs=dict(pk=direction.id))
        self._test_retrive(url, direction, 'name')
