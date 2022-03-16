from study.models import Intern, Direction
from utils.filterset import SearchFilterSet
from django_filters import rest_framework as filters


class InternFilter(SearchFilterSet):
    # Поиск по полям ?q=Иванов
    search_fields = ('fio', )

    class Meta:
        model = Intern
        # Фильтры по полям из модели
        fields = (
            'birthday_year',
        )


class InternRetrieveFilter(SearchFilterSet):

    @property
    def qs(self):
        """
        Тут сладываю оптимизации/аннотации и т.д
        """
        qs = super().qs
        qs = qs.prefetch_related('intern_subjects__subject')
        return qs


class SubjectListFilter(SearchFilterSet):
    direction = filters.ModelChoiceFilter(queryset=Direction.objects.all(), method='filter_direction')

    def filter_direction(self, qs, name, direction):
        if not direction:
            return qs
        return qs.filter(directions=direction).distinct()
