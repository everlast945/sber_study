from study.models import Intern
from utils.filterset import SearchFilterSet


class InternFilter(SearchFilterSet):
    search_fields = ('fio', )

    class Meta:
        model = Intern
        fields = (
            'birthday_year',
        )
