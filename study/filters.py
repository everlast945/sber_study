from study.models import Intern
from utils.filterset import SearchFilterSet


class InternFilter(SearchFilterSet):
    search_fields = ('fio', )

    class Meta:
        model = Intern
        fields = (
            'birthday_year',
        )


class InternRetrieveFilter(SearchFilterSet):

    @property
    def qs(self):
        qs = super().qs
        qs = qs.prefetch_related('intern_subjects__subject')
        return qs
