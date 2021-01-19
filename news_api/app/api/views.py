from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsGetSerializer, NewsPostSerializer, NewsPutSerializer
from .pagination import NewsCursorPagination


class NonExistentPathView(APIView):
    @staticmethod
    def response_api_not_found():
        return Response('Such api url does not exist.', status.HTTP_404_NOT_FOUND)

    def get(self, request):
        return self.response_api_not_found()

    def post(self, request):
        return self.response_api_not_found()

    def put(self, request):
        return self.response_api_not_found()

    def delete(self, request):
        return self.response_api_not_found()


class NewsApiView(APIView):
    paginator = NewsCursorPagination()

    def get(self, request, news_id=None):
        if news_id is None:
            instance = News.objects.all()
            page = self.paginator.paginate_queryset(instance, request, self)
            serializer = self.paginator.get_paginated_response(NewsGetSerializer(page, many=True).data)
            return Response(serializer.data)
        else:
            self.check_news_exist(news_id)
            serializer = NewsGetSerializer(News.objects.get(id=news_id))

        return Response(serializer.data)

    def post(self, request, news_id=None):
        data = self.get_request_data(request, news_id)
        serializer = NewsPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return self.response_change_success(news_id, 'post')

        return self.response_bad_request(serializer)

    def put(self, request, news_id=None):
        self.check_news_exist(news_id)
        data = self.get_request_data(request, news_id)
        serializer = NewsPutSerializer(data=data)
        if serializer.is_valid():
            serializer.update(instance=News.objects.get(id=news_id), validated_data=serializer.validated_data)
            return self.response_change_success(news_id, 'update')

        return self.response_bad_request(serializer)

    def delete(self, request, news_id=None):
        self.check_news_exist(news_id)
        instance = News.objects.get(id=news_id)
        instance.delete()
        return self.response_change_success(news_id, 'delete')


    @staticmethod
    def response_bad_request(serializer):
        output = {
            'Required format': 'JSON',
            'Errors': serializer.errors
        }
        return Response(output, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def response_change_success(news_id, method_name):
        method_ending = 'ed' if method_name[-1] != 'e' else 'd'
        output = f'News with id {news_id} successfully {method_name}{method_ending}.'
        return Response(output, status.HTTP_200_OK)

    @staticmethod
    def check_news_exist(news_id):
        if news_id is None or not News.objects.all().filter(id=news_id).exists():
            raise Http404

    @staticmethod
    def get_request_data(request, news_id):
        data = {'id': news_id}
        data.update(request.data)
        return data

# Create your views here.
