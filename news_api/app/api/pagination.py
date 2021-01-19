from rest_framework.pagination import CursorPagination
from django.conf import settings


class NewsCursorPagination(CursorPagination):
    page_size = settings.NEWS_PAGE_SIZE
    page_size_query_param = 'page_size'
    ordering = '-creation_date'
