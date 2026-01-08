from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        page_data = {
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        }
        if not self.page.paginator.count :
            page_data["current_page"] = 0
            page_data["total_pages"] = 0
        if self.page.paginator.num_pages > self.page.number:
            page_data["next_page"] = self.page.number + 1 
        if self.page.number > 1:
            page_data["previous_page"] = self.page.number - 1 
        return Response(page_data)