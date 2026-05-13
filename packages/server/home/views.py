from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests

# CACHING IN FUNCTION BASE VIEW

# @cache_page(5 * 60)
# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = request.get('https//httpbin.org/delay/2')
#         data = response.json()
#         return render(request, 'hello.html', {'name': cache.get(key)})


# CACHING IN CLASSBASE VIEW

class HelloView(APIView):
    def get(self, request):
        response = request.get('https//httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': 'Mosh'})
