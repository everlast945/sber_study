import factory
from factory import fuzzy

from study.models import Subject, Intern, Direction, InternSubject


class SubjectFactory(factory.django.DjangoModelFactory):
    """
    Фабрика предмета
    """
    class Meta:
        model = Subject

    name = fuzzy.FuzzyText(length=100)
    min_score = factory.fuzzy.FuzzyInteger(low=0, high=100)


class InternFactory(factory.django.DjangoModelFactory):
    """
    Фабрика поступающего
    """
    class Meta:
        model = Intern
    fio = fuzzy.FuzzyText(length=100)
    birthday_year = fuzzy.FuzzyInteger(low=1990, high=2010)
    passport_number = fuzzy.FuzzyText(length=10)


class InternSubjectFactory(factory.django.DjangoModelFactory):
    """
    Фабрика балла по предмету поступающего
    """
    class Meta:
        model = InternSubject

    intern = factory.SubFactory(InternFactory)
    subject = factory.SubFactory(SubjectFactory)
    score = fuzzy.FuzzyInteger(low=0, high=100)


class DirectionFactory(factory.django.DjangoModelFactory):
    """
    Фабрика направления
    """
    class Meta:
        model = Direction
    name = fuzzy.FuzzyText(length=100)
