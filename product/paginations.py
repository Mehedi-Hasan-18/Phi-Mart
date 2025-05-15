from rest_framework.pagination import PageNumberPagination

class DefaulfPagination(PageNumberPagination):
    page_size = 10