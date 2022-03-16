from django.db import models


class Subject(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)
    min_score = models.PositiveSmallIntegerField('Минимальный балл')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Intern(models.Model):
    fio = models.CharField('ФИО', max_length=250)
    birthday_year = models.PositiveSmallIntegerField('Год рождения')
    passport_number = models.CharField('Номер паспорта', max_length=10)
    subjects = models.ManyToManyField(
        Subject,
        related_name='interns',
        through='InternSubject',
        through_fields=('intern', 'subject'),
        verbose_name='Предметы, которые он сдавал и баллы по ним'
    )

    class Meta:
        verbose_name = 'Поступающий'
        verbose_name_plural = 'Поступающие'

    def __str__(self):
        return self.fio

    def save_subjects(self, subjects):
        if subjects is None:
            # Это если на редактирование ничего не отправили
            return
        new_ids = []
        for subject in subjects:
            instance, _ = InternSubject.objects.update_or_create(
                intern=self, defaults=subject
            )
            new_ids.append(instance.id)
        InternSubject.objects.filter(intern=self).exclude(pk__in=new_ids).delete()


class InternSubject(models.Model):
    intern = models.ForeignKey(
        Intern,
        verbose_name='Поступающий',
        on_delete=models.CASCADE,
        related_name='intern_subjects'
    )
    subject = models.ForeignKey(
        Subject,
        verbose_name='Предмет',
        on_delete=models.CASCADE,
        related_name='subject_interns'
    )
    score = models.PositiveSmallIntegerField('Балл по предмету')

    class Meta:
        unique_together = ('intern', 'subject')
        verbose_name = 'Балл по предмету'
        verbose_name_plural = 'Баллы по предметам'


class Direction(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)
    interns = models.ManyToManyField(Intern, verbose_name='Поступающие')
    subjects = models.ManyToManyField(
        Subject,
        related_name='directions',
        verbose_name='Предметы, которые нужны для поступления на это направление'
    )

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name
