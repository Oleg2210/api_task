from rest_framework.pagination import CursorPagination


class NewsCursorPagination(CursorPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    ordering = '-creation_date'
