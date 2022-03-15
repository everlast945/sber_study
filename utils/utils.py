from django.utils import timezone


LIST_CREATE_METHODS = {
    'get': 'list',
    'post': 'create',
}

RETRIEVE_UPDATE_DELETE_METHODS = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
}


def generate_uniq_code():
    return str(timezone.now().timestamp()).replace('.', '')
