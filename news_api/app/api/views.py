from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer, NewsPutSerializer


def test_add(request):
    news = News.objects.all()
    for new in news:
        print(new.id, new.author, new.creation_date, new.text)
    return HttpResponse('ok')


class NewsApiView(APIView):
    def response_bad_request(self, serializer):
        output = {
            'Required format': 'JSON',
            'Errors': serializer.errors
        }
        return Response(output, status=status.HTTP_400_BAD_REQUEST)

    def response_update_success(self, news_id, method_name):
        output = f'News with id {news_id} successfully {method_name}ed.'
        return Response(output, status.HTTP_200_OK)

    def response_not_found(self, news_id):
        return Response(f'News with id {news_id} does not exist.', status=status.HTTP_404_NOT_FOUND)

    def check_news_exist(self, news_id):
        if not News.objects.all().filter(id=news_id).exists():
            return self.response_not_found(news_id)

    def get(self, request, news_id=None):
        if news_id is None:
            serializer = NewsSerializer(News.objects.all(), many=True)
        else:
            _404 = self.check_news_exist(news_id)
            if _404 is not None:
                return _404

            serializer = NewsSerializer(News.objects.get(id=news_id))

        return Response(serializer.data)

    def post(self, request, news_id=None):
        data = {'id': news_id}
        data.update(request.data)
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return self.response_update_success(news_id, 'post')

        return self.response_bad_request(serializer)

    def put(self, request, news_id=None):
        data = {'id': news_id}
        data.update(request.data)
        serializer = NewsPutSerializer(data=data)
        if serializer.is_valid():
            return Response('ok')

        return self.response_bad_request(serializer)

# Create your views here.
