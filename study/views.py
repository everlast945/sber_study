from study.filters import InternFilter, InternRetrieveFilter, SubjectListFilter
from study.models import Intern, Subject, Direction
from study.serializers import InternListSerializer, InternCreateUpdateSerializer, InternRetrieveSerializer, \
    SubjectListRetrieveSerializer, DirectionListSerializer, DirectionRetrieveSerializer, SubjectCreateUpdateSerializer, \
    DirectionCreateUpdateSerializer
from utils.views import MultiSerializerViewSet


class InternViewSet(MultiSerializerViewSet):
    """
    Тут сделал 1 пример с комментариями (они потом попадают в документацию)
    """
    queryset = Intern.objects.all()
    filtersets = {
        'list': InternFilter,
        'retrieve': InternRetrieveFilter,
    }
    serializers = {
        'list': InternListSerializer,
        'retrieve': InternRetrieveSerializer,
        'create': InternCreateUpdateSerializer,
        'update': InternCreateUpdateSerializer,
        'partial_update': InternCreateUpdateSerializer,
    }

    def list(self, request, *args, **kwargs):
        """
        Список поступающих
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создание поступающего
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Чтение поступающего
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Обновление поступающего
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частичное обновление поступающего
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удаление поступающего
        """
        return super().destroy(request, *args, **kwargs)


class SubjectViewSet(MultiSerializerViewSet):
    """
    Тут сделал пример без комментариев. Просто быстрее
    """
    queryset = Subject.objects.all()
    filtersets = {
        'list': SubjectListFilter,
    }
    serializers = {
        'list': SubjectListRetrieveSerializer,
        'retrieve': SubjectListRetrieveSerializer,
        'create': SubjectCreateUpdateSerializer,
        'update': SubjectCreateUpdateSerializer,
        'partial_update': SubjectCreateUpdateSerializer,
    }


class DirectionViewSet(MultiSerializerViewSet):
    """
    Тут сделал пример без комментариев. Просто быстрее и фильтров
    """
    queryset = Direction.objects.all()
    serializers = {
        'list': DirectionListSerializer,
        'retrieve': DirectionRetrieveSerializer,
        'create': DirectionCreateUpdateSerializer,
        'update': DirectionCreateUpdateSerializer,
        'partial_update': DirectionCreateUpdateSerializer,
    }




